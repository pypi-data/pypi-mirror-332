# AML Optima Compass API Client

Simple python api client for AML Optima Compass API.


## Features

- Authenticate with AML Optima Compass API using OAuth 1.0.
- Transaction services:
  - Get transaction data.
  - Check valid transactions.
  - Add document to a transaction.
- TODO: Other Services

## Installation

    ```bash
    pip install amlcompass_api


## Usage

1. Create a file named `.env` in the root of your project.
2. In the `.env` file, define the following environment variables with your credentials and the API URL:
    ```plaintext
    CONSUMER_KEY=your_consumer_key
    CONSUMER_SECRET=your_consumer_secret
    API_URL=https://*.amlcompass.com/
    ```

3. Use the AML Compass API client in your Python code:
    ```python
    from amlcompass_api import aml_client
    
    # Verificar una transacción
    transaction_data = aml_client.transaction_service.get_data("CODE123")
    print(transaction_data)
    
    # Añadir un documento a una transacción
    result = aml_client.transaction_service.add_document(
        "CODE123", 
        "https://ejemplo.com/documento.pdf", 
        83
    )
   ```
   
## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D
6. Remember to run the tests before submitting the PR.
7. If you are adding a new feature, remember to add the documentation for it in the README.md file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

