"""
Function: getUserById
Method: GET
Utility: Get a user by his ID
"""

import requests

GITHUB_API_LINK = "https://api.github.com/"


def getUserById(id):
    url = f"{GITHUB_API_LINK}/user/{id}"
    response = requests.get(url)
    if response.status_code == 200:
        content = response.json()
        return content
    else:
        print("Error: Invalid data provided.")
        return []
