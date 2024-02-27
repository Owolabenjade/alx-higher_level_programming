#!/usr/bin/python3
"""
This module defines a function say_my_name that prints "My name is <first name> <last name>".
It validates that both first_name and last_name are strings.
"""

def say_my_name(first_name, last_name=""):
    """Prints "My name is <first name> <last name>".
    Args:
        first_name (str): The first name.
        last_name (str): The last name, optional.
    Raises:
        TypeError: If either first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
