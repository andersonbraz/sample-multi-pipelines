import pandas as pd


class JobLoad:

    def __init__(self, df_trasform: pd.DataFrame):
        self.df_trasform = df_trasform

    def run_tasks(self) -> pd.DataFrame:
        data = self.df_trasform
        df = pd.DataFrame(data)

        df.to_csv('files/kabum_tv.csv', encoding='utf-8', sep=";", index=False)
        return df
