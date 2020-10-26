import requests
from _sha256 import sha256


class MGCallback:
    class CallbackFields:
        TYPE = "type"
        STATUS = "status"
        ERROR_MESSAGE = "errorMessage"
        ENDPOINT_ID = "endpointID"
        PROCESSOR_TRANSACTION_ID = "processorTransactionID"
        ORDER_ID = "orderID"
        MERCHANT_ORDER_ID = "merchantOrderID"
        AMOUNT = "amount"
        CURRENCY = "currency"
        CUSTOMER_EMAIL = "customerEmail"
        CUSTOM_PARAM = "customParam"
        EXTRA_DATA = "extraData"
        ORIGINAL_REQUEST = "originalRequest"
        SIGNATURE = "signature"

    def __init__(self, http_request: requests.Request):
        self._raw_request = http_request

        raw_request_json = self._raw_request.json

        self._type = raw_request_json.get(self.CallbackFields.TYPE, None)
        self._status = raw_request_json.get(self.CallbackFields.STATUS, None)
        self._error_message = raw_request_json.get(self.CallbackFields.ERROR_MESSAGE, None)
        self._endpoint_id = raw_request_json.get(self.CallbackFields.ENDPOINT_ID, None)
        self._processor_transaction_id = raw_request_json.get(self.CallbackFields.PROCESSOR_TRANSACTION_ID, None)
        self._order_id = raw_request_json.get(self.CallbackFields.ORDER_ID, None)
        self._merchant_order_id = raw_request_json.get(self.CallbackFields.MERCHANT_ORDER_ID, None)
        self._amount = raw_request_json.get(self.CallbackFields.AMOUNT, None)
        self._currency = raw_request_json.get(self.CallbackFields.CURRENCY, None)
        self._customer_email = raw_request_json.get(self.CallbackFields.CUSTOMER_EMAIL, None)
        self._custom_param = raw_request_json.get(self.CallbackFields.CUSTOM_PARAM, None)
        self._extra_data = raw_request_json.get(self.CallbackFields.EXTRA_DATA, None)
        self._original_request = raw_request_json.get(self.CallbackFields.ORIGINAL_REQUEST, None)
        self._signature = raw_request_json.get(self.CallbackFields.SIGNATURE)

    def _validate_signature(self, merchant_secret_key):
        """
        Validates whether the signature returned in the callback is OK.

        Args:
            merchant_secret_key: The secret key as provided by ZotaPay

        Returns:
            Boolean whether the signature is verified.
        """
        signature_template = "{endpoint}{oid}{moid}{status}{amt}{email}{secret}"
        signature = signature_template.format(
            **{
                'endpoint': self.endpoint_id,
                'oid': self.order_id,
                'moid': self.merchant_order_id,
                'status': self.status,
                'amt': self.amount,
                'email': self.customer_email,
                'secret': merchant_secret_key
            }
        )

        sig_hash = sha256(signature.encode('utf-8')).hexdigest()
        return sig_hash == self._signature

    @property
    def type(self):
        return self._type

    @property
    def status(self):
        return self._status

    @property
    def error_message(self):
        return self._error_message

    @property
    def endpoint_id(self):
        return self._endpoint_id

    @property
    def processor_transaction_id(self):
        return self._processor_transaction_id

    @property
    def order_id(self):
        return self._order_id

    @property
    def merchant_order_id(self):
        return self._merchant_order_id

    @property
    def amount(self):
        return self._amount

    @property
    def currency(self):
        return self._currency

    @property
    def customer_email(self):
        return self._customer_email

    @property
    def custom_param(self):
        return self._custom_param

    @property
    def extra_data(self):
        return self._extra_data

    @property
    def original_request(self):
        return self._original_request

    @property
    def signature(self):
        return self._signature

    def is_valid(self, merchant_secret_key):
        return self._validate_signature(merchant_secret_key=merchant_secret_key)
