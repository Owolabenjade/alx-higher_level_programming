#!/usr/bin/python3
"""
Fetches the last 10 commits of a given repository and owner from GitHub using the GitHub API.
Prints the SHA and the author name of each commit.
Utilizes requests for HTTP requests and sys to handle command line arguments.
"""

import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'
    params = {'per_page': 10}

    response = requests.get(url, params=params)
    commits = response.json()

    for commit in commits:
        sha = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author}")
