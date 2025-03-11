import logging
import requests
from amlcompass_api.exceptions import ApiClientException
from amlcompass_api.response import Response

logger = logging.getLogger(__name__)


class TransactionService:
    def __init__(self, auth_instance, api_url):
        self.auth = auth_instance
        self.api_url = api_url.rstrip('/')

    def get_data(self, transaction_id: str) -> Response:
        """
            Retrieves transaction data from the API based on the provided transaction code (transaction_id).

            This method makes a GET request to the transactions endpoint with the specified transaction_id
            as a query parameter. It handles various HTTP exceptions that may occur during the request.

            :param transaction_id: Transaction code to identify the transaction in the API
            :return: Response object with status_code and data containing the transaction information
            :raises ApiClientException: With appropriate error message and code in these cases:
                - HTTP errors (with original status code)
                - Connection errors (code 500)
                - Timeout errors (code 504)
                - General request exceptions (code 500)
        """

        endpoint = "transactions"
        url = f"{self.api_url}/{endpoint.lstrip('/')}"
        params = {"Pcode": transaction_id}

        response = self.auth.oauth_session.get(url, params=params)
        try:
            response.raise_for_status()
            result = response.json()
            return Response(
                data=result.get('Rtransaction'),
                status_code=200
            )
        except requests.exceptions.HTTPError as http_err:
            error_message = f"HTTP error occurred for Pcode {transaction_id}: {http_err}"
            logger.error(error_message)
            raise ApiClientException(
                message=error_message,
                code=http_err.response.status_code
            )
        except requests.exceptions.ConnectionError as conn_err:
            error_message = f"Connection error occurred for Pcode {transaction_id}: {conn_err}"
            logger.error(error_message)
            raise ApiClientException(message=error_message, code=500)
        except requests.exceptions.Timeout as timeout_err:
            error_message = f"Timeout error occurred for Pcode {transaction_id}: {timeout_err}"
            logger.error(error_message)
            raise ApiClientException(message=error_message, code=504)
        except requests.exceptions.RequestException as req_err:
            error_message = f"Request error occurred for Pcode {transaction_id}: {req_err}"
            logger.error(error_message)
            raise ApiClientException(message=error_message, code=500)

    def is_valid(self, transaction_id: str) -> Response:
        """
            Verifies if a transaction is valid based on the transaction code (transaction_id).

            This method checks the existence and validity of a transaction by requesting
            its data from the API and analyzing the response. A transaction is considered
            valid if the API returns non-empty data.

            :param transaction_id: Transaction code used to identify the transaction in the API
            :return: Response object with status_code=200 and data containing:
                     - 'valid': Boolean indicating if the transaction is valid
                     - 'transaction_id': The original transaction code
            :raises ApiClientException: With appropriate error message and code in these cases:
                     - When underlying API calls fail
                     - When validation process encounters errors (code 500)
        """
        try:
            transaction = self.get_data(transaction_id)

            # Determinar validez según el tipo de datos recibido
            if transaction.data is None:
                valid = False
            elif isinstance(transaction.data, list):
                valid = bool(transaction.data)  # Más conciso que len > 0
            elif isinstance(transaction.data, dict):
                valid = bool(transaction.data)  # Más conciso que len > 0
            else:
                valid = bool(transaction.data)

            logger.debug(f"Transaction validation for {transaction_id}: {valid}")

            return Response(
                data={"valid": valid, "transaction_id": transaction_id},
                status_code=200
            )

        except ApiClientException as api_err:
            raise ApiClientException(
                message=f"Error validating transaction: {api_err.message}",
                code=api_err.code
            )
        except Exception as e:
            error_message = f"Error validating transaction {transaction_id}: {e}"
            logger.error(error_message)
            raise ApiClientException(message=error_message, code=500)

    def add_document(self, transaction_id: str, document_url: str, document_type: int) -> Response:
        """
            Service 4. Reports a new document associated with a transaction to AML Compass using a URL.

            This method sends a POST request to the AML Compass API to report a new document
            associated with a specific transaction. The document is identified by a URL and
            a document type ID.

            :param transaction_id: Transaction number to which the document is associated.
            :param document_url: String containing a valid URL where the new document is located.
            :param document_type: Integer representing the ID of the document type.
            :return: Response object with status_code and data containing the API response in JSON format.
                     The expected format of the response data is {'Rerror_code': 0, 'Rerror_message': ''}.
            :raises ApiClientException: With appropriate error message and code in these cases:
                     - HTTP errors (with original status code)
                     - Connection errors (code 500)
                     - Timeout errors (code 504)
                     - General request exceptions (code 500)
        """
        endpoint = "transactions/addurldocument"
        url = f"{self.api_url}/{endpoint.lstrip('/')}"
        data = {
            "Pcode": transaction_id,
            "PURLdocument": document_url,
            "Pdocument_type_id": document_type
        }
        response = self.auth.oauth_session.post(url, json=data)
        try:
            response.raise_for_status()
            result = response.json()
            if str(result.get('Rerror_code')) != '0':
                error_message = f"Error reporting document for transaction {transaction_id}: {result.get('Rerror_message')}"
                logger.error(error_message)
                raise ApiClientException(
                    message=error_message,
                    code=400
                )
            return Response(
                data=result.get('Rerror_message'),
                status_code=200
            )
        except requests.exceptions.HTTPError as http_err:
            error_message = f"HTTP error occurred: {http_err}"
            logger.error(error_message)
            raise ApiClientException(
                message=error_message,
                code=http_err.response.status_code
            )
        except requests.exceptions.ConnectionError as conn_err:
            error_message = f"Connection error occurred: {conn_err}"
            logger.error(error_message)
            raise ApiClientException(
                message=error_message,
                code=500
            )
        except requests.exceptions.Timeout as timeout_err:
            error_message = f"Timeout error occurred: {timeout_err}"
            logger.error(error_message)
            raise ApiClientException(
                message=error_message,
                code=504
            )
        except requests.exceptions.RequestException as req_err:
            error_message = f"Request error occurred: {req_err}"
            logger.error(error_message)
            raise ApiClientException(
                message=error_message,
                code=500
            )