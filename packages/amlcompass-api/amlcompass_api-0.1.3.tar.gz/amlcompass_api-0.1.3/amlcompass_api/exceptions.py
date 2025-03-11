
class ApiClientException(Exception):
    """
        Custom exception for API client errors.
    """

    def __init__(self, message, code=None):
        """
            Initializes the exception with a descriptive message and optionally an error code.

            :param message: Error description.
            :param code: Error code (optional).
        """
        self.message = message
        self.code = code
        super().__init__(message)

    def __str__(self):
        if self.code is not None:
            return f"[Error {self.code}] {self.message}"
        return self.message
