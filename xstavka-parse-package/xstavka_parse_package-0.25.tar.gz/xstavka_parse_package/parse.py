import json
import os.path
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait


def get_html(url_, file_name, reload=True):
    if reload or not os.path.exists(os.path.join('html', file_name + '.html')):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(url_)
        try:
            WebDriverWait(driver, 10)
            with open(os.path.join('html', file_name + '.html'), 'w', encoding='utf-8') as f:
                f.write(driver.page_source)
        finally:
            driver.quit()


def parse_html(file_name):
    with open(os.path.join('html', file_name + '.html'), encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'lxml')
        data = []

        for item in soup.find_all('div', attrs={'data-name': 'dashboard-champ-content'}):
            data.append(parse_item(item))
    save_json(file_name, data)
    return data


def save_json(file_name, data):
    with open(os.path.join('json', file_name + '.json'), 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, indent=4, ensure_ascii=False))


def parse_item(item):
    data = {
        'head': [item.find('a', class_='c-events__liga').text.strip(),
                 *[i.text for i in item.find_all('span', class_='c-bets__title')]
                 ],
        'event': []
    }
    for event_game in item.find_all('div', class_='c-events__item c-events__item_game'):
        event = {
            'time': event_game.find('div', class_='c-events__time min').text.strip(),
            'teams': list(map(lambda x: x.text.strip(), event_game.find_all('span', class_='c-events__team'))),
            'data': list(map(lambda x: x.text, event_game.find_all('span', class_='c-bets__bet')))

        }

        data['event'].append(event)
    return data


def parse_list(url_list, reload=False):
    for item in url_list:
        file_name = item.rsplit('/', 2)[-2]
        get_html(item, file_name, reload)
        parse_html(file_name)


def foo():
    return 100
