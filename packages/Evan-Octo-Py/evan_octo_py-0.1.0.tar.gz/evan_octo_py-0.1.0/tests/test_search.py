import unittest
from unittest.mock import patch
import sys
import os

# Add the project directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from api.search import Search

class TestSearch(unittest.TestCase):
    def setUp(self):
        self.token = os.getenv('GITHUB_TOKEN')
        self.search = Search(self.token)

    @patch('api.search.requests.get')
    def test_search_repositories(self, mock_get):
        mock_get.return_value.json.return_value = {"items": "repo_results"}
        response = self.search.search_repositories("test_query")
        self.assertEqual(response, {"items": "repo_results"})

    @patch('api.search.requests.get')
    def test_search_code(self, mock_get):
        mock_get.return_value.json.return_value = {"items": "code_results"}
        response = self.search.search_code("test_query")
        self.assertEqual(response, {"items": "code_results"})

    @patch('api.search.requests.get')
    def test_search_issues(self, mock_get):
        mock_get.return_value.json.return_value = {"items": "issue_results"}
        response = self.search.search_issues("test_query")
        self.assertEqual(response, {"items": "issue_results"})

    @patch('api.search.requests.get')
    def test_search_commits(self, mock_get):
        mock_get.return_value.json.return_value = {"items": "commit_results"}
        response = self.search.search_commits("test_query")
        self.assertEqual(response, {"items": "commit_results"})

    @patch('api.search.requests.get')
    def test_search_users(self, mock_get):
        mock_get.return_value.json.return_value = {"items": "user_results"}
        response = self.search.search_users("test_query")
        self.assertEqual(response, {"items": "user_results"})

if __name__ == '__main__':
    unittest.main()
