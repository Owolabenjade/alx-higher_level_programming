#!/usr/bin/python3
"""Module containing the definition of the Square class."""


class Square:
    """Class representing a square.

    Attributes:
        __size (int): Private instance attribute representing the size of the square.

    """
    def __init__(self, size):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square.

        """
        self.__size = size
