"""Parsers for the monito package

LICENSE
   MIT (https://mit-license.org/)

COPYRIGHT
   © 2021 Steffen Brinkmann <s-b@mailbox.org>
"""

import logging
import re
from datetime import datetime
from bs4 import BeautifulSoup
import feedparser


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept-Encoding": "*",
    "Connection": "keep-alive",
}


def parser(parser_cfg: str, content: str) -> dict:
    """Wrapper funtion for parsers"""
    _parser = eval(parser_cfg)
    return _parser(content)


def parser_rss(parser_cfg: str, feed: feedparser.util.FeedParserDict) -> list:
    """retrieve the feed from the url and return the urls of the items as a list"""
    _parser = eval(parser_cfg)
    return _parser(feed)


def parse_8columnas(feed: feedparser.util.FeedParserDict) -> list:
    parsed_articles = []
    outlet = feed["channel"]["title"]
    for entry in feed.entries:
        article_dict = {}
        article_dict["outlet"] = outlet
        article_dict["title"] = entry.title
        article_dict["subtitle"] = entry.summary
        article_dict["url"] = entry.link
        article_dict["authors"] = [entry.author]
        article_dict["published"] = datetime(*entry.published_parsed[:5]).isoformat(timespec="minutes")
        article_dict["keywords"] =[tag.term for tag in entry.tags]
        article_dict["category"] = article_dict["keywords"][:1]
        article_dict["text"] = BeautifulSoup(entry.content[0].value, "lxml").get_text().strip()
        m = re.search(r"Por ([\w ]+)\.?\n", article_dict["text"])
        if m:
            article_dict["authors"] = [m.group(1)]
            article_dict["text"] = re.sub("Por " + m.group(1) + "\.?\n", "", article_dict["text"])
            article_dict["subtitle"] = re.sub("Por " + m.group(1), "", article_dict["subtitle"])
        article_dict["text"] = re.sub("\nFOTO: [^\n]+", "", article_dict["text"])

        parsed_articles.append(article_dict)

    return parsed_articles


def parse_quadratin(content: str) -> dict:
    """Parse an article from "Quadratin" """

    soup = BeautifulSoup(content, "lxml")
    html = soup.find("body")

    result = {}

    result["outlet"] = "Quadratín"

    post_info = html.find("div", attrs={"class": "single-post-info"})
    result["category"] = [
        cat.strip()
        for cat in post_info.find("div", attrs={"class": "category"}).text.split("/")
    ]
    result["title"] = post_info.find("h1").text.strip()
    result["authors"] = [
        post_info.find("div", attrs={"class": "redacted"})
        .text.split("/")[0]
        .strip()
        .replace("\n", " ")
    ]

    date_str = (
        html.find("div", attrs={"class": "date"}).text.strip()
        + " "
        + html.find("div", attrs={"class": "hour"}).text.strip()
    )
    result["published"] = datetime.strptime(date_str, "%d de %B de %Y %H:%M").isoformat(
        timespec="minutes"
    )
    result["text"] = "\n".join(
        [
            p.text.strip().replace("\n", " ")
            for p in html.find("div", attrs={"class": "post-content"}).find_all("p")
        ]
    ).strip()
    result["subtitle"] = result["text"].split("\n")[0]

    result["keywords"] = [
        tag["content"]
        for tag in soup.find("head").find_all("meta", attrs={"property": "article:tag"})
    ]

    # print([tag["content"] for tag in soup.find("head").find_all("meta", attrs={"property": "article:tag"})])

    return result


def parse_lavozdemichoacan(content: str) -> dict:
    """Parse an article from "La voz de Michoacan" """

    soup = BeautifulSoup(content, "lxml")
    html = soup.find("article")

    result = {}

    result["outlet"] = "La Voz de Michoacan"
    result["category"] = [
        html.find("span", attrs={"class": "cat-title"}).text.strip(" \t|")
    ]
    result["title"] = html.find("h1", attrs={"class": "post-title"}).text
    result["subtitle"] = html.find(
        "h4", attrs={"class": "post-excerpt"}
    ).next_sibling.text
    result["authors"] = [
        html.find("div", attrs={"class": "px-0"})
        .p.text.split("/")[0]
        .strip()
        .replace("\n", " ")
    ]
    if result["title"] == "MAQUIAVELO":
        result["authors"] = ["MAQUIAVELO"]
        if "maquiavelo" in result["url"].split("/")[-2]:
            result["title"] = result["url"].split("/")[-2]

    date_str = html.find("div", attrs={"class": "cat-date"}).text.strip()
    result["published"] = datetime.strptime(date_str, "%d %b, %Y, %H:%M").isoformat(
        timespec="minutes"
    )

    result["text"] = "\n".join(
        [
            p.text.strip().replace("\n", " ")
            for p in html.find("div", attrs={"class": "entry"}).find_all("p")
        ][1:]
    ).strip()

    result["keywords"] = []
    post_tag = soup.find("p", attrs={"class": "post-tag"})
    if post_tag:
        result["keywords"] = [
            tag.text.strip().strip('"') for tag in post_tag.find_all("a")
        ]

    # logging.debug(f"article_dict: {result}")
    return result


