import os
from dotenv import load_dotenv

load_dotenv()


def discover_credentials():

    consumer_key = 'CONSUMER_KEY'
    consumer_secret = 'CONSUMER_SECRET'
    api_url = 'API_URL'

    if consumer_key in os.environ and consumer_secret in os.environ and api_url in os.environ:
        return os.environ[consumer_key], os.environ[consumer_secret], os.environ[api_url]

    raise AttributeError(
        f"Missing credentials: {consumer_key}, {consumer_secret}, {api_url}. Please, add your credentials to the environment variables."
    )