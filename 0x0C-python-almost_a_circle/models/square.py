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

    def update(self, *args, **kwargs):
        """Method documentation: update"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, val in enumerate(args):
                setattr(self, attrs[i], val)
        elif kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """Method documentation: to_dictionary"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
