#!/usr/bin/python3
"""
Module 7-rectangle

Defines a Rectangle class with private instance attributes width and height,
a class attribute number_of_instances, a class attribute print_symbol,
and methods for area, perimeter, string representation, and deletion handling.
"""

class Rectangle:
    """Represent a rectangle.

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (Any): Symbol used for string representation.

    Args:
        width (int): The width of the rectangle (default: 0).
        height (int): The height of the rectangle (default: 0).

    Raises:
        TypeError: If width or height is not an integer.
        ValueError: If width or height is less than 0.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get or set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get or set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the Rectangle.

        Returns 0 if either the width or the height is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Uses the `print_symbol` for representation. Returns an empty string
        if width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return ""
        
        rows = []
        for i in range(self.height):
            rows.append(str(self.print_symbol) * self.width)
        return "\n".join(rows)

    def __repr__(self):
        """Return the string representation of the Rectangle.

        This string is a valid Python expression that can recreate
        the Rectangle instance.
        """
        return "Rectangle({0}, {1})".format(self.width, self.height)

    def __del__(self):
        """Print a message for every deletion of a Rectangle instance."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
