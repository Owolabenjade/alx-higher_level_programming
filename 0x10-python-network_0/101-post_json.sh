#!/bin/bash
# This script sends a JSON POST request with the contents of a file
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"