def parse_elsoldemorelia(content: str) -> dict:
    """Parse an article from "El Sol de Morelia" """

    soup = BeautifulSoup(content, "lxml")
    html = soup.find("section", attrs={"role": "main"})

    result = {}

    result["outlet"] = "El Sol de Morelia"

    if html.find("div", attrs={"class": "cartones-titulos"}):
        return result

    result["category"] = [html.find("div", attrs={"class": "breadcrumb"}).text.strip()]
    result["title"] = html.find("h1", attrs={"class": "title"}).text.strip()
    if "Analisis" in result["category"]:
        result["authors"] = [
            html.find("p", attrs={"class": "author"}).text.replace("\n", " ").strip()
        ]
    else:
        result["authors"] = [
            html.find("p", attrs={"class": "byline"}).text.split("|")[0].strip()
        ]

    date_str = (
        html.find("p", attrs={"class": "published-date"}).text.strip().strip("/ ")
    )

    for script in soup("script"):
        if script.text.strip().startswith("{") and script.text.strip().endswith("}"):
            m = re.search(r"\"datePublished\": \"(.*)\"", script.text)
            if m:
                result["published"] = datetime.fromisoformat(m.group(1)[:-3]).isoformat(
                    timespec="minutes"
                )
                print(result["published"])
                break
    else:
        result["published"] = datetime.strptime(
            date_str, "%A %d de %B de %Y"
        ).isoformat(timespec="minutes")

    result["text"] = (
        "\n".join(
            p.text.strip().replace("\n", " ")
            for p in html.find("article", "content-continued-body").find_all("p")
            if not p.find("a")
        )
        .strip()
        .replace("\n\n", "\n")
    )
    result["subtitle"] = ""
    if html.find("h3", attrs={"class": "subtitle"}):
        result["subtitle"] = (
            html.find("h3", attrs={"class": "subtitle"}).text.replace("\n", " ").strip()
        )

    tags_list = html.find("div", attrs={"class": "tags-list"}).find_all(
        "a", attrs={"class": "item-tags"}
    )
    result["keywords"] = [tag.text.strip() for tag in tags_list]

    return result


def parse_amlo(content: str) -> dict:
    """Parse an article from "AMLO" """

    soup = BeautifulSoup(content, "lxml")
    html = soup.find("article")

    result = {}

    result["outlet"] = "AMLO"

    # if html.find("div", attrs={"class": "cartones-titulos"}):
    #     return result

    result["category"] = [
        cat[9:] for cat in html["class"] if cat.startswith("category-")
    ]
    result["title"] = html.find("h1", attrs={"class": "entry-title"}).text.strip()

    result["keywords"] = [cat[4:] for cat in html["class"] if cat.startswith("tag-")]

    if "version-estenografica" in result["category"]:
        result["authors"] = list(
            {p.b.text.strip().strip(":") for p in html.find_all("p") if p.b}
        )
        result["authors"] = [
            a
            for a in result["authors"]
            if a
            not in [
                "",
                ",",
                "PREGUNTA",
                "INTERVENCIÓN",
                "INTERLOCUTORA",
                "INTERLOCUTOR",
            ]
        ]

    else:
        result["authors"] = []

    date_str = html.find("span", attrs={"class": "entry-date"}).text.strip()
    result["published"] = datetime.strptime(date_str, "%B %d, %Y").isoformat(
        timespec="minutes"
    )

    if len(html.find_all("p")) > 1:
        result["text"] = "\n".join(
            p.text.strip().replace("\n", " ").replace("+++++", "").replace("\n\n", "\n")
            for p in html.find_all("p")[2:]
        ).strip()
        result["subtitle"] = html.find_all("p")[1].text.strip()
    else:
        result["text"] = ""
        result["subtitle"] = ""

    return result


def parse_mimorelia(content: str) -> dict:
    """Parse an article from "Mi Morelia" """

    soup = BeautifulSoup(content, "lxml")
    html = soup.find("body")

    result = {}

    result["outlet"] = "Mi Morelia"

    result["category"] = [
        html.find("div", attrs={"data-test-id": "sectionTag"}).text.strip()
    ]
    result["title"] = html.find(
        "h1", attrs={"data-testid": "story-headline"}
    ).text.strip()

    result["keywords"] = []

    result["authors"] = [
        html.find("div", attrs={"data-test-id": "author-name"}).text.strip()
    ]

    date_str = html.find("time")["datetime"].strip()
    result["published"] = datetime.fromisoformat(date_str.strip("Z")).isoformat(
        timespec="minutes"
    )

    result["text"] = "\n".join(
        p.text.strip().replace("\n", " ")
        for p in html.find("div", attrs={"data-test-id": "text"}).find_all("p")
    ).strip()
    if re.match(r"\w+, \w+ \(MiMorelia.com\).-", result["text"]):
        result["text"] = re.sub(r"\w+, \w+ \(MiMorelia.com\).-", "", result["text"])

    result["subtitle"] = html.find(
        "div", attrs={"data-test-id": "subheadline"}
    ).text.strip()

    return result


def parse_primeraplana(content: str) -> dict:
    """Parse an article from "primeraplana" """

    soup = BeautifulSoup(content, "lxml")

    html = soup.find("article")

    result = {}

    result["outlet"] = "primeraplana"

    result["category"] = [
        html.find("li", "entry-category").text.strip()
    ]

    result["title"] = html.find("h1", "entry-title").text.strip()

    result["keywords"] = list(html.find("ul", "td-tags").li)[1:]

    result["authors"] = [html.find("div", "td-author-by").text.replace("Por", "").strip()]

    date_str = html.find("meta", attrs={"itemprop": "datePublished"})["content"].strip()
    result["published"] = datetime.fromisoformat(date_str).isoformat(timespec="minutes")

    result["text"] = "\n".join(
        p.text.strip().replace("\n", " ")
        for p in html.find("div", "td-post-content").find_all("p")[1:]
    ).strip()

    result["subtitle"] = list(html.find("div", "td-post-content").find_all("p"))[1].text.strip()

    return result
