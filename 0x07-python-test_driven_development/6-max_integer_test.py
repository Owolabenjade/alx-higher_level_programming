#!/usr/bin/python3
import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    """
    TestMaxInteger class contains test cases for the max_integer function.
    
    It tests various scenarios to ensure the max_integer function behaves as expected
    across a range of inputs, including regular lists of integers, lists with negative
    numbers, empty lists, lists with a single element, and more.
    """
    
    def test_regular_list(self):
        """Test a list of integers to find the maximum correctly."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4, "Should be 4")

    def test_empty_list(self):
        """Test an empty list returns None."""
        self.assertIsNone(max_integer([]), "Should return None for empty list")

    def test_one_element(self):
        """Test a list with one element returns that element."""
        self.assertEqual(max_integer([100]), 100, "Should return the element itself")

    def test_negative_numbers(self):
        """Test a list with all negative numbers to find the maximum."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1, "Should return the highest negative number")

    def test_identical_numbers(self):
        """Test a list with all identical numbers returns that number."""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7, "Should return the number itself")

    def test_none_input(self):
        """Test that passing None as input raises a TypeError."""
        with self.assertRaises(TypeError):
            max_integer(None)

    # You can add more test methods as needed to cover other cases.

if __name__ == '__main__':
    unittest.main()
