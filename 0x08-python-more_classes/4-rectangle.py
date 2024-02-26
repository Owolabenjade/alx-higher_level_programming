#!/usr/bin/python3
"""
Module 4-rectangle
Defines a Rectangle class with private attributes width and height,
and methods for calculating area, perimeter, printing, and repr.
"""

class Rectangle:
    """Rectangle class with width, height, area, perimeter, print, and repr methods"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width, checks for integer type and value >= 0"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height, checks for integer type and value >= 0"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle, or 0 if width or height is 0"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the printable representation of the Rectangle, using '#'"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_rows = []
        for _ in range(self.__height):
            row = '#' * self.__width
            rect_rows.append(row)
        return '\n'.join(rect_rows)

    def __repr__(self):
        """Return the string representation of the Rectangle instance.
        This enables recreation of a new instance with the same attributes."""
        return f"Rectangle({self.__width}, {self.__height})"
