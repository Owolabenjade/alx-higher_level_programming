#!/bin/bash
# This script sends a request to a URL and displays the size of the body of the response
curl -s "$1" -o response_body.tmp -w '%{size_download}\n'

