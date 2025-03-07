import unittest
from unittest.mock import patch
import sys
import os

# Add the project directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from api.rulesets import Rulesets

class TestRuleset(unittest.TestCase):
    def setUp(self):
        self.token = os.getenv('GITHUB_TOKEN')
        self.org = os.getenv('GITHUB_ORG')
        self.repo = os.getenv('GITHUB_REPO', 'test_repo')
        self.ruleset = Rulesets(self.token, self.org, self.repo)

    @patch('api.rulesets.requests.get')
    def test_list_org_rulesets(self, mock_get):
        mock_get.return_value.json.return_value = {"rulesets": "org_rulesets"}
        response = self.ruleset.list_org_rulesets()
        self.assertEqual(response, {"rulesets": "org_rulesets"})

    @patch('api.rulesets.requests.get')
    def test_get_org_ruleset(self, mock_get):
        mock_get.return_value.json.return_value = {"ruleset": "org_ruleset"}
        response = self.ruleset.get_org_ruleset(1)
        self.assertEqual(response, {"ruleset": "org_ruleset"})

    @patch('api.rulesets.requests.post')
    def test_create_org_ruleset(self, mock_post):
        mock_post.return_value.json.return_value = {"result": "org_ruleset_created"}
        response = self.ruleset.create_org_ruleset({"name": "test_ruleset"})
        self.assertEqual(response, {"result": "org_ruleset_created"})

    @patch('api.rulesets.requests.put')
    def test_update_org_ruleset(self, mock_put):
        mock_put.return_value.json.return_value = {"result": "org_ruleset_updated"}
        response = self.ruleset.update_org_ruleset(1, {"name": "updated_ruleset"})
        self.assertEqual(response, {"result": "org_ruleset_updated"})

    @patch('api.rulesets.requests.delete')
    def test_delete_org_ruleset(self, mock_delete):
        mock_delete.return_value.json.return_value = {"result": "org_ruleset_deleted"}
        response = self.ruleset.delete_org_ruleset(1)
        self.assertEqual(response, {"result": "org_ruleset_deleted"})

    @patch('api.rulesets.requests.get')
    def test_list_repo_rulesets(self, mock_get):
        mock_get.return_value.json.return_value = {"rulesets": "repo_rulesets"}
        response = self.ruleset.list_repo_rulesets()
        self.assertEqual(response, {"rulesets": "repo_rulesets"})

    @patch('api.rulesets.requests.get')
    def test_get_repo_ruleset(self, mock_get):
        mock_get.return_value.json.return_value = {"ruleset": "repo_ruleset"}
        response = self.ruleset.get_repo_ruleset(1)
        self.assertEqual(response, {"ruleset": "repo_ruleset"})

    @patch('api.rulesets.requests.post')
    def test_create_repo_ruleset(self, mock_post):
        mock_post.return_value.json.return_value = {"result": "repo_ruleset_created"}
        response = self.ruleset.create_repo_ruleset({"name": "test_ruleset"})
        self.assertEqual(response, {"result": "repo_ruleset_created"})

    @patch('api.rulesets.requests.put')
    def test_update_repo_ruleset(self, mock_put):
        mock_put.return_value.json.return_value = {"result": "repo_ruleset_updated"}
        response = self.ruleset.update_repo_ruleset(1, {"name": "updated_ruleset"})
        self.assertEqual(response, {"result": "repo_ruleset_updated"})

    @patch('api.rulesets.requests.delete')
    def test_delete_repo_ruleset(self, mock_delete):
        mock_delete.return_value.json.return_value = {"result": "repo_ruleset_deleted"}
        response = self.ruleset.delete_repo_ruleset(1)
        self.assertEqual(response, {"result": "repo_ruleset_deleted"})

if __name__ == '__main__':
    unittest.main()
