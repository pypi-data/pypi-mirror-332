import unittest
from unittest.mock import patch
import sys
import os

# Add the project directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from api.custom_properties import CustomProperties

class TestCustomProperties(unittest.TestCase):
    def setUp(self):
        self.token = os.getenv('GITHUB_TOKEN')
        self.org = os.getenv('GITHUB_ORG')
        self.repo = os.getenv('GITHUB_REPO', 'test_repo')
        self.custom_properties = CustomProperties(self.token, self.org, self.repo)

    @patch('api.custom_properties.requests.get')
    def test_list_org_custom_properties(self, mock_get):
        mock_get.return_value.json.return_value = {"properties": "org_properties"}
        response = self.custom_properties.list_org_custom_properties()
        self.assertEqual(response, {"properties": "org_properties"})

    @patch('api.custom_properties.requests.get')
    def test_get_org_custom_property(self, mock_get):
        mock_get.return_value.json.return_value = {"property": "org_property"}
        response = self.custom_properties.get_org_custom_property("test_property")
        self.assertEqual(response, {"property": "org_property"})

    @patch('api.custom_properties.requests.put')
    def test_create_org_custom_property(self, mock_put):
        mock_put.return_value.json.return_value = {"result": "org_property_created"}
        response = self.custom_properties.create_org_custom_property("test_property", {"data": "value"})
        self.assertEqual(response, {"result": "org_property_created"})

    @patch('api.custom_properties.requests.patch')
    def test_update_org_custom_property(self, mock_patch):
        mock_patch.return_value.json.return_value = {"result": "org_property_updated"}
        response = self.custom_properties.update_org_custom_property("test_property", {"data": "new_value"})
        self.assertEqual(response, {"result": "org_property_updated"})

    @patch('api.custom_properties.requests.delete')
    def test_delete_org_custom_property(self, mock_delete):
        mock_delete.return_value.json.return_value = {"result": "org_property_deleted"}
        response = self.custom_properties.delete_org_custom_property("test_property")
        self.assertEqual(response, {"result": "org_property_deleted"})

    @patch('api.custom_properties.requests.get')
    def test_list_repo_custom_properties(self, mock_get):
        mock_get.return_value.json.return_value = {"properties": "repo_properties"}
        response = self.custom_properties.list_repo_custom_properties()
        self.assertEqual(response, {"properties": "repo_properties"})

    @patch('api.custom_properties.requests.get')
    def test_get_repo_custom_property(self, mock_get):
        mock_get.return_value.json.return_value = {"property": "repo_property"}
        response = self.custom_properties.get_repo_custom_property("test_property")
        self.assertEqual(response, {"property": "repo_property"})

    @patch('api.custom_properties.requests.put')
    def test_create_repo_custom_property(self, mock_put):
        mock_put.return_value.json.return_value = {"result": "repo_property_created"}
        response = self.custom_properties.create_repo_custom_property("test_property", {"data": "value"})
        self.assertEqual(response, {"result": "repo_property_created"})

    @patch('api.custom_properties.requests.patch')
    def test_update_repo_custom_property(self, mock_patch):
        mock_patch.return_value.json.return_value = {"result": "repo_property_updated"}
        response = self.custom_properties.update_repo_custom_property("test_property", {"data": "new_value"})
        self.assertEqual(response, {"result": "repo_property_updated"})

    @patch('api.custom_properties.requests.delete')
    def test_delete_repo_custom_property(self, mock_delete):
        mock_delete.return_value.json.return_value = {"result": "repo_property_deleted"}
        response = self.custom_properties.delete_repo_custom_property("test_property")
        self.assertEqual(response, {"result": "repo_property_deleted"})

if __name__ == '__main__':
    unittest.main()
