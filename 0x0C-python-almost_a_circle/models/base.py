#!/usr/bin/python3
"""Module documentation: base.py"""
import json

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Method documentation: to_json_string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
