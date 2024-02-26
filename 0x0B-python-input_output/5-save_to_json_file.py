#!/usr/bin/python3
"""Module to save an object in JSON format to a file.

This module provides a function save_to_json_file which serializes
an object to a JSON formatted string and writes it to a file.
"""

import json

def save_to_json_file(my_obj, filename):
    """Serializes an object to JSON and writes it to a file.

    Args:
        my_obj: The object to serialize.
        filename: The name of the file to write the JSON string to.
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
