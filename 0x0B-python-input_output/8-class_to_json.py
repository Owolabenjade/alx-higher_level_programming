#!/usr/bin/python3
def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer, boolean)
    for JSON serialization of an object.

    Args:
        obj: An instance of a Class with serializable attributes.
    """
    return obj.__dict__
