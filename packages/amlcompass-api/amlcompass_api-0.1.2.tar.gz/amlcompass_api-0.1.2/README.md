# AML Optima Compass API Client

A Python client library for interacting with the AML Optima Compass API.

## Installation

```bash
pip install amlcompass_api
```

## Quick Start

1. Create `.env` file in your project root:
```plaintext
CONSUMER_KEY=<your_consumer_key>
CONSUMER_SECRET=<your_consumer_secret>
API_URL=https://api.amlcompass.com
```

2. Basic Usage:
```python
from amlcompass_api import aml_client
from typing import Dict

# Get transaction details
def get_transaction(transaction_id: str) -> Dict:
    return aml_client.transaction_service.get_data(transaction_id)

# Add document to transaction
def add_document(transaction_id: str, document_url: str, doc_type_id: int) -> Dict:
    return aml_client.transaction_service.add_document(
        transaction_id=transaction_id,
        document_url=document_url,
        document_type_id=doc_type_id
    )
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