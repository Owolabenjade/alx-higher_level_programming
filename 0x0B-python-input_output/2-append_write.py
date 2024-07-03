#!/usr/bin/python3
"""
This module defines the append_write function that appends a string at the end
of a text file and returns the number of characters added. If the file doesn’t
exist, it will be created. It uses a with statement for safe file handling.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file and returns the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
