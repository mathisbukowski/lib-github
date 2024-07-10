"""
Function: getRepository
Method: GET
Utility: Get infos of a repo with his name and the name of the owner
"""

import requests
GITHUB_API_LINK = "https://api.github.com"


def getRepository(owner, name):
    url = f"{GITHUB_API_LINK}/repos/{owner}/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        content = response.json()
        return content
    else:
        print("Error: Invalid Data Provided.")
        return []
