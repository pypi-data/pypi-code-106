"""Main file for the monito package

LICENSE
   MIT (https://mit-license.org/)

COPYRIGHT
   © 2021 Steffen Brinkmann <s-b@mailbox.org>
"""

__version__ = "0.1.0"

import argparse
import csv
import locale
import logging
import os
import time

import requests  # type: ignore
import toml
import urllib3
import feedparser
import requests

from datetime import datetime
from time import mktime

from alive_progress import alive_bar
from bs4 import BeautifulSoup  # type: ignore
from numpy.random import shuffle
from selenium import webdriver
from selenium.common.exceptions import (StaleElementReferenceException,
                                        TimeoutException)
from selenium.webdriver.common.by import By

try:
    from article import Article
    from parsers import parser, parser_rss
    from tools import process_article_text
except ModuleNotFoundError:
    from .article import Article
    from .parsers import parser, parser_rss
    from .tools import process_article_text

_MONITO_DEBUG_MODE = False
_MONITO_QUIET_MODE = False

logging_format = "monito | %(name)s | %(asctime)s | %(levelname)-8s | %(message)s"
logging.basicConfig(format=logging_format, level=logging.INFO)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept-Encoding": "*",
    "Connection": "keep-alive",
}


def _set_logging_level(
    quiet: bool, verbose: bool, debug: bool
) -> None:  # pragma: no cover
    if debug is True:
        logging.getLogger().setLevel(logging.DEBUG)
        logging.info("debug mode engaged")
    if verbose is True:
        logging.getLogger().setLevel(logging.INFO)
    if quiet is True:
        logging.getLogger().setLevel(logging.ERROR)


def _parse_arguments(argv=None):
    # parse the command line options
    argparser = argparse.ArgumentParser(
        description="monito: a tool for monitoring and filtering news feeds. "
        "Please have a look at the documentation (https://monito.readthedocs.io/en/latest/) "
        "for further information on how tho use this software.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    argparser.add_argument(
        "-c",
        "--config",
        type=str,
        nargs="+",
        help="One or more configuration files. [mandatory]",
    )
    argparser.add_argument(
        "-s",
        "--scrape-page",
        type=int,
        default=0,
        help="Which page to scrape additionally.",
    )

    argparser.add_argument(
        "-p",
        "--pages",
        type=int,
        default=0,
        help="How many pages to scrape. If 0, all available pages are scraped.",
    )
    argparser.add_argument(
        "-a",
        "--articles",
        type=int,
        default=0,
        help="How many articles to scrape. If 0, all available pages are scraped.",
    )
    argparser.add_argument(
        "-o",
        "--output-directory",
        type=str,
        default=None,
        help="The directory to save the articles. Overwrites the setting in the configuration file.",
    )
    argparser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="Switch off text output except for error messages. This will overwrite -v.",
    )
    argparser.add_argument(
        "--shuffle",
        action="store_true",
        help="Shuffle the pages before downloading links from them.",
    )
    argparser.add_argument(
        "-v", "--verbose", action="store_true", help="more verbose text output"
    )
    argparser.add_argument(
        "-d",
        "--debug",
        action="store_true",
        help="switch on debug mode. This will show intermediate results and plots, as well as "
        "log a lot of debugging information.",
    )
    argparser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
        help="show the version of this software",
    )
    return argparser.parse_args(argv)


def get_page(url: str) -> str:
    """get raw content from url"""
    logging.debug(f"get content from: {url}")
    r = requests.get(url, headers=headers)
    logging.debug(f"status {r.status_code}")

    if r.status_code != 200:
        logging.warning(f"{r.status_code} for {url}")
        raise Exception(f"status code {r.status_code} for {url}")

    result = r.text

    return result


def get_article_links(url: str, driver, sleep_s: int = 5) -> set:
    """retrieve all links to articles from a url"""

    logging.debug(f"get content from: {url}")
    success = False
    max_tries = 5
    tries = 0
    while not success:
        tries += 1
        if tries > max_tries:
            break
        try:
            driver.get(url)
            time.sleep(sleep_s)
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;"
            )
            time.sleep(1)
            success = True
        except TimeoutException:
            logging.debug(f"trying again... {tries} / {max_tries}")
            time.sleep(1)
        except ConnectionRefusedError:
            logging.debug(f"connection refused ({url})")
            time.sleep(1)
        except urllib3.exceptions.MaxRetryError:
            logging.debug(f"max retry error ({url})")
            time.sleep(1)
        # except Exception as e:
        #     logging.debug(f"connection error ({url})")
        #     logging.debug(e)
        #     time.sleep(1)

    logging.debug("finding links...")
    # links = driver.find_elements_by_xpath("//a[@href]")
    try:
        links = driver.find_elements(By.TAG_NAME, "a")
        result = {link.get_attribute("href") for link in links}
    except StaleElementReferenceException:
        logging.debug("StaleElementReferenceException")
        time.sleep(1)
        links = driver.find_elements(By.TAG_NAME, "a")
        result = {link.get_attribute("href") for link in links}
    except urllib3.exceptions.MaxRetryError:
        logging.debug(f"max retry error ({url})")
        time.sleep(1)
        result = set()

    if len(result) == 0:
        logging.warning(f"Could not load {url}")

    if None in result:
        result.remove(None)

    return result


