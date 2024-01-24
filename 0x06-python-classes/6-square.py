#!/usr/bin/python3
"""Module containing the definition of the Square class."""


class Square:
        """Class representing a square.

            Attributes:
                    __size (int): Private instance attribute representing the size
                                          of the square.
                                                __position (tuple): Private instance attribute representing the
                                                                            position of the square.

                                                                                """
                                                                                    def __init__(self, size=0, position=(0, 0)):
                                                                                            """Initialize a new Square instance.

                                                                                                    Args:
                                                                                                                    size (int, optional): The size of the square (default is 0).
                                                                                                                                position (tuple, optional): The position of the square
                                                                                                                                                                        (default is (0, 0)).

                                                                                                                                                                                Raises:
                                                                                                                                                                                                TypeError: If size is not an integer or if position is not a tuple
                                                                                                                                                                                                                        of 2 positive integers.
                                                                                                                                                                                                                                    ValueError: If size is less than 0 or if position contains
                                                                                                                                                                                                                                                            non-positive integers.

                                                                                                                                                                                                                                                                    """
                                                                                                                                                                                                                                                                            self.size = size
                                                                                                                                                                                                                                                                                    self.position = position

                                                                                                                                                                                                                                                                                        @property
                                                                                                                                                                                                                                                                                            def size(self):
                                                                                                                                                                                                                                                        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The new position value.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
            ValueError: If value contains non-positive integers.

        """
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(x, int) for x in value) \
                or not all(x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Compute and return the area of the square."""
        return self.__size ** 2

                                                                                                                            def my_print(self):
        """Print the square with the character # and position."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
