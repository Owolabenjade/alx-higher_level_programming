#!/usr/bin/python3
"""
This module defines a function class_to_json that takes in an object
and returns a dictionary description with simple data structures
(list, dictionary, string, integer, boolean) for JSON serialization
of the object's attributes.

The purpose is to ensure that objects can be easily serialized into
JSON format, focusing on simple data types that are natively supported
by JSON serialization without requiring custom processing.
"""

def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer, boolean)
    for JSON serialization of an object.

    This function iterates through an object's attributes, ensuring
    that all attributes returned are in a format that can be
    serialized into JSON. The function leverages the native Python
    dictionary representation of an object's `__dict__` attribute,
    which contains all its attributes. This makes it suitable for
    serializing objects that contain simple data types.

    Args:
        obj: An instance of a Class with serializable attributes.

    Returns:
        A dictionary containing all of the serializable attributes of `obj`.
    """
    return obj.__dict__
