import pandas as pd


class JobExtract:

    def __init__(self, lista_urls: list):
        self.lista_urls = lista_urls

    def _download_files(self):
        files = self.lista_urls
        for file in files:
            print(file)

    def run_tasks(self):
        self._download_files()
