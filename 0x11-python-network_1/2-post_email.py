#!/usr/bin/python3
"""
Sends a POST request to a given URL with an email as a parameter and displays the response.
This script uses urllib and sys to handle HTTP POST requests and command line arguments, respectively.
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')  # Data should be bytes
    req = urllib.request.Request(url, data)
    
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode('utf-8')
        print(response_body)
