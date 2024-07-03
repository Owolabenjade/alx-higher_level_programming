#!/usr/bin/python3
"""
This module defines a function add_integer that adds two numbers.
The function ensures that the inputs are either integers or floats,
and returns their sum as an integer.
"""


def add_integer(a, b=98):
    """Add two integers.
    Args:
        a: The first parameter, must be an integer or float.
        b: The second parameter, must be an integer or float (defaults to 98).
    Returns:
        The integer addition of a and b.
    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
