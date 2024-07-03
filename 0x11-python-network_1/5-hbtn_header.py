#!/usr/bin/python3
"""
Sends a request to a given URL and displays the value of the X-Request-Id variable from the response header.
This script uses requests and sys to handle HTTP requests and command line arguments, respectively.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    # Retrieve the value of the X-Request-Id header using the .get method which safely returns None if the key doesn't exist
    request_id = response.headers.get('X-Request-Id')
    if request_id:
        print(request_id)

