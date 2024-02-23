#!/usr/bin/python3
"""
Module for inherits_from function.
"""


def inherits_from(obj, a_class):
	"""
	Returns True if the object is an instance of a class that inherited
	(directly or indirectly) from the specified class; otherwise, False.

	Args:
		obj: An object.
		a_class: A class.

	Returns:
		True if obj is an instance of a class inherited from a_class,
		False otherwise.

	Example:
	>>> inherits_from(True, int)
	True
	>>> inherits_from(True, bool)
	True
	>>> inherits_from(True, object)
	True
	"""
	return issubclass(type(obj), a_class) and type(obj) is not a_class


if __name__ == "__main__":
	import doctest
	doctest.testmod()
