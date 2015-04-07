"""
Test for source.source1
"""
from source.source1 import get_triangle_type
from unittest import TestCase

class TestGetTriangleType(TestCase):

    def test_get_triangle_equilateral_all_int(self):    # provided
        result = get_triangle_type(1, 1, 1)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_equilateral_tuple(self):      # added for lab 1
        tup = (2, 2, 2)
        result = get_triangle_type(tup)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_equilateral_dict(self):      # added for lab 1
        dic = {'a': 2, 'b': 2, 'c': 2}
        result = get_triangle_type(dic)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_all_int(self):        # fixed for lab 1
        result = get_triangle_type(1, 2, 3)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_isosceles_all_int(self):      # added for lab 1
        result = get_triangle_type(1, 1, 2)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_scalene_all_int(self):        # provided
        result = get_triangle_type(1, 2, 3)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_improper_type(self):          # added for lab 1
        result = get_triangle_type(1, "a", 3)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_negative_value(self):          # added for lab 1
        result = get_triangle_type(1, -1, 3)
        self.assertEqual(result, 'invalid')