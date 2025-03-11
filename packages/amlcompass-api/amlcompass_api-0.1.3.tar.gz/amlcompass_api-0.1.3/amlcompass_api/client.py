
import os
from dotenv import load_dotenv
from .auth import AMLCompassAPIAuth
from .services.transactions import TransactionService

load_dotenv()


class AMLCompassAPIClient:
    """
        AMLCompassAPIClient is a client for interacting with the AML Compass API.

        Attributes:
            consumer_key (str): The consumer key for API authentication.
            consumer_secret (str): The consumer secret for API authentication.
            api_url (str): The base URL for the API.
    """
    def __init__(self, consumer_key=None, consumer_secret=None, api_url=None):
        """Initialize the AML Compass API client.

        Args:
            consumer_key: API consumer key or None to use environment variable
            consumer_secret: API consumer secret or None to use environment variable
            api_url: Base API URL or None to use environment variable

        Raises:
            ConnectionError: If credentials are missing or authentication fails
        """
        # Load and validate credentials
        self._load_credentials(consumer_key, consumer_secret, api_url)
        self._validate_credentials()

        # Process credentials
        self.consumer_key = self.consumer_key.strip()
        self.consumer_secret = self.consumer_secret.strip()
        self.api_url = self.api_url.rstrip('/')

        # Authenticate
        self._setup_authentication()

        # Initialize services
        self.transaction_service = TransactionService(self.auth, self.api_url)

    def _load_credentials(self, consumer_key, consumer_secret, api_url):
        """Load credentials from parameters or environment variables."""
        self.consumer_key = consumer_key or os.environ.get('CONSUMER_KEY')
        self.consumer_secret = consumer_secret or os.environ.get('CONSUMER_SECRET')
        self.api_url = api_url or os.environ.get('API_URL')

    def _validate_credentials(self):
        """Validate that all required credentials are present."""
        if not all([self.consumer_key, self.consumer_secret, self.api_url]):
            raise ConnectionError("Missing credentials. Please, verify all required fields are provided.")

    def _setup_authentication(self):
        """Set up and authenticate the API connection."""
        try:
            self.auth = AMLCompassAPIAuth(self.consumer_key, self.consumer_secret, self.api_url)
            self.auth.authenticate()

            if not self.auth.oauth_session:
                raise ValueError("Could not establish the OAuth session")
        except Exception as e:
            raise ConnectionError(f"Error authenticating with Optima Compass API: {str(e)}")

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


