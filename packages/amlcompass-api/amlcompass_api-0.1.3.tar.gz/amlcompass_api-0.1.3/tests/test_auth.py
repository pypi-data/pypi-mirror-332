import unittest
from unittest.mock import patch, MagicMock
from amlcompass_api.auth import AMLCompassAPIAuth

class TestAMLCompassAPIAuth(unittest.TestCase):
    @patch('amlcompass_api.auth.OAuth1Session')
    def test_request_token_obtained_successfully(self, mock_oauth):
        mock_oauth_instance = MagicMock()
        mock_oauth.return_value = mock_oauth_instance
        mock_oauth_instance.fetch_request_token.return_value = {
            "oauth_token": "test_token",
            "oauth_token_secret": "test_secret"
        }

        auth = AMLCompassAPIAuth("test_key", "test_secret", "https://test.api.com")
        response = auth.get_request_token()

        self.assertEqual(response["oauth_token"], "test_token")
        self.assertEqual(response["oauth_token_secret"], "test_secret")

    @patch('amlcompass_api.auth.OAuth1Session')
    def test_request_token_failure(self, mock_oauth):
        mock_oauth_instance = MagicMock()
        mock_oauth.return_value = mock_oauth_instance
        mock_oauth_instance.fetch_request_token.side_effect = Exception("Request token error")

        auth = AMLCompassAPIAuth("test_key", "test_secret", "https://test.api.com")

        with self.assertRaises(Exception) as context:
            auth.get_request_token()
        self.assertIn("Request token error", str(context.exception))

    @patch('amlcompass_api.auth.OAuth1Session')
    def test_access_token_obtained_successfully(self, mock_oauth):
        mock_oauth_instance = MagicMock()
        mock_oauth.return_value = mock_oauth_instance
        mock_oauth_instance.fetch_access_token.return_value = {
            "oauth_token": "access_token",
            "oauth_token_secret": "access_secret"
        }

        auth = AMLCompassAPIAuth("test_key", "test_secret", "https://test.api.com")
        auth.get_access_token("request_token", "request_secret", "verifier")

        self.assertEqual(auth.access_token, "access_token")
        self.assertEqual(auth.access_token_secret, "access_secret")
        self.assertIsNotNone(auth.oauth_session)

    @patch('amlcompass_api.auth.requests.get')
    def test_verifier_obtained_programmatically(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = "verifier_code"

        auth = AMLCompassAPIAuth("test_key", "test_secret", "https://test.api.com")
        verifier = auth.get_verifier_programmatically("request_token")

        self.assertEqual(verifier, "verifier_code")

    @patch('amlcompass_api.auth.requests.get')
    def test_verifier_programmatic_failure(self, mock_get):
        mock_get.return_value.status_code = 400
        mock_get.return_value.text = "Error message"

        auth = AMLCompassAPIAuth("test_key", "test_secret", "https://test.api.com")

        with self.assertRaises(Exception) as context:
            auth.get_verifier_programmatically("request_token")
        self.assertIn("Error getting verifier", str(context.exception))

    @patch('amlcompass_api.auth.OAuth1Session')
    def test_authentication_successful(self, mock_oauth_session):
        # Configurar los mocks para simular todas las llamadas OAuth
        mock_oauth_instance = MagicMock()
        mock_oauth_session.return_value = mock_oauth_instance

        # Mock de fetch_request_token
        mock_oauth_instance.fetch_request_token.return_value = {
            "oauth_token": "request_token_test",
            "oauth_token_secret": "request_secret_test"
        }

        # Mock de fetch_access_token
        mock_oauth_instance.fetch_access_token.return_value = {
            "oauth_token": "access_token_test",
            "oauth_token_secret": "access_secret_test"
        }

        # Simular la obtención del verifier
        with patch.object(AMLCompassAPIAuth, 'get_verifier_programmatically', return_value="verifier_code_test"):
            auth = AMLCompassAPIAuth("test_key", "test_secret", "https://test.api.com")
            access_token, access_token_secret = auth.authenticate()

        # Verificar resultados
        self.assertEqual(access_token, "access_token_test")
        self.assertEqual(access_token_secret, "access_secret_test")
        self.assertIsNotNone(auth.oauth_session)

    @patch('amlcompass_api.auth.AMLCompassAPIAuth.get_request_token')
    def test_authentication_failure(self, mock_get_request_token):
        mock_get_request_token.side_effect = Exception("Authentication error")

        auth = AMLCompassAPIAuth("test_key", "test_secret", "https://test.api.com")

        with self.assertRaises(Exception) as context:
            auth.authenticate()
        self.assertIn("Authentication error", str(context.exception))