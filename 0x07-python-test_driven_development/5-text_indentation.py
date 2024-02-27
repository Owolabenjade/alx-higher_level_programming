#!/usr/bin/python3
"""
This module defines the text_indentation function that processes a given text.
It adds two new lines after each '.', '?', and ':', ensuring proper text formatting.
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.

    This function takes a string as an argument and prints it, inserting two
    new lines after each occurrence of '.', '?', or ':'. It also ensures that
    there is no unnecessary space at the beginning of the new line that follows
    these punctuation marks.

    Args:
        text (str): The text to format and print.

    Raises:
        TypeError: If `text` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            if i + 1 < len(text) and text[i + 1] == " ":
                i += 2
                continue
        i += 1
