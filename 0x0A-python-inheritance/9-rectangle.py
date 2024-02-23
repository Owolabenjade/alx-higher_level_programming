#!/usr/bin/python3
"""
Module for Rectangle class.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
	"""
	A class for Rectangle, inherits from BaseGeometry.
	"""

	def __init__(self, width, height):
		"""
		Initializes a Rectangle instance with width and height.

		Args:
			width: Width of the rectangle.
			height: Height of the rectangle.
		"""
		self.integer_validator("width", width)
		self.integer_validator("height", height)
		self.__width = width
		self.__height = height

	def area(self):
		"""
		Calculates and returns the area of the rectangle.

		Returns:
			The area of the rectangle.
		"""
		return self.__width * self.__height

	def __str__(self):
		"""
		Returns a string representation of the Rectangle.

		Returns:
			A string representing the Rectangle.
		"""
		return "[Rectangle] {}/{}".format(self.__width, self.__height)


if __name__ == "__main__":
	r = Rectangle(3, 5)

	print(r)
	print(r.area())
