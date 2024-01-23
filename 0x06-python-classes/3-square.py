#!/usr/bin/python3
"""Module containing the definition of the Square class."""


class Square:
    """Class representing a square.

    Attributes:
        __size (int): Private instance attribute representing the size
                        of the square.
    """
    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size (int, optional): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size                                                                                              

    def area(self):
        """Compute and return the area of the square."""
        return self.__size ** 2
