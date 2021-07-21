import requests
from bs4 import BeautifulSoup as bs
import csv


CSV = 'cards.csv'
HOST = 'https://www.mtggoldfish.com/'
URL = 'https://www.mtggoldfish.com/prices/paper/standard/'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/91.0.4472.124 Safari/537.36 '
}


def get_html(url, params=''):
    r = requests.get(url, headers= HEADERS, params=params)
    return r


def get_content(html):
    soup = bs(html, 'html.parser')
    items = soup.find_all('div', class_='priceListV2-row')
    cards = []

    for item in items:
        cards.append(
            {
                'title': item.find('span', class_='card_id card_name').find('a').get_text(strip= True),
                'price': item.find('div', class_='priceList-price-price-wrapper').get_text(strip= True),
                'link': HOST + item.find('span', class_='card_id card_name').find('a').get('href'),
            }
        )
    return cards


def save_doc(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Name', 'Price', 'Link'])
        for item in items:
            writer.writerow([item['title'],item['price'], item['link']])


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        cards = get_content(html.text)
        save_doc(cards, CSV)
        pass
    else:
        print('Error')


parser()





