import json
from zotapaysdk.helpers import HTTP_STATUS_OK
from zotapaysdk.mg_requests.response import MGResponse


class MGOrderStatusResponse(MGResponse):
    class Fields:
        TYPE = "type"
        STATUS = "status"
        ERROR_MESSAGE = "errorMessage"
        PROCESSOR_TRANSACTION_ID = "processorTransactionID"
        ORDER_ID = "orderID"
        MERCHANT_ORDER_ID = "merchantOrderID"
        AMOUNT = "amount"
        CURRENCY = "currency"
        CUSTOMER_EMAIL = "customerEmail"
        CUSTOM_PARAM = "customParam"
        REQUEST = "request"
        MESSAGE = "message"
        DATA = "data"

    def __init__(self, http_response):
        """
        Wrapper around the order status request response from the API.

        Args:
            http_response (requests.Response):
        """
        super().__init__(http_response)

        self._type = None
        self._status = None
        self._error_message = None
        self._processor_transaction_id = None
        self._order_id = None
        self._merchant_order_id = None
        self._amount = None
        self._currency = None
        self._customer_email = None
        self._custom_param = None
        self._request = None

        parsed_response = json.loads(http_response.text)

        if http_response.status_code != HTTP_STATUS_OK:
            self._error_message = parsed_response.get(self.Fields.MESSAGE, "Unavailable message")
        else:
            parsed_response_data = parsed_response.get(self.Fields.DATA, None)
            self._type = parsed_response_data.get(self.Fields.TYPE, None)
            self._status = parsed_response_data.get(self.Fields.STATUS, None)
            self._processor_transaction_id = parsed_response_data.get(
                self.Fields.PROCESSOR_TRANSACTION_ID, None)
            self._order_id = parsed_response_data.get(self.Fields.ORDER_ID, None)
            self._merchant_order_id = parsed_response_data.get(self.Fields.MERCHANT_ORDER_ID, None)
            self._amount = parsed_response_data.get(self.Fields.AMOUNT, None)
            self._currency = parsed_response_data.get(self.Fields.CURRENCY, None)
            self._customer_email = parsed_response_data.get(self.Fields.CUSTOMER_EMAIL, None)
            self._custom_param = parsed_response_data.get(self.Fields.CUSTOM_PARAM, None)
            self._request = parsed_response_data.get(self.Fields.REQUEST, None)

    @property
    def type(self):
        """
        Getter for the type.

        Returns:

        """
        return self._type

    @property
    def status(self):
        """
        Getter for the status.

        Returns:

        """
        return self._status

    @property
    def error_message(self):
        """
        Getter for the actual error message.

        Returns:

        """
        return self._error_message

    @property
    def is_ok(self):
        """
        Flag whether the request went ok or not.

        Returns: True if there is no error else False

        """
        return self._error_message is not None

    @property
    def processor_transaction_id(self):
        """
        Getter for the processor transaction id.

        Returns:

        """
        return self._processor_transaction_id

    @property
    def order_id(self):
        """
        Getter for the order id.

        Returns:

        """
        return self._order_id

    @property
    def merchant_order_id(self):
        """
        Getter for the merchant order id.

        Returns:

        """
        return self._merchant_order_id

    @property
    def amount(self):
        """
        Getter for the amount.

        Returns:

        """
        return self._amount

    @property
    def currency(self):
        """
        Getter for the currency of the order.

        Returns:

        """
        return self._currency

    @property
    def customer_email(self):
        """
        Getter for the customer email.

        Returns:

        """
        return self._customer_email

    @property
    def custom_param(self):
        """
        Getter for the custom parameter passed to the api.

        Returns:

        """
        return self._custom_param

    @property
    def request(self):
        """
        Getter for the raw request as returned.

        Returns:

        """
        return self._request
