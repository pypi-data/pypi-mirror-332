import unittest
from unittest.mock import patch, MagicMock
from amlcompass_api.credentials import discover_credentials

class TestDiscoverCredentials(unittest.TestCase):
    @patch.dict('os.environ', {'CONSUMER_KEY': 'test_key', 'CONSUMER_SECRET': 'test_secret', 'API_URL': 'https://test.api.com'})
    def test_credentials_discovered_successfully(self):
        consumer_key, consumer_secret, api_url = discover_credentials()
        self.assertEqual(consumer_key, 'test_key')
        self.assertEqual(consumer_secret, 'test_secret')
        self.assertEqual(api_url, 'https://test.api.com')

    @patch.dict('os.environ', {}, clear=True)
    def test_credentials_missing_raises_error(self):
        with self.assertRaises(AttributeError) as context:
            discover_credentials()
        self.assertIn("Missing credentials", str(context.exception))