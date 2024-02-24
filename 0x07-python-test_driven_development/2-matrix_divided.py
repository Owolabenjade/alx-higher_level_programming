#!/usr/bin/python3
"""
This module defines a function matrix_divided that divides each element of a matrix.
The function ensures that the matrix is a list of lists of integers or floats, each row has the same size, and div is a non-zero number.
"""

def matrix_divided(matrix, div):
"""
Divides all elements of a matrix by a divisor, rounding to 2 decimal places.

Args:
matrix: A list of lists of integers or floats.
div: A non-zero integer or float.

Returns:
A new matrix with all elements divided by div and rounded to 2 decimal places.

Raises:
TypeError: If the matrix is not a list of lists of integers/floats, or
		   if each row of the matrix does not have the same size, or
		   if div is not a number.
ZeroDivisionError: If div is zero.
"""
if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) or not all(all(isinstance(el, (int, float)) for el in row) for row in matrix):
	raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
if any(len(row) != len(matrix[0]) for row in matrix):
	raise TypeError("Each row of the matrix must have the same size")
if not isinstance(div, (int, float)):
	raise TypeError("div must be a number")
if div == 0:
	raise ZeroDivisionError("division by zero")
return [[round(el / div, 2) for el in row] for row in matrix]
