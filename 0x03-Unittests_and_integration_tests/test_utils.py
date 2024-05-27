#!/usr/bin/env python3
""" Test """
import unittest
import requests
from parameterized import parameterized
from utils import access_nested_map
from utils import get_json
from unittest.mock import patch, Mock
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


class TestGetJson(unittest.TestCase):
    """ Test class for get_json """

    @parameterized.expand([
        ('http://example.com', {"payload": True}),
        ('http://holberton.io', {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, mock_get, test_url, test_payload):
        """ method to test that utils.get_json returns expected result"""

        # Create a Mock object to simulate the HTTP response
        mock_response = Mock()

        # Set the .json() method of the mock response to return test_payload
        mock_response.json.return_value = test_payload

        # When requests.get is called, return the mock response
        mock_get.return_value = mock_response

        # Call the function being tested with the test URL
        result = get_json(test_url)

        # Ensure requests.get was called exactly once with the provided URL
        mock_get.assert_called_once_with(test_url)

        # Verify the result of get_json matches the expected payload
        self.assertEqual(result, test_payload)
