#!/usr/bin/python3
"""Module documentation: square.py"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Class documentation: Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Method documentation: __init__"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Method documentation: size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """Method documentation: size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """Method documentation: __str__"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )
