"""
Function: getAllRepositories
Method: GET
Utility: Get all repositories of a user provided.
"""

import requests


GITHUB_API_LINK = "https://api.github.com/"


def getAllRepositories(user):
    url = f"{GITHUB_API_LINK}/users/{user}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        repositories = response.json()
        return repositories
    else:
        print(f"Error: Invalid data provided.")
        return []
