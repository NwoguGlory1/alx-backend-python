#!/usr/bin/env python3
""" Test """
import unittest
from parameterized import parameterized
from utils import access_nested_map
""" import the necessary modules"""


class TestAccessNestedMap(unittest.TestCase):
    """ Test class for access_nested_map """
    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b':2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2),
        ])
    def TestAccessNestedMap.test_access_nested_map(self, nested_map, path):
        """ method to test """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)
