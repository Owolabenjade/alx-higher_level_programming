#!/usr/bin/python3
"""
Module for lookup function.
"""


def lookup(obj):
"""
Returns the list of available attributes and methods of an object.

Args:
	obj: An object.

Returns:
	List of attributes and methods.

Example:
>>> class MyClass:
...     def __init__(self):
...         self.name = "example"
...     def display(self):
...         return "Hello, " + self.name
>>> obj = MyClass()
>>> lookup(obj)
['__init__', 'display', 'name']
"""
return [attr for attr in obj.__dir__() if not callable(getattr(obj, attr)) or attr.startswith('__')]


if __name__ == "__main__":
import doctest
doctest.testmod()
