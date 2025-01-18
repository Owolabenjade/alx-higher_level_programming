#!/usr/bin/python3
"""
Uses the GitHub API with Basic Authentication to fetch and display the user's GitHub ID.
Takes GitHub username and a personal access token as arguments to authenticate and access user data.
Uses requests and sys for HTTP requests and command line argument handling, respectively.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = 'https://api.github.com/user'

    response = requests.get(url, auth=(username, token))
    if response.status_code == 200:
        print(response.json().get('id'))
    else:
        print(None)
