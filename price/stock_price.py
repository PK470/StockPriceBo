from bs4 import BeautifulSoup
import requests
import time


class StockPrice:

    
    _class1 = "YMlKec fxKbKc"
    def get_price(self, name):

        response = requests.get(f'https://www.google.com/finance/quote/{name}:NSE')
        soup = BeautifulSoup(response.text, 'html.parser')
        #print(soup)
        return soup.find(class_ = self._class1).text.strip()[1:]
