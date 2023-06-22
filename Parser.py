import requests
from bs4 import BeautifulSoup as bs


class Parser:
    def __init__(self, url):
        self.url = url
        self.result = {}

    def get_data_from_url(self):
        self.html = requests.get(self.url).text

    def parse_data(self):
        parsed = bs(self.html, "html.parser")
        product_name = parsed.find_all('h5', class_='s-product-header')
        product_price = parsed.find_all(class_='s-price')
        product_link = parsed.find_all('h5', class_='s-product-header')
        for n in range(len(product_name)):
            product_name[n] = product_name[n].text
        for n in range(len(product_price)):
            product_price[n] = product_price[n].text
        for n in range(len(product_link)):
            product_link[n] = product_link[n].a['href']
        self.result = dict(zip(product_name, zip(product_price, product_link)))

    def print_result(self):
        for key, value in self.result.items():
            element1 = key
            element2, element3 = value
            print(f'Name: "{element1}", Price: "{element2}", Link: {url}{element3}')


# using
url = 'http://sklad-7.ru'
parser = Parser(url)
parser.get_data_from_url()
parser.parse_data()
parser.print_result()