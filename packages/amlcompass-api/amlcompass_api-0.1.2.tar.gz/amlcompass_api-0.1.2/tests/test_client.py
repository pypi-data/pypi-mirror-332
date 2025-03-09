import unittest
from unittest.mock import patch, MagicMock
from amlcompass_api import AMLCompassAPIClient


class TestAMLCompassAPIClient(unittest.TestCase):
    @patch('amlcompass_api.client.AMLCompassAPIAuth')
    def test_client_initialization_successful(self, mock_auth_class):
        # Crear mock para el método authenticate
        mock_auth_instance = MagicMock()
        mock_auth_instance.oauth_session = MagicMock()  # Asegurar que oauth_session existe
        mock_auth_class.return_value = mock_auth_instance

        client = AMLCompassAPIClient(
            consumer_key="test_key",
            consumer_secret="test_secret",
            api_url="https://test.api.com"
        )

        mock_auth_instance.authenticate.assert_called_once()
        self.assertIsNotNone(client.transaction_service)

    @patch('amlcompass_api.client.AMLCompassAPIAuth')
    def test_client_initialization_missing_credentials(self, mock_auth_class):
        with self.assertRaises(ConnectionError) as context:
            AMLCompassAPIClient(
                consumer_key="",
                consumer_secret="test_secret",
                api_url="https://test.api.com"
            )
        self.assertIn("Missing credentials", str(context.exception))

    @patch('amlcompass_api.client.AMLCompassAPIAuth')
    def test_client_initialization_authentication_failure(self, mock_auth_class):
        mock_auth_instance = MagicMock()
        mock_auth_instance.authenticate.side_effect = Exception("Authentication error")
        mock_auth_class.return_value = mock_auth_instance

        with self.assertRaises(ConnectionError) as context:
            AMLCompassAPIClient(
                consumer_key="test_key",
                consumer_secret="test_secret",
                api_url="https://test.api.com"
            )
        self.assertIn("Error authenticating with Optima Compass API", str(context.exception))

    @patch('amlcompass_api.client.AMLCompassAPIAuth')
    def test_oauth_session_property(self, mock_auth_class):
        mock_auth_instance = MagicMock()
        mock_auth_instance.oauth_session = "mock_session"
        mock_auth_class.return_value = mock_auth_instance

        mock_auth_instance.authenticate = MagicMock()

        client = AMLCompassAPIClient(
            consumer_key="test_key",
            consumer_secret="test_secret",
            api_url="https://test.api.com"
        )

        self.assertEqual(client.oauth_session, "mock_session")

    @patch('amlcompass_api.client.AMLCompassAPIAuth')
    def test_access_token_property(self, mock_auth_class):
        mock_auth_instance = MagicMock()
        mock_auth_instance.access_token = "mock_access_token"
        mock_auth_instance.oauth_session = MagicMock()  # Necesario para evitar error
        mock_auth_class.return_value = mock_auth_instance

        mock_auth_instance.authenticate = MagicMock()

        client = AMLCompassAPIClient(
            consumer_key="test_key",
            consumer_secret="test_secret",
            api_url="https://test.api.com"
        )

        self.assertEqual(client.access_token, "mock_access_token")

    @patch('amlcompass_api.client.AMLCompassAPIAuth')
    def test_access_token_secret_property(self, mock_auth_class):
        mock_auth_instance = MagicMock()
        mock_auth_instance.access_token_secret = "mock_access_token_secret"
        mock_auth_instance.oauth_session = MagicMock()  # Necesario para evitar error
        mock_auth_class.return_value = mock_auth_instance

        mock_auth_instance.authenticate = MagicMock()

        client = AMLCompassAPIClient(
            consumer_key="test_key",
            consumer_secret="test_secret",
            api_url="https://test.api.com"
        )

        self.assertEqual(client.access_token_secret, "mock_access_token_secret")