#!/usr/bin/python3
"""Module 10-student.py
This module enhances the class Student by allowing selective retrieval of
information through the to_json method, based on a list of attribute names.
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
        
        If attrs is a list of strings, only attributes contained in this list
        will be retrieved. Otherwise, all attributes will be retrieved.
        
        Args:
            attrs (list): A list of strings representing attribute names to
                          include in the returned dictionary.
                          
        Returns:
            A dictionary representation of the Student instance.
        """
        if isinstance(attrs, list) and all(isinstance(item, str) for item in attrs):
            return {key: value for key, value in self.__dict__.items() if key in attrs}
        return self.__dict__
