#!/usr/bin/python3
"""
This module provides a function load_from_json_file which reads from a JSON file
and creates an object based on the JSON file's content. This utility is useful for
converting JSON-encoded data into Python objects.

Usage:
    This script is intended to be used as a utility module in Python projects where
    JSON data needs to be converted into Python objects. It abstracts the file reading
    and JSON parsing process into a single function call.

Example:
    import 6-load_from_json_file as json_loader
    my_object = json_loader.load_from_json_file('my_file.json')
"""

import json

def load_from_json_file(filename):
    """
    Reads from a JSON file and creates an object represented by the JSON file.

    This function opens a file with the given filename, reads its contents, and
    interprets it as JSON, converting the JSON data into a Python object. The function
    uses the with statement to ensure the file is properly closed after its contents
    have been read and processed.

    Args:
        filename (str): The name of the JSON file to be read.

    Returns:
        object: The Python object represented by the JSON file content.

    Note:
        This function does not handle exceptions that may arise from invalid JSON data
        or issues with file access permissions. It is assumed the JSON file is correctly
        formatted and accessible.
    """
    with open(filename, "r") as f:
        return json.load(f)
