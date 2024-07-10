"""
Function: createPr
Method: POST
Utility: create a pull request
"""

import requests

GITHUB_API_LINK = "https://api.github.com"


def createPullRequest(owner, repo, title, body, base, branchToBeMerged):
    url = f"{GITHUB_API_LINK}/repos/{owner}/{repo}/pulls"
    request = {'title': title, 'body': body, 'head': branchToBeMerged, 'base': base}
    response = requests.post(url, params=request)
    if response.status_code == 201:
        content = response.json()
        return content
    else:
        print("Error: Invalid Data Provided.")
        return []