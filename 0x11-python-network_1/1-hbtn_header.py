#!/usr/bin/python3
"""
Fetches the X-Request-Id from the response header of a given URL.
This script demonstrates fetching specific header information using urllib and sys in Python.
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        # Retrieve the value of the X-Request-Id header
        request_id = response.getheader('X-Request-Id')
        print(request_id)

