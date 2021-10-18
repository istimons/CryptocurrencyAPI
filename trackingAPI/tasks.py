from time import sleep
from celery import shared_task
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

from .models import Cryptocurrency
from alpha_vantage.cryptocurrencies import CryptoCurrencies

APIKEY = 'TXP8RWA7450TYG6A'

# Create your views here.

@shared_task
def crawl_currency():
    print('Crawling data and creating objects in database ..')

    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=CNY&apikey=TXP8RWA7450TYG6A'
    r = requests.get(url)
    data = r.json()

    # All json
    # x_y = data['Realtime Currency Exchange Rate']

    bid_price = data['Realtime Currency Exchange Rate']['8. Bid Price']

    print(bid_price)
    # Sleep 3 seconds to avoid any errors
    sleep(3)


@shared_task
def update_currency():
    print('Updating data ..')

    import requests

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=CNY&apikey=TXP8RWA7450TYG6A'
    r = requests.get(url)
    data = r.json()

    # All json
    # x_y = data['Realtime Currency Exchange Rate']

    bid_price = data['Realtime Currency Exchange Rate']['8. Bid Price']

    print(bid_price)

    sleep(3)


if not Cryptocurrency.objects:
    crawl_currency()

while True:
    sleep(1)
    update_currency()




