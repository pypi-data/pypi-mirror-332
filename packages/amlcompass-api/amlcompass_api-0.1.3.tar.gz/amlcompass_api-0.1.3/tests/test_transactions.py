import requests
import unittest
from unittest.mock import patch, MagicMock

from amlcompass_api.exceptions import ApiClientException
from amlcompass_api.response import Response
from amlcompass_api.services.transactions import TransactionService


class TestTransactionService(unittest.TestCase):

    @patch('amlcompass_api.services.transactions.TransactionService.get_data')
    def test_is_valid_transaction_valid(self, mock_get_data):
        mock_response = Response(status_code=200, data={"Rtransaction": {"transaction_key": "value"}})
        mock_get_data.return_value = mock_response

        auth_instance = MagicMock()
        service = TransactionService(auth_instance, "https://test.api.com")
        result = service.is_valid("valid_pcode")

        self.assertEqual(result.data["valid"], True)
        self.assertEqual(result.data["transaction_id"], "valid_pcode")

    @patch('amlcompass_api.services.transactions.TransactionService.get_data')
    def test_is_valid_transaction_invalid(self, mock_get_data):
        mock_response = Response(status_code=200, data=None)
        mock_get_data.return_value = mock_response

        auth_instance = MagicMock()
        service = TransactionService(auth_instance, "https://test.api.com")
        result = service.is_valid("invalid_pcode")

        self.assertEqual(result.data["valid"], False)
        self.assertEqual(result.data["transaction_id"], "invalid_pcode")

    @patch('amlcompass_api.services.transactions.TransactionService.get_data')
    def test_is_valid_transaction_error(self, mock_get_data):
        mock_get_data.side_effect = ApiClientException("API error", code=500)

        auth_instance = MagicMock()
        service = TransactionService(auth_instance, "https://test.api.com")

        with self.assertRaises(ApiClientException) as context:
            service.is_valid("error_pcode")
        self.assertEqual(context.exception.code, 500)
        self.assertEqual(context.exception.message, "Error validating transaction: API error")

    @patch('amlcompass_api.services.transactions.requests.Session.post')
    def test_add_document_successful(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"Rerror_code": 0, "Rerror_message": ""}

        auth_instance = MagicMock()
        auth_instance.oauth_session.post = mock_post

        service = TransactionService(auth_instance, "https://test.api.com")
        result = service.add_document("test_pcode", "https://test.url/document", 1)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data, "")

    @patch('amlcompass_api.services.transactions.requests.Session.post')
    def test_add_document_api_error(self, mock_post):
        mock_post.return_value.status_code = 400
        mock_post.return_value.json.return_value = {"Rerror_code": 1, "Rerror_message": "Invalid document"}

        auth_instance = MagicMock()
        auth_instance.oauth_session.post = mock_post

        service = TransactionService(auth_instance, "https://test.api.com")

        with self.assertRaises(ApiClientException) as context:
            service.add_document("test_pcode", "https://test.url/document", 1)
        self.assertEqual(context.exception.code, 400)
        self.assertEqual(context.exception.message,
                         "Error reporting document for transaction test_pcode: Invalid document")

    @patch('amlcompass_api.services.transactions.requests.Session.post')
    def test_add_document_http_error(self, mock_post):
        mock_post.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError(
            response=MagicMock(status_code=500))

        auth_instance = MagicMock()
        auth_instance.oauth_session.post = mock_post

        service = TransactionService(auth_instance, "https://test.api.com")

        with self.assertRaises(ApiClientException) as context:
            service.add_document("test_pcode", "https://test.url/document", 1)
        self.assertEqual(context.exception.code, 500)

