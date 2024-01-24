import pandas as pd
from datetime import datetime


class JobTransform:

    def __init__(self, df_extracted: pd.DataFrame):
        self.df_extracted = df_extracted

    def run_tasks(self) -> pd.DataFrame:
        df = self.df_extracted

        organization = df["full_name"].str.split("/", n=1).str[0]

        df["created_at"] = pd.to_datetime(df["created_at"])
        df["updated_at"] = pd.to_datetime(df["updated_at"])
        df["organization"] = organization.str.upper()

        df = df.drop(["full_name"], axis=1)
        df.columns = df.columns.str.upper()

        return df
