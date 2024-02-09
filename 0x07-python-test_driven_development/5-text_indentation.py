#!/usr/bin/python3
"""
Module to print text with 2 new lines after ., ? and : characters.
"""

def text_indentation(text):
    """
    Prints text with 2 new lines after ., ? and : characters.

    Parameters:
    - text (str): The input text.

    Raises:
    - TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars_to_indent = ['.', '?', ':']
    current_line = ""

    for char in text:
        current_line += char
        if char in chars_to_indent:
            print(current_line.strip())
            print()
            current_line = ""

    if current_line.strip():
        print(current_line.strip())