def _get_article_links_0(url: str) -> set:
    """retrieve all links to articles from a url"""

    logging.debug(f"get content from: {url}")
    r = requests.get(url, headers=headers)
    logging.debug(f"status {r.status_code}")

    result = set()

    if r.status_code == 200:
        try:
            soup = BeautifulSoup(r.text, "lxml")
            html = soup.find("body")
            # print(html.find("div", attrs={"id": "container"}).find_all("a"))
        except Exception as e:
            logging.error(str(e))
        else:
            result = {
                link.get("href")
                for link in html.find("div", attrs={"id": "container"}).find_all("a")
            }
    else:
        logging.warning(f"{r.status_code} for {url}")

    return result


def scrape_pages(page_urls: list, config: dict) -> set:
    """scrape links from pages"""

    article_urls = set()
    logging.info(f"get links from {len(page_urls)} pages.")
    # create webdriver
    chrome_options = webdriver.chrome.options.Options()
    # chrome_options.add_argument("--disable-extensions")
    # chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument("--no-sandbox") # linux only
    chrome_options.add_argument("--headless")
    # chrome_options.headless = True # also works
    driver = webdriver.Chrome(options=chrome_options, service_log_path=os.path.devnull)
    driver.set_page_load_timeout(5)
    # driver = webdriver.Firefox()
    with alive_bar(len(page_urls)) as bar:
        for i, url in enumerate(page_urls, 1):
            logging.info(f"({i}/{len(page_urls)}) get links from {url}")
            links = get_article_links(url, driver, config["sleep_s"])
            logging.debug(f"{len(links)}")
            # logging.debug(f"{links}")
            article_urls.update(links)
            bar()
            if _MONITO_DEBUG_MODE:
                break

    # shut down driver
    driver.quit()

    # print("scrape_pages", "\n".join(sorted(map(str, article_urls))), sep="\n")

    return article_urls


def filter_links(article_urls: list, config: dict) -> list:
    """Filter a list of urls"""
    article_urls = {
        link
        for link in article_urls
        if isinstance(link, str) and link.startswith(config["base_url"])
    }
    article_urls = {
        link
        for link in article_urls
        if isinstance(link, str) and not link.endswith(".xml")
    }
    article_urls = {link for link in article_urls if link not in config["urls"]}
    article_urls = {link for link in article_urls if "/page/" not in link}
    article_urls = {link for link in article_urls if not link.endswith("hide")}
    article_urls = {link for link in article_urls if not link.endswith("@USER")}
    article_urls = {link for link in article_urls if not link.endswith("#respond")}

    for u in (config["exclude"]
              + [link + "#" for link in config["urls"]]
              + [link + "/#" for link in config["urls"]]
              ):
        article_urls = {link for link in article_urls if not link.startswith(u)}

    urls_in_db = get_urls_in_db(config)
    for u in urls_in_db:
        try:
            article_urls.remove(u)
        except KeyError:
            pass

    return article_urls


def get_urls_in_db(config: dict) -> None:
    """ get urls that have already been processed"""
    urls_in_db = []
    try:
        with open(
            os.path.join(config["output_directory"], "urls.csv"), newline=""
        ) as f:
            reader = csv.reader(f)
            urls_in_db = [row[0] for row in reader]
    except FileNotFoundError:
        logging.info(
            f"file {os.path.join(config['output_directory'], 'urls.csv')} not found."
        )

    return urls_in_db


def get_page_urls(config: dict, args: argparse.Namespace) -> list:
    """Compile the list of urls to scrape for links"""
    if args.scrape_page > 0:
        page_urls = [url + f"page/{args.scrape_page}/" for url in config["urls"]]
    else:
        page_urls = config["urls"]

    if args.pages > 0:
        if args.shuffle:
            shuffle(page_urls)
        page_urls = page_urls[: args.pages]
        logging.info(f"processing only {args.pages} pages")

    return page_urls


