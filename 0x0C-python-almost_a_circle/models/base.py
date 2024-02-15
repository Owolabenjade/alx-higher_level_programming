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

    @classmethod
    def save_to_file(cls, list_objs):
        """Method documentation: save_to_file"""
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding='utf-8') as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Method documentation: from_json_string"""
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)
