import pandas as pd
import re


class JobTransform:

    def __init__(self, df_extracted: pd.DataFrame):
        self.df_extracted = df_extracted

    def _process_data(self):
        df = self.df_extracted

        price = df["price"].str.replace("R$", "").str.replace(".", "").str.replace(",", "")
        # price = df["price"].str.replace(re.compile("[R$,.]", re.UNICODE), "")
        df["price"] = price

        return df

    def run_tasks(self):
        return self._process_data()
