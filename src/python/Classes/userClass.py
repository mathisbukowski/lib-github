"""
Class: User
Method: POST/GET/PUT/PATCH
Utility: Manage Users.
"""

import requests

GITHUB_API_LINK = "https://api.github.com/"


class User:
    def __init__(self, token, repo):
        self.repo_name = repo
        self.headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json'
        }
    def getUserById(self, id):
        url = f"{GITHUB_API_LINK}/user/{id}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.json().get('message', 'Invalid Data Provided.')}")
            return response.json()

    def getUserInfo(self, user):
        if user is not None:
            url = f"{GITHUB_API_LINK}/users/{user}"
        else:
            url = f"{GITHUB_API_LINK}/users/"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.json().get('message', 'Invalid Data Provided.')}")
            return response.json()
