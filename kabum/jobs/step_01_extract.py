import math
import pandas as pd
import re

import utils.edge_client as nav
from bs4 import BeautifulSoup


class JobExtract:
    URL_SITE = "https://www.kabum.com.br"
    WAIT_TIME = 2

    def __init__(self, departament: str):
        self.departament = departament

    def _get_content(self):
        browser = nav.EdgeBrowser(url=f"{self.URL_SITE}/{self.departament}", wait_time=self.WAIT_TIME)
        return browser.get_html_page()

    def _get_page(self, url_page: str):
        browser = nav.EdgeBrowser(url=url_page, wait_time=self.WAIT_TIME)
        return browser.get_html_page()

    def _get_test(self):
        result = self.departament.upper()
        return result

    def _prepare_content(self) -> pd.DataFrame:
        content = self._get_content()
        soup = BeautifulSoup(str(content), "html.parser")

        div_count = soup.find('div', id='listingCount').get_text().strip()
        pos_space = div_count.find(" ")
        tot_products = int(div_count[:pos_space])
        last_page = (math.ceil(tot_products / 20)) + 1

        dict_products = {"name": [], "price": []}

        for page in range(1, last_page):
            url_page = (f"{self.URL_SITE}/{self.departament}?page_number={page}"
                        f"&page_size=20&facet_filters=&sort=most_searched")
            content = self._get_page(url_page=url_page)
            soup = BeautifulSoup(str(content), 'html.parser')
            products = soup.find_all('div', class_=re.compile('productCard'))

            for product in products:
                name = product.find("span", class_=re.compile("nameCard")).get_text().strip()
                price = product.find("span", class_=re.compile("priceCard")).get_text().strip()

                print("Conteúdo = ", f"Produto: {name} | Preço: {price} | In: {page}")

                dict_products["name"].append(name)
                dict_products["price"].append(price)

        df = pd.DataFrame(dict_products)
        return df

    def run_tasks(self) -> pd.DataFrame:
        return self._prepare_content()
