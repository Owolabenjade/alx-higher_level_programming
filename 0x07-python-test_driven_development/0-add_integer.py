#!/usr/bin/python3
"""
This module defines a function add_integer that adds two numbers.
The function ensures that the inputs are either integers or floats.
If they are floats, they are cast to integers before addition.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats.
    
    Args:
    a: The first parameter, must be an integer or float.
    b: The second parameter, must be an integer or float. Defaults to 98.
    
    Returns:
    The integer addition of a and b.
    
    Raises:
    TypeError: If either a or b is neither an integer nor a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

# Below lines are examples of how to use the function and should not be included in the script file
# print(add_integer(1, 2))
# print(add_integer(100, -2))
# print(add_integer(2))
# print(add_integer(100.3, -2))
# try:
#     print(add_integer(4, "School"))
# except Exception as e:
#     print(e)
# try:
#     print(add_integer(None))
# except Exception as e:
#     print(e)
