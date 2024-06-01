#!/usr/bin/env python3
""" Test """
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient"""

    @parameterized.expand([
        ('google',),
        ('abc',),
    ])
    @patch('client.get_json')
    def test_org(self, input, mock_get_json):
        """Method to test that GithubOrgClient.org returns the correct value"""
        
        # Define the mock return value
        mock_response = {"login": input}
        mock_get_json.return_value = mock_response

        # Instantiate the GithubOrgClient with the test organization
        test_class = GithubOrgClient(input)

        # Call the org method
        result = test_class.org()

        # Verify that get_json was called once with the expected URL
        expected_url = f"https://api.github.com/orgs/{input}"
        mock_get_json.assert_called_once_with(expected_url)

        # Verify the result of the org method
        self.assertEqual(result, mock_response)

if __name__ == '__main__':
    unittest.main()
