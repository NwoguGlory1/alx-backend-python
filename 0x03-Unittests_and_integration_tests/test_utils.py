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
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ method to test access_nested_map """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ('a',), KeyError),
        ({'a': 1}, ('a', 'b'), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """ method to test if access_nested_map handles exceptions well"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
            """
            access_nested_map is called to see if exception is raised
            if it is raised, then access_nested_map is OK
            """
