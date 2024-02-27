#!/usr/bin/python3
import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Defines test cases for the max_integer function.
    This class tests various lists to ensure correct maximum integer identification.
    """
    
    def test_sorted_list(self):
        """Test with a list of sorted integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    
    def test_unsorted_list(self):
        """Test with a list of unsorted integers."""
        self.assertEqual(max_integer([4, 1, 3, 2]), 4)
    
    def test_with_negative(self):
        """Test a list containing negative values."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
    
    def test_single_element(self):
        """Test a single-element list."""
        self.assertEqual(max_integer([7]), 7)
    
    def test_empty_list(self):
        """Test an empty list."""
        self.assertIsNone(max_integer([]))
    
    def test_same_elements(self):
        """Test a list where all elements are the same."""
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)
    
    # You can add more tests to cover other cases, such as lists with strings (which should raise an error).

if __name__ == '__main__':
    unittest.main()
