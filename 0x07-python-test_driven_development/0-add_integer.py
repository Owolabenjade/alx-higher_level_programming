#!/usr/bin/python3
"""
This module provides a function add_integer() that adds two numbers.
The function is designed to handle integers and floats, with floats being
converted to integers before addition. Special float values like NaN and infinity
are handled gracefully by raising appropriate errors.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats.
    After casting floats to integers, the function returns the sum.

    Parameters:
    a (int or float): The first number.
    b (int or float, optional): The second number. Defaults to 98.

    Returns:
    int: The sum of a and b after casting to integers.

    Raises:
    TypeError: If either a or b is not an integer or float.
    ValueError: If either a or b is NaN or an infinite number.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float) and (math.isnan(a) or math.isinf(a)):
        raise ValueError("a cannot be NaN or an infinite number")
    if isinstance(b, float) and (math.isnan(b) or math.isinf(b)):
        raise ValueError("b cannot be NaN or an infinite number")
    return int(a) + int(b)
