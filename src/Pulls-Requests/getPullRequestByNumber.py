"""
Function: getPullRequestByNumber
Method: GET
Utility: drop the PullRequest by her number
"""

import requests


GITHUB_API_LINK = "https://api.github.com"


def getPullRequestByNumber(owner, repo, pull_number):
    url = f"{GITHUB_API_LINK}/repos/{owner}/{repo}/pulls/{pull_number}"
    response = requests.get(url)
    if response.status_code == 200:
        content = response.json()
        return content
    else:
        print("Error: Invalid Data Provided.")
        return None
