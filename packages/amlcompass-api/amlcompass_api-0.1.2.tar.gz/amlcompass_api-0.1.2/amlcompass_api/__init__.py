import sys

def custom_exception_handler(exc_type, exc_value, exc_traceback):
    # Si se trata de un ConnectionError, se imprime solo el mensaje
    if issubclass(exc_type, ConnectionError) or issubclass(exc_type, AttributeError):
        print(exc_value)
    else:
        # Para otros tipos de error, se utiliza el handler por defecto
        sys.__excepthook__(exc_type, exc_value, exc_traceback)

sys.excepthook = custom_exception_handler


from amlcompass_api.client import AMLCompassAPIClient, aml_client

__all__ = [
    "AMLCompassAPIClient",
    "aml_client"
]