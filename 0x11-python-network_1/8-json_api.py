#!/usr/bin/python3
"""
Sends a POST request with a given letter as a parameter to a specified URL.
Handles and displays JSON responses: shows user ID and name if valid and non-empty,
otherwise reports errors in JSON format or lack of results.
Uses requests and sys to manage HTTP requests and command line arguments.
"""

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    response = requests.post(url, data={'q': letter})

    try:
        json_resp = response.json()
        if json_resp:
            print(f"[{json_resp.get('id')}] {json_resp.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

