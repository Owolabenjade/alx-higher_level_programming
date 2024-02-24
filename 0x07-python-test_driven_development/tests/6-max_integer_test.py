# File: tests/6-max_integer_test.py

import unittest
from my_module import max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Unit tests for the max_integer function.
    """

    def test_positive_numbers(self):
        """
        Test max_integer with positive numbers.
        """
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([10, 20, 30]), 30)
        self.assertEqual(max_integer([5, 8, 2]), 8)

    def test_negative_numbers(self):
        """
        Test max_integer with negative numbers.
        """
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([-10, -20, -30]), -10)
        self.assertEqual(max_integer([-5, -8, -2]), -2)

    def test_mixed_numbers(self):
        """
        Test max_integer with mixed positive and negative numbers.
        """
        self.assertEqual(max_integer([1, -2, 3]), 3)
        self.assertEqual(max_integer([-10, 20, -30]), 20)
        self.assertEqual(max_integer([5, -8, 2]), 5)

    def test_empty_list(self):
        """
        Test max_integer with an empty list.
        """
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        """
        Test max_integer with a single-element list.
        """
        self.assertEqual(max_integer([42]), 42)

    def test_invalid_input(self):
        """
        Test max_integer with invalid input types.
        """
        with self.assertRaises(TypeError):
            max_integer("not_a_list")
        with self.assertRaises(TypeError):
            max_integer([1, 2, "string"])
        with self.assertRaises(TypeError):
            max_integer([1, 2, None])

if __name__ == '__main__':
    unittest.main()
