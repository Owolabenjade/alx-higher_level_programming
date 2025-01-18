#!/usr/bin/python3
"""
Fetches content from a given URL and handles HTTP errors gracefully.
This script demonstrates error handling with urllib and sys, specifically managing HTTP errors.
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            response_body = response.read().decode('utf-8')
            print(response_body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