def download_rss_articles(
    page_urls: list, config: dict, args: argparse.Namespace
) -> list:
    """scrape links from the urls given in the config and download the articels from those links"""

    saved_articles = []
    for url in page_urls:
        feed = feedparser.parse(url)
        parsed_articles = parser_rss(config["parser"], feed)
        urls_in_db = get_urls_in_db(config)
        with alive_bar(len(feed.entries)) as bar:
            for article_dict in parsed_articles:
                if article_dict["url"] in urls_in_db:
                    bar()
                    continue
                process_article_text(article_dict, config)

                article_dict["version"] = __version__

                try:
                    logging.debug("creating and saving article")
                    article = Article(**article_dict)
                    json_filename = article.dump_json(outdir=config["output_directory"])
                except Exception as e:
                    logging.error("error while creating or saving article to file:")
                    logging.error(e)
                    logging.error(article_dict)
                    raise e
                    continue
                if _MONITO_DEBUG_MODE:
                    break

                saved_articles.append((article_dict["url"], json_filename))
                bar()

    return saved_articles


def download_web_articles(
    page_urls: list, config: dict, args: argparse.Namespace
) -> list:
    """scrape links from the urls given in the config and download the articels from those links"""

    article_urls = scrape_pages(page_urls, config)

    # print("1", "\n".join(sorted(article_urls)))

    # filter links
    article_urls = filter_links(article_urls, config)

    # print("2", "\n".join(sorted(article_urls)))
    # exit(11)

    logging.info(f"gathered {len(article_urls)} new links from {len(page_urls)} pages.")

    if args.articles > 0:
        article_urls = sorted(article_urls)[: args.articles]
        logging.info(f"processing only {args.articles} articles")

    # get articles from links
    saved_articles = []
    with alive_bar(len(article_urls)) as bar:
        for i, article_url in enumerate(sorted(article_urls),1):
            logging.info(f"processing article {i}/{len(article_urls)}: {article_url}")

            try:
                article_content = get_page(article_url)
                article_dict = parser(config["parser"], article_content)
            except AttributeError as e:
                logging.error(f"Error while parsing {article_url}")
                logging.error(e)
                continue

            assert isinstance(article_dict, dict)

            article_dict["url"] = article_url

            process_article_text(article_dict, config)

            article_dict["version"] = __version__

            try:
                logging.debug("creating and saving article")
                article = Article(**article_dict)
                json_filename = article.dump_json(outdir=config["output_directory"])
            except Exception as e:
                logging.error("error while creating or saving article to file:")
                logging.error(e)
                logging.error(article_dict)
                continue
            if _MONITO_DEBUG_MODE:
                break
            saved_articles.append((article_url, json_filename))
            bar()

    return saved_articles


def run(argv: list = None):
    """the command line tool. Please use the ``--help`` option to get help."""

    global _MONITO_QUIET_MODE
    global _MONITO_DEBUG_MODE

    # parse the command line options
    args = _parse_arguments(argv)

    # print the logo and version
    if args.quiet is False:  # pragma: no cover
        print(f"monito {__version__}")

    # set quiet mode
    _MONITO_QUIET_MODE = args.quiet

    # set debug mode
    _MONITO_DEBUG_MODE = args.debug

    # set verbosity level
    _set_logging_level(args.quiet, args.verbose, args.debug)
    logging.getLogger("selenium").setLevel(logging.WARNING)
    logging.getLogger("urllib3.connectionpool").setLevel(logging.ERROR)

    logging.debug(args)

    n_saved_articles = 0
    n_scraped_pages = 0

    for config_file in args.config:
        logging.debug(f"loading {config_file}")

        # load config
        config = toml.load(config_file)
        logging.debug(f"config:\n{config}")
        logging.info(f"=> Processing: {config['name']}")

        # set locale
        locale.setlocale(locale.LC_ALL, config["locale"])

        # set and create output directory if necessary
        if args.output_directory:
            output_directory = config["output_directory"] = args.output_directory
        else:
            output_directory = config["output_directory"]
        if not os.path.isdir(output_directory):
            logging.info(f"creating output directory {output_directory}")
            os.makedirs(output_directory)

        # get links from urls
        page_urls = get_page_urls(config, args)
        if config["type"] == "web":
            saved_articles = download_web_articles(page_urls, config, args)
        elif config["type"] == "rss":
            saved_articles = download_rss_articles(page_urls, config, args)
        else:
            logging.error(f"type {config['type']} unkown")
            continue

        # write urls.csv
        with open(os.path.join(output_directory, "urls.csv"), "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(saved_articles)

        # sum saved articles
        n_saved_articles += len(saved_articles)
        n_scraped_pages += len(page_urls)

    logging.info("==> summary:")
    logging.info(f"{len(args.config)} config files")
    logging.info(f"{n_scraped_pages} pages scraped")
    logging.info(f"{n_saved_articles} articles saved")


if __name__ == "__main__":
    run()
