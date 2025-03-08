import logging
import requests

logger = logging.getLogger(__name__)


class TransactionService:
    def __init__(self, auth_instance, api_url):
        self.auth = auth_instance
        self.api_url = api_url.rstrip('/')

    def get_data(self, pcode):
        """
            Retrieves transaction data from the API based on the provided transaction code (Pcode).

            :param pcode: Transaction code
            :return: JSON response from the API if successful, e.g., {'Rerror_code': '0', 'Rerror_message': '', 'Rtransaction': {} or []}, None otherwise
        """

        endpoint = "transactions"
        url = f"{self.api_url}/{endpoint.lstrip('/')}"
        params = {"Pcode": pcode}

        response = self.auth.oauth_session.get(url, params=params)
        try:
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error getting transaction data: {e}")
            return None

    def is_valid(self, pcode):
        """
            Verifies if a transaction is valid based on the transaction code (Pcode).

            :param pcode: Transaction code
            :return: True if the transaction is valid, False otherwise
        """
        transaction = self.get_data(pcode)
        rt = transaction.get("Rtransaction")

        if rt is None:
            valid = False
        elif isinstance(rt, list):
            valid = len(rt) > 0
        elif isinstance(rt, dict):
            valid = len(rt.keys()) > 0
        else:
            valid = bool(rt)

        return valid

    def add_document(self, pcode, purl_document, pdocument_type_id):
        """
            Service 4. Reports to AML Compass a new document associated with a transaction using a URL.

            :param pcode: Transaction number
            :param purl_document: String containing a valid URL where the new document is located
            :param pdocument_type_id: ID of the document type
            :return: API response in JSON format {'Rerror_code': 0, 'Rerror_message': ''}
        """
        endpoint = "transactions/addurldocument"
        url = f"{self.api_url}/{endpoint.lstrip('/')}"
        data = {
            "Pcode": pcode,
            "PURLdocument": purl_document,
            "Pdocument_type_id": pdocument_type_id
        }
        response = self.auth.oauth_session.post(url, json=data)
        try:
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error reporting document: {e}")
            return None