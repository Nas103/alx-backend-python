#!/usr/bin/env python3
"""
Integration tests for GithubOrgClient
"""


import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient"""

    @parameterized.expand([
        ("google", [{"name": "repo1"}, {"name": "repo2"}]),
        ("abc", [{"name": "repo3"}, {"name": "repo4"}])
    ])
    @patch('client.requests.get')
    def test_public_repos(self, org_name, expected_repos, mock_get):
        """Test public_repos method"""
        mock_get.return_value.json.return_value = expected_repos

        client = GithubOrgClient(org_name)
        self.assertEqual(client.public_repos(), [repo['name'] for repo in expected_repos])
        mock_get.assert_called_once_with(f"https://api.github.com/orgs/{org_name}/repos")

    @parameterized.expand([
        ("google", "apache-2.0", [{"name": "repo1", "license": {"key": "apache-2.0"}}, {"name": "repo2", "license": {"key": "mit"}}], ["repo1"]),
        ("abc", "mit", [{"name": "repo3", "license": {"key": "mit"}}, {"name": "repo4", "license": {"key": "apache-2.0"}}], ["repo3"])
    ])
    @patch('client.requests.get')
    def test_public_repos_with_license(self, org_name, license, repos, expected_repos, mock_get):
        """Test public_repos method with license filter"""
        mock_get.return_value.json.return_value = repos

        client = GithubOrgClient(org_name)
        self.assertEqual(client.public_repos(license=license), expected_repos)
        mock_get.assert_called_once_with(f"https://api.github.com/orgs/{org_name}/repos")


if __name__ == "__main__":
    unittest.main()
