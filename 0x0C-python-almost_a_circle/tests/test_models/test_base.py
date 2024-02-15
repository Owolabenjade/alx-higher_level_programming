#!/usr/bin/python3
"""Test documentation: test_base.py"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Test class documentation: TestBase"""

    def test_init(self):
        """Test method documentation: test_init"""
        b = Base(10, 20)
        self.assertEqual(b.width, 10)
        self.assertEqual(b.height, 20)

if __name__ == '__main__':
    unittest.main()
