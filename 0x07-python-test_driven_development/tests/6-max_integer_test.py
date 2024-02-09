import unittest
from .your_module import max_integer  # Use a relative import

class TestMaxIntegerFunction(unittest.TestCase):

    def test_regular_list(self):
        result = max_integer([1, 2, 3, 4, 5])
        self.assertEqual(result, 5)

    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_all_negative_numbers(self):
        result = max_integer([-1, -2, -3, -4, -5])
        self.assertEqual(result, -1)

    def test_mixed_positive_and_negative_numbers(self):
        result = max_integer([-1, 2, -3, 4, -5])
        self.assertEqual(result, 4)

    def test_all_positive_numbers(self):
        result = max_integer([1, 2, 3, 4, 5])
        self.assertEqual(result, 5)

    def test_float_numbers(self):
        result = max_integer([1.5, 2.5, 3.5, 4.5])
        self.assertEqual(result, 4.5)

    def test_mixed_integer_and_float_numbers(self):
        result = max_integer([1, 2, 3.5, 4, 5])
        self.assertEqual(result, 5)

    def test_strings_in_list(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, 'three', 4, 5])

if __name__ == '__main__':
    unittest.main()
