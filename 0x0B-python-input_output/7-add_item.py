#!/usr/bin/python3
"""
A script that adds all arguments to a list and saves them to a JSON file.

This script demonstrates the use of functions to read from and write to JSON files,
handling the scenario where the JSON file may not initially exist.
"""

import sys
import json

def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using a JSON representation."""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)

def load_from_json_file(filename):
    """Creates an object from a "JSON file"."""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []  # Return an empty list if the file does not exist

if __name__ == "__main__":
    filename = "add_item.json"
    
    # Load existing items from file, or initialize an empty list if the file doesn't exist
    items = load_from_json_file(filename)
    
    # Add all command-line arguments (except the script name) to the list
    items.extend(sys.argv[1:])
    
    # Save the updated list to the file
    save_to_json_file(items, filename)
