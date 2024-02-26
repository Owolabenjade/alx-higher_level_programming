#!/usr/bin/python3
import json

def load_from_json_file(filename):
    """
    Reads from a JSON file and creates an object represented by the JSON file.

    Args:
        filename (str): The name of the JSON file to be read.

    Returns:
        object: The Python object represented by the JSON file content.
    """
    with open(filename, "r") as f:
        return json.load(f)
