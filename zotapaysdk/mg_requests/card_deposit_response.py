# pylint: disable=missing-module-docstring
import json
from zotapaysdk.helpers import HTTP_STATUS_OK
from zotapaysdk.mg_requests.response import MGResponse


class MGCardDepositResponse(MGResponse):
    # pylint: disable=too-few-public-methods
    class Fields:
        DATA = 'data'
        STATUS = 'status'
        MERCHANT_ORDER_ID = 'merchantOrderID'
        ORDER_ID = 'orderID'
        MESSAGE = "message"

    def __init__(self, http_response):
        """
        Wrapper around the request response for credit card deposits.

        Args:
            http_response (requests.Response):
        """
        super().__init__(http_response)

        self._merchant_order_id = None
        self._order_id = None
        self._status = None

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
                self._status = response_data.get(self.Fields.STATUS)

    @property
    def status(self):
        """
        Getter for the status field.

        Returns:

        """
        return self._status

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
        Getter for the ok flag.

        Returns: True if no order else False

        """
        return not self._is_error

    @property
    def error(self):
        """
        Getter for the error.

        Returns: The actual error message.

        """
        return self._error_reason
