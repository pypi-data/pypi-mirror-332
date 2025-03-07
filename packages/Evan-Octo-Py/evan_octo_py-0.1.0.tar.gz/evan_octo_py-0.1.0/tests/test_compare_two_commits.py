import unittest
from unittest.mock import patch
import sys
import os

# Add the project directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from api.compare_two_commits import compare_commits

class TestCompareCommits(unittest.TestCase):
    def setUp(self):
        self.token = os.getenv('GITHUB_TOKEN')
        self.owner = os.getenv('GITHUB_ORG')
        self.repo = os.getenv('GITHUB_REPO', 'test_repo')
        self.base_commit = "base_commit"
        self.head_commit = "head_commit"

    @patch('api.compare_two_commits.requests.get')
    def test_compare_commits_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"files": "changed_files"}
        response = compare_commits(self.token, self.owner, self.repo, self.base_commit, self.head_commit)
        self.assertEqual(response, {"files": "changed_files"})

    @patch('api.compare_two_commits.requests.get')
    def test_compare_commits_failure(self, mock_get):
        mock_get.return_value.status_code = 404
        mock_get.return_value.json.return_value = {"message": "Not Found"}
        response = compare_commits(self.token, self.owner, self.repo, self.base_commit, self.head_commit)
        self.assertEqual(response, {"error": 404, "message": {"message": "Not Found"}})

if __name__ == '__main__':
    unittest.main()
