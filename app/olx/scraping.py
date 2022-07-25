import requests
requests.packages.urllib3.disable_warnings()

from typing import Generator, Text, List
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod
from .serializer import Serializer


class Scraper(ABC):

    def __init__(self) -> None:
        self._url = f"https://mg.olx.com.br/regiao-de-uberlandia-e-uberaba/triangulo-mineiro/uberlandia/imoveis/venda?sf=1"

    @abstractmethod
    def get_html(self) -> Text:
        pass

    @abstractmethod
    def get_data(self, html: Text) -> Text:
        pass


class OLX(Scraper):
    
        def get_html(self, page: int = 0) -> Text:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
            }
            if page:
                self._url = f"{self._url}&o={page}"
            resp = requests.get(f"{self._url}", headers=headers, verify=False)
            return resp.text
    
        def get_data(self, html: Text) -> Generator[dict, None, None]:
            soup = BeautifulSoup(html, 'html.parser')
            items: List[BeautifulSoup] = soup.find('ul', {'class': 'sc-1fcmfeb-1 kntIvV'}).find_all('li')
            for item in items:
                ad_div = item.find('div', {'class': 'sc-12rk7z2-3 fqDYpJ'})
                if not ad_div:
                    continue
                serializer = Serializer().bs4_serializer(ad_div)
                yield serializer
        
        def get_parsed_data(self, page: int = 0) -> Generator[dict, None, None]:
            html: Text = self.get_html(page)
            return self.get_data(html)