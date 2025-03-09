import requests
import unittest
from unittest.mock import patch, MagicMock
from amlcompass_api.services.transactions import TransactionService


class TestTransactionService(unittest.TestCase):
    def setUp(self):
        # Create a mock of the auth object directly
        self.mock_auth = MagicMock()
        # Ensure that oauth_session exists
        self.mock_auth.oauth_session = MagicMock()
        # Create the service with the mock
        self.service = TransactionService(self.mock_auth, "https://test.api.com")

    def test_transaction_data_retrieved_successfully(self):
        # Configure the mock behavior
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "Rerror_code": "0",
            "Rerror_message": "",
            "Rtransaction": {}
        }
        mock_response.status_code = 200
        self.mock_auth.oauth_session.get.return_value = mock_response

        # Execute the method to be tested
        response = self.service.get_data("CODE123")

        # Verify the result
        self.assertEqual(response["Rerror_code"], "0")
        self.assertEqual(response["Rerror_message"], "")
        self.assertIsInstance(response["Rtransaction"], dict)

        # Verify that it was called with the correct parameters
        self.mock_auth.oauth_session.get.assert_called_once()
        args, kwargs = self.mock_auth.oauth_session.get.call_args
        self.assertEqual(args[0], "https://test.api.com/transactions")
        self.assertEqual(kwargs["params"], {"Pcode": "CODE123"})

    def test_transaction_data_retrieval_failure(self):
        # Create a mock response that raises an exception when calling raise_for_status()
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = requests.exceptions.RequestException("Error")
        self.mock_auth.oauth_session.get.return_value = mock_response

        # Execute the method to be tested
        response = self.service.get_data("CODE123")

        # Verify that it returns None when there is an error
        self.assertIsNone(response)

    def test_transaction_is_valid(self):
        # Config  mock
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "Rtransaction": {"key": "value"}
        }
        mock_response.status_code = 200
        self.mock_auth.oauth_session.get.return_value = mock_response

        # Execute the method to be tested
        valid = self.service.is_valid("CODE123")

        # Verify the result
        self.assertTrue(valid)

    def test_transaction_is_invalid(self):
        # Config mock
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "Rtransaction": None
        }
        mock_response.status_code = 200
        self.mock_auth.oauth_session.get.return_value = mock_response

        # Execute the method to be tested
        valid = self.service.is_valid("CODE123")

        # Verify the result
        self.assertFalse(valid)

    def test_document_added_successfully(self):
        # Config mock
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "Rerror_code": 0,
            "Rerror_message": ""
        }
        mock_response.status_code = 200
        self.mock_auth.oauth_session.post.return_value = mock_response

        # Execute the method to be tested
        response = self.service.add_document("CODE123", "https://example.com/document.pdf", 1)

        # Verify the result
        self.assertEqual(response["Rerror_code"], 0)
        self.assertEqual(response["Rerror_message"], "")

        # Verify that it was called with the correct parameters
        self.mock_auth.oauth_session.post.assert_called_once()
        args, kwargs = self.mock_auth.oauth_session.post.call_args
        self.assertEqual(args[0], "https://test.api.com/transactions/addurldocument")
        self.assertEqual(kwargs["json"], {
            "Pcode": "CODE123",
            "PURLdocument": "https://example.com/document.pdf",
            "Pdocument_type_id": 1
        })

    def test_document_addition_failure(self):
        # Create a mock response that raises an exception when calling raise_for_status()
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = requests.exceptions.RequestException("Error")
        self.mock_auth.oauth_session.post.return_value = mock_response

        # # Execute the method to be tested
        response = self.service.add_document("CODE123", "https://example.com/document.pdf", 1)

        # Verify that it returns None when there is an error
        self.assertIsNone(response)