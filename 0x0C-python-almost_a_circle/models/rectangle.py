#!/usr/bin/python3
"""Module documentation: rectangle.py"""
from models.base import Base

class Rectangle(Base):
    """Class documentation: Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Method documentation: __init__"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Method documentation: width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Method documentation: width setter"""
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """Method documentation: height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Method documentation: height setter"""
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """Method documentation: x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """Method documentation: x setter"""
        self.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """Method documentation: y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """Method documentation: y setter"""
        self.integer_validator("y", value)
        self.__y = value

    def area(self):
        """Method documentation: area"""
        return self.width * self.height

    def display(self):
        """Method documentation: display"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Method documentation: __str__"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def to_dictionary(self):
        """Method documentation: to_dictionary"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
