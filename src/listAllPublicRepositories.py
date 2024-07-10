"""
Function: listAllPublicRepositories
Method: GET
Utility: List all public repositories of a user
"""

import requests

GITHUB_API_LINK = "https://api.github.com"


def listAllPublicRepositories(user):
    url = f"{GITHUB_API_LINK}/users/{user}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        repositories = response.json()
        return repositories
    else:
        print(f"Error: Invalid data provided.")
        return []
