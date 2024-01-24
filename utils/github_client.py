import requests
import os


class GitHubRepos:
    URL_API = "https://api.github.com"

    def __init__(self, organization: str, per_page: int, page: int):
        self.organization = organization
        self.per_page = per_page
        self.page = page
        self.token = os.environ["GITHUB_TOKEN"]

    def _get_auth_header(self):
        header = {
            "Authorization": "Bearer " + self.token,
            "X-GitHub-Api-Version": "2022-11-28",
        }
        return header

    def get_repos(self):
        """
        Faz uma chamada no endpoint https://api.github.com/orgs/microsoft/repos
        """
        url = f"{self.URL_API}/orgs/{self.organization}/repos?per_page={self.per_page}&page={self.page}"
        response = requests.get(url, headers=self._get_auth_header())

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"{response.raise_for_status()}")
