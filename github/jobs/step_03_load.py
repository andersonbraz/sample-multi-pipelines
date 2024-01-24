import pandas as pd
from utils.report_client import GenReport


class JobLoad:

    def __init__(self, df_trasform: pd.DataFrame):
        self.df_trasform = df_trasform

    def run_tasks(self) -> pd.DataFrame:
        data = self.df_trasform
        df = pd.DataFrame(data)

        reports = GenReport(df_obt=df)
        reports.generate()

        df.to_csv('files/repos.csv', encoding='utf-8', sep=";", index=False)
        return df
