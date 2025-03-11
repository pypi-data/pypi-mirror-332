import requests
from requests_oauthlib import OAuth1Session


class AMLCompassAPIAuth:
    def __init__(self, consumer_key, consumer_secret, api_url):
        self.consumer_key = consumer_key.strip()
        self.consumer_secret = consumer_secret.strip()
        self.api_url = api_url.rstrip('/')
        self.request_token_url = f"{self.api_url}/oauth.php/request_token"
        self.authorization_url = f"{self.api_url}/authorize.php"
        self.access_token_url = f"{self.api_url}/oauth.php/access_token"
        self.oauth_session = None
        self.access_token = None
        self.access_token_secret = None

    def initialize_oauth_session(self):
        """Initializes or reinitializes the OAuth session with the current tokens"""
        if not self.access_token or not self.access_token_secret:
            return False

        self.oauth_session = OAuth1Session(
            self.consumer_key,
            client_secret=self.consumer_secret,
            resource_owner_key=self.access_token,
            resource_owner_secret=self.access_token_secret
        )
        return True

    def get_request_token(self):
        print(f"Attempting to obtain request token with consumer_key: {self.consumer_key[:5]}...")
        print(f"Request URL: {self.request_token_url}")

        try:
            oauth = OAuth1Session(
                self.consumer_key,
                client_secret=self.consumer_secret,
                callback_uri='oob'  # Añadir callback para autenticación fuera de banda
            )

            headers = {'Accept': 'application/json'}
            response = oauth.fetch_request_token(self.request_token_url, headers=headers, timeout=30)
            print(f"Token obtained successfully: {response}")
            return response
        except Exception as e:
            print(f"Detailed error: {str(e)}")

            # Verify that the server responds
            try:
                base_resp = requests.get(self.api_url, timeout=5)
                print(f"API base responds: {base_resp.status_code}")
            except Exception as base_err:
                print(f"API not accessible: {str(base_err)}")

            raise

    def get_authorization_url(self, request_token):
        oauth = OAuth1Session(self.consumer_key, client_secret=self.consumer_secret, resource_owner_key=request_token)
        authorization_url = oauth.authorization_url(self.authorization_url)
        return authorization_url

    def get_access_token(self, request_token, request_token_secret, verifier):
        oauth = OAuth1Session(
            self.consumer_key,
            client_secret=self.consumer_secret,
            resource_owner_key=request_token,
            resource_owner_secret=request_token_secret,
            verifier=verifier
        )
        token = oauth.fetch_access_token(self.access_token_url)
        self.access_token = token.get("oauth_token")
        self.access_token_secret = token.get("oauth_token_secret")

        self.initialize_oauth_session()
        return token

    def get_verifier_programmatically(self, request_token):
        params = {'oauth_token': request_token}
        response = requests.get(self.authorization_url, params=params, auth=(self.consumer_key, self.consumer_secret))
        if response.status_code == 200:
            verifier = response.text.strip()
            return verifier
        else:
            raise Exception(f"Error getting verifier: {response.status_code} {response.text}")

    def authenticate(self, use_programmatic_verifier=True):
        try:
            request_token_response = self.get_request_token()
            request_token = request_token_response.get("oauth_token")
            request_token_secret = request_token_response.get("oauth_token_secret")

            if not request_token or not request_token_secret:
                raise ValueError("No valid request tokens obtained")

            if use_programmatic_verifier:
                verifier = self.get_verifier_programmatically(request_token)
            else:
                auth_url = self.get_authorization_url(request_token)
                print("Please visit the following URL and authorize the application:", auth_url)
                verifier = input("Enter the provided verifier: ").strip()

            self.get_access_token(request_token, request_token_secret, verifier)

            # Additional verification
            if not self.oauth_session:
                raise ValueError("OAuth session was not initialized correctly")

            return self.access_token, self.access_token_secret

        except Exception as e:
            print(f"Authentication error: {str(e)}")
            if use_programmatic_verifier:
                print("Retrying with manual method...")
                return self.authenticate(use_programmatic_verifier=False)
            raise