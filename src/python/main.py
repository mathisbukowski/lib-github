#!/usr/bin/python3

import requests


GITHUB_API_LINK = "https://api.github.com"


def getCommit(repo_name) -> object:
    url = f"{GITHUB_API_LINK}/repos/{repo_name}/commits"
    response = requests.get(url, headers={})
    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.json().get('message', 'Invalid Data Provided.')}")
        return 84
    return response.json()

def getLastCommits():
    url = f"{GITHUB_API_LINK}/users/repos"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.json().get('message', 'Invalid Data Provided.')}")
        return 84

    content = response.json()
    numberOfRepos = len(content)

    for i in range(numberOfRepos):
        repo_name = content[i].get('name')
        if not repo_name:
            continue
        commit_request = getCommit(repo_name)
        print(commit_request)
        print("\n")

if __name__ == '__main__':
    getLastCommits()
