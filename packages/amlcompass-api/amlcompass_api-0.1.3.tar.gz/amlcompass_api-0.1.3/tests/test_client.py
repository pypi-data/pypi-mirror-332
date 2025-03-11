import unittest
from unittest.mock import patch, MagicMock

from amlcompass_api.auth import AMLCompassAPIAuth
from amlcompass_api.client import AMLCompassAPIClient
from amlcompass_api.services.transactions import TransactionService


class TestAMLCompassAPIClient(unittest.TestCase):

    @patch('amlcompass_api.client.AMLCompassAPIAuth')
    @patch('amlcompass_api.client.TransactionService')
    def test_client_initialization_successful(self, mock_transaction_service, mock_auth):
        mock_auth_instance = MagicMock()
        mock_auth.return_value = mock_auth_instance
        mock_transaction_service.return_value = MagicMock()

        client = AMLCompassAPIClient("test_consumer_key", "test_consumer_secret", "https://test.api.com")
        self.assertEqual(client.consumer_key, "test_consumer_key")
        self.assertEqual(client.consumer_secret, "test_consumer_secret")
        self.assertEqual(client.api_url, "https://test.api.com")
        mock_auth.assert_called_with("test_consumer_key", "test_consumer_secret", "https://test.api.com")
        mock_transaction_service.assert_called_with(mock_auth_instance, "https://test.api.com")

    @patch('amlcompass_api.client.TransactionService')
    @patch('amlcompass_api.client.AMLCompassAPIAuth')
    def test_client_missing_credentials_error(self, mock_auth, mock_transaction_service):
        with self.assertRaises(ConnectionError) as context:
            AMLCompassAPIClient(consumer_key=None, consumer_secret=None, api_url=None)
        self.assertEqual(str(context.exception),
                         "Missing credentials. Please, verify all required fields are provided.")

    @patch('amlcompass_api.client.AMLCompassAPIAuth')
    @patch('amlcompass_api.client.TransactionService')
    def test_client_oauth_session(self, mock_transaction_service, mock_auth):
        mock_auth_instance = MagicMock()
        mock_auth.return_value = mock_auth_instance
        mock_auth_instance.oauth_session = "test_oauth_session"

        client = AMLCompassAPIClient("test_consumer_key", "test_consumer_secret", "https://test.api.com")
        self.assertEqual(client.oauth_session, "test_oauth_session")

    @patch('amlcompass_api.client.AMLCompassAPIAuth')
    @patch('amlcompass_api.client.TransactionService')
    def test_client_access_token(self, mock_transaction_service, mock_auth):
        mock_auth_instance = MagicMock()
        mock_auth_instance.access_token = "test_access_token"
        mock_auth.return_value = mock_auth_instance

        client = AMLCompassAPIClient("test_consumer_key", "test_consumer_secret", "https://test.api.com")
        self.assertEqual(client.access_token, "test_access_token")

    @patch('amlcompass_api.client.AMLCompassAPIAuth')
    @patch('amlcompass_api.client.TransactionService')
    def test_client_access_token_secret(self, mock_transaction_service, mock_auth):
        mock_auth_instance = MagicMock()
        mock_auth_instance.access_token_secret = "test_access_token_secret"
        mock_auth.return_value = mock_auth_instance

        client = AMLCompassAPIClient("test_consumer_key", "test_consumer_secret", "https://test.api.com")
        self.assertEqual(client.access_token_secret, "test_access_token_secret")

