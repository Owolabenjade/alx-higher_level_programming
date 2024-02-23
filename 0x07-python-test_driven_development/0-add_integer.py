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
    
    # Check for NaN by comparing the number with itself
    if a != a or b != b:
        raise ValueError("Cannot convert NaN to integer")
    
    # Check for infinity by comparing with a very large number
    if abs(a) == float('inf') or abs(b) == float('inf'):
        raise ValueError("Cannot convert infinity to integer")
    
    return int(a) + int(b)
