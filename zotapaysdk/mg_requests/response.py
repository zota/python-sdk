import requests


class MGResponse:
    def __init__(self, http_response: requests.Response):
        """
        Superclass for all MGResponse type classes. Ensures that all that inherit have the raw response available.

        Args:
            http_response:
        """
        self._raw_response = http_response

    @property
    def raw_response(self):
        return self._raw_response
