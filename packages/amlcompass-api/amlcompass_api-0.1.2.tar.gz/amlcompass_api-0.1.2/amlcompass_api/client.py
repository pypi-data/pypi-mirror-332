
from .credentials import discover_credentials
from .auth import AMLCompassAPIAuth
from .services.transactions import TransactionService

consumer_key, consumer_secret, api_url = discover_credentials()


class AMLCompassAPIClient:
    """
        AMLCompassAPIClient is a client for interacting with the AML Compass API.

        Attributes:
            consumer_key (str): The consumer key for API authentication.
            consumer_secret (str): The consumer secret for API authentication.
            api_url (str): The base URL for the API.
    """

    def __init__(self, consumer_key, consumer_secret, api_url):

        if not consumer_key or not consumer_secret or not api_url:
            raise ConnectionError(f"Missing credentials. Please, verify all required fields are provided.")

        self.consumer_key = consumer_key.strip()
        self.consumer_secret = consumer_secret.strip()
        self.api_url = api_url.rstrip('/')

        # Create and authenticate the authentication instance
        self.auth = AMLCompassAPIAuth(self.consumer_key, self.consumer_secret, self.api_url)

        try:
            # Initial authentication
            self.auth.authenticate()

            # Verify that the authentication was successful
            if not self.auth.oauth_session:
                raise ValueError("Could not establish the OAuth session")

        except Exception as e:
            raise ConnectionError(f"Error authenticating with Optima Compass API: {str(e)}")

        # Initialize services passing the authorization instance
        # instead of the session directly
        self.transaction_service = TransactionService(
            self.auth,
            self.api_url
        )

    @property
    def oauth_session(self):
        """Access to the updated OAuth session"""
        return self.auth.oauth_session

    @property
    def access_token(self):
        """Access to the access token"""
        return self.auth.access_token

    @property
    def access_token_secret(self):
        """Access to the access token secret"""
        return self.auth.access_token_secret


aml_client = AMLCompassAPIClient(consumer_key, consumer_secret, api_url)
