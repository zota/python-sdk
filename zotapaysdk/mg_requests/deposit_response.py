"""
Contains Deposit Response class definition.
"""
import json
import requests
from zotapaysdk.helpers import HTTP_STATUS_OK
from zotapaysdk.mg_requests.response import MGResponse


class MGDepositResponse(MGResponse):  # pylint: disable=too-few-public-methods
    """
    Object that wraps around the ZotaPay Deposit Request response.
    """
    class Fields:  # pylint: disable=too-few-public-methods
        """
        Static class containing all the fields that are received from the response 'data' parameter.
        """
        CODE = "code"
        DATA = 'data'
        DEPOSIT_URL = 'depositUrl'
        MERCHANT_ORDER_ID = 'merchantOrderID'
        ORDER_ID = 'orderID'
        MESSAGE = "message"

    def __init__(self, http_response):
        """
        Container class for the deposit request response.

        Example response from the API:

        {
            "code": "200",
            "data": {
                "depositUrl": "<URL>/api/v1/deposit/init/8b3a6b89697e8ac8f45d964bcc90c7ba41764acd/",
                "merchantOrderID": "QvE8dZshpKhaOmHY",
                "orderID": "8b3a6b89697e8ac8f45d964bcc90c7ba41764acd"
            }
        }

        Args:
            http_response (requests.Response): an instance of the raw requests.Response
                as returned when the client calls the ZotaPay API
        """
        super().__init__(http_response)
        # Define all instance variables
        self._merchant_order_id = None
        self._order_id = None
        self._deposit_url = None

        self._is_error = False
        self._error_reason = None

        # Parse the response
        parser_response = json.loads(http_response.text)

        if http_response.status_code != HTTP_STATUS_OK:
            self._is_error = True
            self._error_reason = parser_response.get(self.Fields.MESSAGE, None)
        else:
            response_data = parser_response.get(self.Fields.DATA, None)
            if response_data is not None:
                self._merchant_order_id = response_data.get(self.Fields.MERCHANT_ORDER_ID)
                self._order_id = response_data.get(self.Fields.ORDER_ID)
                self._deposit_url = response_data.get(self.Fields.DEPOSIT_URL)

    @property
    def deposit_url(self):
        """
        Getter for the deposit url.

        Returns:

        """
        return self._deposit_url

    @property
    def merchant_order_id(self):
        """
        Getter for the merchant order id.

        Returns:

        """
        return self._merchant_order_id

    @property
    def order_id(self):
        """
        Getter for the order id.

        Returns:

        """
        return self._order_id

    @property
    def is_ok(self):
        """
        A flag whether the request returned an error or not.

        Returns:

        """
        return not self._is_error

    @property
    def error(self):
        """
        Getter for the actual error if such has occurred.

        Returns:

        """
        return self._error_reason
