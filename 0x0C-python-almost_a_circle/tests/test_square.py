#!/usr/bin/python3

import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    # Test case to ensure that area calculation is correct
    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    # Test case to ensure that perimeter calculation is correct
    def test_perimeter(self):
        s = Square(5)
        self.assertEqual(s.perimeter(), 20)

    # Test case to ensure that __str__ method returns the correct string representation
    def test_str(self):
        s = Square(5, 1, 2, 10)
        self.assertEqual(str(s), "[Square] (10) 1/2 - 5")
