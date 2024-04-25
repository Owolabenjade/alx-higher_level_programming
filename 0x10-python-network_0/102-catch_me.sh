#!/bin/bash
# This script makes a specific request that triggers a custom server response
curl -sLX PUT "0.0.0.0:5000/catch_me" -H "Origin: HolbertonSchool" -d "user_id=98"

