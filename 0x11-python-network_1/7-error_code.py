#!/usr/bin/python3
"""
Sends a request to a given URL and handles the response.
Displays the body of the response or an error message if the HTTP status code is 400 or greater.
Uses requests and sys to manage HTTP requests and command line arguments, respectively.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
