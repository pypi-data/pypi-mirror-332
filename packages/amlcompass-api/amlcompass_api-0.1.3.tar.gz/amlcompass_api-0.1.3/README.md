# AML Optima Compass API Client

A Python client library for interacting with the AML Optima Compass API.

## Installation

```bash
pip install amlcompass_api
```

## Configuration

There are two ways to configure the client:

### Environment Variables (Recommended)

Create a `.env` file in your project root:

```plaintext
CONSUMER_KEY=your_consumer_key
CONSUMER_SECRET=your_consumer_secret
API_URL=https://api.amlcompass.com
```

### Explicit Configuration

```python
from amlcompass_api import AMLCompassAPIClient

aml_client = AMLCompassAPIClient(
    consumer_key="your_consumer_key",
    consumer_secret="your_consumer_secret",
    api_url="https://api.amlcompass.com"
)
```

## Usage Examples

### Transaction Operations

```python
from amlcompass_api import AMLCompassAPIClient

# Define transaction data
transaction_id: str = "123456"
document_url: str = "https://example.com/document.pdf"
document_type: int = 1

# Initialize client. 
# If you have set environment variables, you can skip the explicit configuration.
aml_client = AMLCompassAPIClient()

# Check if a transaction is valid:
aml_client.transaction_service.is_valid(transaction_id)

# Get Transaction Data:
aml_client.transaction_service.get_data(transaction_id)

# Add a document to a transaction:
aml_client.transaction_service.add_document(transaction_id, document_url, document_type)


# Responses example:
{
  "data": {"valid": True, "transaction_id": "123456"},
  "status_code": 200,
}


```


## Available Features

- **Authentication**
  - OAuth 1.0 support
  
- **Transaction Services**
  - Transaction data retrieval
  - Transaction validation
  - Document attachment
  
- **Future Services** (Coming Soon)

## Development

### Setup Local Environment

```bash
# Clone repository
git clone https://github.com/yarel2l/amlcompass_api.git
cd amlcompass_api

# Install development dependencies
pip install -r requirements.txt

# Run tests
pytest
```


### Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -am 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Create Pull Request

### Development Guidelines

- Run tests before submitting PRs
- Add documentation for new features
- Follow Python type hinting conventions
- Update changelog

## License

MIT License - See [LICENSE](LICENSE) for details.