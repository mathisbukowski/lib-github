"""
Function: getUserInfo
Method: GET
Utility: Get all data with a provided user. Return in JSON
"""

import requests

GITHUB_API_LINK = "https://api.github.com/"


def getUserInfo(user):
    url = f"{GITHUB_API_LINK}/users/{user}"
    response = requests.get(url)
    if response.status_code == 200:
        content = response.json()
        return content
    else:
        print("Error: Invalid data provided.")
        return []
