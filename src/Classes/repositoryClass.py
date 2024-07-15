"""
Class: Repository
Method: POST/GET/PUT/PATCH
Utility: Manage Repositories.
"""

import requests


GITHUB_API_LINK = "https://api.github.com"


class Repository:
    def __init__(self, token, repo):
        self.repo_name = repo
        self.headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json'
        }

    def getRepository(self):
        url = f"{GITHUB_API_LINK}/repos/{self.repo_name}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.json().get('message', 'Invalid Data Provided.')}")
            return response.json()

    def listAllPublicRepositories(self):
        url = f"{GITHUB_API_LINK}/users/repos"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.json().get('message', 'Invalid Data Provided.')}")
            return response.json()

    def updateRepository(self, state, name, description, homepage):
        url = f"{GITHUB_API_LINK}/repos/{self.repo_name}"
        request = {'state': state, 'name': name, 'description': description, 'homepage': homepage}
        response = requests.patch(url, headers=self.headers, json=request)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.json().get('message', 'Invalid Data Provided.')}")
            return response.json()

    def deleteRepository(self):
        url = f"{GITHUB_API_LINK}/repos/{self.repo_name}"
        response = requests.delete(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.json().get('message', 'Invalid Data Provided.')}")
            return response.json()
