#!/usr/bin/python3
"""
Module for is_same_class function.
"""


def is_same_class(obj, a_class):
	"""
	Returns True if the object is exactly an instance of the specified class;
	otherwise, False.

	Args:
		obj: An object.
		a_class: A class.

	Returns:
		True if obj is an instance of a_class, False otherwise.

	Example:
	>>> is_same_class(1, int)
	True
	>>> is_same_class(1, float)
	False
	>>> is_same_class(1, object)
	False
	"""
	return type(obj) is a_class


if __name__ == "__main__":
	import doctest
	doctest.testmod()
