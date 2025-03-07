import unittest
from unittest.mock import patch
import sys
import os

# Add the project directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from api.copilot import Copilot

class TestCopilot(unittest.TestCase):
    def setUp(self):
        self.token = os.getenv('GITHUB_TOKEN')
        self.org = os.getenv('GITHUB_ORG')
        self.enterprise = os.getenv('GITHUB_ENTERPRISE')
        self.copilot = Copilot(self.token, self.org, self.enterprise)
        
    @patch('api.copilot.requests.get')
    def test_get_copilot_metrics_enterprise(self, mock_get):
        mock_get.return_value.json.return_value = {"metrics": "enterprise_metrics"}
        response = self.copilot.get_copilot_metrics_enterprise()
        self.assertEqual(response, {"metrics": "enterprise_metrics"})

    @patch('api.copilot.requests.get')
    def test_get_copilot_metrics_org(self, mock_get):
        mock_get.return_value.json.return_value = {"metrics": "org_metrics"}
        response = self.copilot.get_copilot_metrics_org()
        self.assertEqual(response, {"metrics": "org_metrics"})

    @patch('api.copilot.requests.get')
    def test_get_copilot_metrics_team(self, mock_get):
        mock_get.return_value.json.return_value = {"metrics": "team_metrics"}
        response = self.copilot.get_copilot_metrics_team("test_team")
        self.assertEqual(response, {"metrics": "team_metrics"})

    @patch('api.copilot.requests.get')
    def test_get_copilot_usage_enterprise(self, mock_get):
        mock_get.return_value.json.return_value = {"usage": "enterprise_usage"}
        response = self.copilot.get_copilot_usage_enterprise()
        self.assertEqual(response, {"usage": "enterprise_usage"})

    @patch('api.copilot.requests.get')
    def test_get_copilot_usage_org(self, mock_get):
        mock_get.return_value.json.return_value = {"usage": "org_usage"}
        response = self.copilot.get_copilot_usage_org()
        self.assertEqual(response, {"usage": "org_usage"})

    @patch('api.copilot.requests.get')
    def test_get_copilot_usage_team(self, mock_get):
        mock_get.return_value.json.return_value = {"usage": "team_usage"}
        response = self.copilot.get_copilot_usage_team("test_team")
        self.assertEqual(response, {"usage": "team_usage"})

    @patch('api.copilot.requests.get')
    def test_list_copilot_seats_org(self, mock_get):
        mock_get.return_value.json.return_value = {"seats": "org_seats"}
        response = self.copilot.list_copilot_seats_org()
        self.assertEqual(response, {"seats": "org_seats"})

    @patch('api.copilot.requests.get')
    def test_get_copilot_seat_user(self, mock_get):
        mock_get.return_value.json.return_value = {"seat": "user_seat"}
        response = self.copilot.get_copilot_seat_user("test_user")
        self.assertEqual(response, {"seat": "user_seat"})

    @patch('api.copilot.requests.post')
    def test_add_users_to_copilot(self, mock_post):
        mock_post.return_value.json.return_value = {"result": "users_added"}
        response = self.copilot.add_users_to_copilot(["user1", "user2"])
        self.assertEqual(response, {"result": "users_added"})

    @patch('api.copilot.requests.delete')
    def test_remove_users_from_copilot(self, mock_delete):
        mock_delete.return_value.json.return_value = {"result": "users_removed"}
        response = self.copilot.remove_users_from_copilot(["user1", "user2"])
        self.assertEqual(response, {"result": "users_removed"})

    @patch('api.copilot.requests.post')
    def test_add_teams_to_copilot(self, mock_post):
        mock_post.return_value.json.return_value = {"result": "teams_added"}
        response = self.copilot.add_teams_to_copilot(["team1", "team2"])
        self.assertEqual(response, {"result": "teams_added"})

    @patch('api.copilot.requests.delete')
    def test_remove_teams_from_copilot(self, mock_delete):
        mock_delete.return_value.json.return_value = {"result": "teams_removed"}
        response = self.copilot.remove_teams_from_copilot(["team1", "team2"])
        self.assertEqual(response, {"result": "teams_removed"})

if __name__ == '__main__':
    unittest.main()
