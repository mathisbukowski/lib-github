"""
Function: createPullRequest
Method: POST
Utility: create a pull request
"""
import json

import requests

GITHUB_API_LINK = "https://api.github.com"


class PullRequest:
    def __init__(self, token, repo):
        self.repo_name = repo
        self.bearer = token
        self.headers = {
            'Authorization': f'token {self.bearer}',
            'Accept': 'application/vnd.github.v3+json'
        }

    def createPullRequest(self, title, body, base, branchToBeMerged):
        url = f"{GITHUB_API_LINK}/repos/{self.repo_name}/pulls"
        request = {'title': title, 'body': body, 'head': branchToBeMerged, 'base': base}
        response = requests.post(url, headers=self.headers, json=request)
        if response.status_code == 201:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.json().get('message', 'Invalid Data Provided.')}")
            return response.json()

    def getPullRequestByNumber(self, pull_number):
        url = f"{GITHUB_API_LINK}/repos/{self.repo_name}/pulls/{pull_number}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.json().get('message', 'Invalid Data Provided.')}")
            return response.json()

    def getAllPullRequests(self):
        url = f"{GITHUB_API_LINK}/repos/{self.repo_name}/pulls"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.json().get('message', 'Invalid Data Provided.')}")
            return response.json()

    def updatePullRequest(self, pull_number, title, body, state, base, maintainer_can_modify):
        url = f"{GITHUB_API_LINK}/repos/{self.repo_name}/pulls/{pull_number}"
        request = {'title': title, 'body': body, 'state': state, 'base': base, 'maintainer_can_modify': maintainer_can_modify}
        response = requests.patch(url, headers=self.headers, json=request)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.json().get('message', 'Invalid Data Provided.')}")
            return response.json()
