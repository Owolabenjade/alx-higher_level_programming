#!/usr/bin/python3
"""
Fetches the status from https://alx-intranet.hbtn.io/status using the requests package.
This script demonstrates fetching web content simply and displaying it in a formatted manner.
"""

import requests

if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status')
    content = response.text
    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")

