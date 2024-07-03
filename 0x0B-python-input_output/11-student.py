#!/usr/bin/python3
"""Module 11-student.py
This module contains a class Student that defines a student by:
- first_name
- last_name
- age
Includes methods to retrieve a dictionary representation of the Student instance and to replace all attributes of the Student instance.
"""


class Student:
    """Defines a Student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance.
        
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.
        
        If attrs is a list of strings, only attributes contained in this list are retrieved.
        Otherwise, all attributes are retrieved.
        
        Args:
            attrs (list): A list of strings representing the names of the attributes to retrieve.
        
        Returns:
            The dictionary representation of the instance.
        """
        if isinstance(attrs, list) and all(isinstance(item, str) for item in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance.
        
        Args:
            json (dict): A dictionary where keys are attribute names and values are the attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
