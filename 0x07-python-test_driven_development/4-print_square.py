#!/usr/bin/python3
"""
Module to print a square with the character #.
"""

def print_square(size):
    """
    Prints a square with the character #.

    Parameters:
    - size (int): The size length of the square.

    Raises:
    - TypeError: If size is not an integer or if it is a float less than 0.
    - ValueError: If size is less than 0.
    """
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
