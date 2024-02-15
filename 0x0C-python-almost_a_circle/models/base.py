#!/usr/bin/python3
"""Module documentation: base.py"""

class Base:
    """Class documentation: Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Method documentation: __init__"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
