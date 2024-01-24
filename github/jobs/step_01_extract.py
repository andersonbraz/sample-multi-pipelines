import utils.github_client as api
import pandas as pd


class JobExtract:

    MAX_PER_PAGE = 10

    def __init__(self, lista_orgs, lista_campos):
        self.lista_orgs = lista_orgs
        self.lista_campos = lista_campos

    def _listar_repos(self) -> pd.DataFrame:

        orgs = self.lista_orgs
        dfs = []

        for org in orgs:
            for item in range(0, 20):
                github = api.GitHubRepos(organization=org, per_page=self.MAX_PER_PAGE, page=item)
                repos = github.get_repos()
                df_repo = pd.DataFrame.from_dict(repos)
                df_repo = df_repo[self.lista_campos]
                dfs.append(df_repo)

        df = pd.concat(dfs, join="inner", ignore_index=True)
        return df

    def run_tasks(self) -> pd.DataFrame:

        df = self._listar_repos()
        return df
