"""
Class: Repository
Method: POST/GET/PUT/PATCH
Utility: Manage Repositories.
"""

import requests


GITHUB_API_LINK = "https://api.github.com"


class Commit:
    def __init__(self, token, repo):
        self.repo_name = repo
        self.headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json'
        }

    def getLastCommits(self):
        url = f"{GITHUB_API_LINK}/users/repos"
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            print(f"Error: {response.status_code} - {response.json().get('message', 'Invalid Data Provided.')}")
            return 84

        content = response.json()
        numberOfRepos = len(content)

        for i in range(numberOfRepos):
            print(content[i].name)
