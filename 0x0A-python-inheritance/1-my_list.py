#!/usr/bin/python3
"""
Module for MyList class.
"""


class MyList(list):
	"""
	MyList class that inherits from list.

	Public instance method:
		def print_sorted(self): Prints the list, but sorted (ascending sort).

	Example:
	>>> my_list = MyList([3, 1, 4, 1, 5, 9, 2])
	>>> my_list.print_sorted()
	[1, 1, 2, 3, 4, 5, 9]
	"""

	def print_sorted(self):
		"""Prints the list, but sorted (ascending sort)."""
		print(sorted(self))


if __name__ == "__main__":
	import doctest
	doctest.testmod()
