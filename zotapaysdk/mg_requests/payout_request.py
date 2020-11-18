from zotapaysdk.mg_requests.objects import MGRequestParam
from zotapaysdk.mg_requests.mg_request import MGRequest


class MGPayoutRequest(MGRequest):
    # pylint: disable=missing-function-docstring
    def __init__(self, **kwargs):
        self._merchant_order_id = \
            MGRequestParam(self.PayoutRequestParameters.MERCHANT_ORDER_ID.request_param_name,
                           kwargs.get(
                               self.PayoutRequestParameters.MERCHANT_ORDER_ID.arg_name,
                               None),
                           max_size=128,
                           required=True)

        self._merchant_order_desc = \
            MGRequestParam(self.PayoutRequestParameters.MERCHANT_ORDER_DESC.request_param_name,
                           kwargs.get(self.PayoutRequestParameters.MERCHANT_ORDER_DESC.arg_name,
                                      None),
                           max_size=128,
                           required=True)

        self._order_amount = \
            MGRequestParam(self.PayoutRequestParameters.ORDER_AMOUNT.request_param_name,
                           kwargs.get(self.PayoutRequestParameters.ORDER_AMOUNT.arg_name,
                                      None),
                           max_size=12,
                           required=True)

        self._order_currency = \
            MGRequestParam(self.PayoutRequestParameters.ORDER_CURRENCY.request_param_name,
                           kwargs.get(self.PayoutRequestParameters.ORDER_CURRENCY.arg_name,
                                      None),
                           max_size=3,
                           required=True)

        self._customer_email = \
            MGRequestParam(self.PayoutRequestParameters.CUSTOMER_EMAIL.request_param_name,
                           kwargs.get(self.PayoutRequestParameters.CUSTOMER_EMAIL.arg_name,
                                      None),
                           max_size=50,
                           required=False)

        self._customer_first_name = \
            MGRequestParam(self.PayoutRequestParameters.CUSTOMER_FIRST_NAME.request_param_name,
                           kwargs.get(
                               self.PayoutRequestParameters.CUSTOMER_FIRST_NAME.arg_name,
                               None),
                           max_size=50,
                           required=True)

        self._customer_last_name = \
            MGRequestParam(self.PayoutRequestParameters.CUSTOMER_LAST_NAME.request_param_name,
                           kwargs.get(
                               self.PayoutRequestParameters.CUSTOMER_LAST_NAME.arg_name,
                               None),
                           max_size=50,
                           required=True)

        self._customer_phone = \
            MGRequestParam(self.PayoutRequestParameters.CUSTOMER_PHONE.request_param_name,
                           kwargs.get(
                               self.PayoutRequestParameters.CUSTOMER_PHONE.arg_name,
                               None),
                           max_size=15,
                           required=True)

        self._customer_ip = \
            MGRequestParam(self.PayoutRequestParameters.CUSTOMER_IP.request_param_name,
                           kwargs.get(
                               self.PayoutRequestParameters.CUSTOMER_IP.arg_name,
                               None),
                           max_size=20,
                           required=True)

        self._customer_bank_code = \
            MGRequestParam(self.PayoutRequestParameters.CUSTOMER_BANK_CODE.request_param_name,
                           kwargs.get(self.PayoutRequestParameters.CUSTOMER_BANK_CODE.arg_name,
                                      None),
                           max_size=8,
                           required=False)

        self._customer_bank_account_number = \
            MGRequestParam(
                self.PayoutRequestParameters.CUSTOMER_BANK_ACCOUNT_NUMBER.request_param_name,
                kwargs.get(self.PayoutRequestParameters.CUSTOMER_BANK_ACCOUNT_NUMBER.arg_name,
                           None),
                max_size=15,
                required=True)

        self._customer_bank_account_name = \
            MGRequestParam(self.PayoutRequestParameters.CUSTOMER_BANK_ACCOUNT_NAME.request_param_name,
                           kwargs.get(self.PayoutRequestParameters.CUSTOMER_BANK_ACCOUNT_NAME.arg_name,
                                      None),
                           max_size=128,
                           required=True)

        self._customer_bank_branch = \
            MGRequestParam(self.PayoutRequestParameters.CUSTOMER_BANK_BRANCH.request_param_name,
                           kwargs.get(self.PayoutRequestParameters.CUSTOMER_BANK_BRANCH.arg_name,
                                      None),
                           max_size=128,
                           required=False)

        self._customer_bank_address = \
            MGRequestParam(self.PayoutRequestParameters.CUSTOMER_BANK_ADDRESS.request_param_name,
                           kwargs.get(self.PayoutRequestParameters.CUSTOMER_BANK_ADDRESS.arg_name,
                                      None),
                           max_size=128,
                           required=False)

        self._customer_bank_zip_code = \
            MGRequestParam(self.PayoutRequestParameters.CUSTOMER_BANK_ZIP_CODE.request_param_name,
                           kwargs.get(self.PayoutRequestParameters.CUSTOMER_BANK_ZIP_CODE.arg_name,
                                      None),
                           max_size=15,
                           required=False)

        self._customer_bank_routing_number = \
            MGRequestParam(self.PayoutRequestParameters.CUSTOMER_BANK_ROUTING_NUMBER.request_param_name,
                           kwargs.get(self.PayoutRequestParameters.CUSTOMER_BANK_ROUTING_NUMBER.arg_name,
                                      None),
                           max_size=16,
                           required=False)

        self._customer_bank_province = \
            MGRequestParam(self.PayoutRequestParameters.CUSTOMER_BANK_PROVINCE.request_param_name,
                           kwargs.get(self.PayoutRequestParameters.CUSTOMER_BANK_PROVINCE.arg_name,
                                      None),
                           max_size=64,
                           required=False)

        self._customer_bank_area = \
            MGRequestParam(self.PayoutRequestParameters.CUSTOMER_BANK_AREA.request_param_name,
                           kwargs.get(self.PayoutRequestParameters.CUSTOMER_BANK_AREA.arg_name,
                                      None),
                           max_size=64,
                           required=False)

        self._callback_url = \
            MGRequestParam(self.PayoutRequestParameters.CALLBACK_URL.request_param_name,
                           kwargs.get(
                               self.PayoutRequestParameters.CALLBACK_URL.arg_name,
                               None),
                           max_size=128,
                           required=False)

        self._custom_param = \
            MGRequestParam(self.PayoutRequestParameters.CUSTOM_PARAM.request_param_name,
                           kwargs.get(self.PayoutRequestParameters.CUSTOM_PARAM.arg_name,
                                      None),
                           max_size=128,
                           required=False)

        self._redirect_url = \
            MGRequestParam(self.PayoutRequestParameters.REDIRECT_URL.request_param_name,
                           kwargs.get(self.PayoutRequestParameters.REDIRECT_URL.arg_name,
                                      None),
                           max_size=128,
                           required=True)

    @property
    def merchant_order_id(self):
        return self._merchant_order_id.param_value

    def set_merchant_order_id(self, value):
        self._merchant_order_id.set_value(value)
        return self

    @property
    def merchant_order_desc(self):
        return self._merchant_order_desc.param_value

    def set_merchant_order_desc(self, value):
        self._merchant_order_desc.set_value(value)
        return self

    @property
    def order_amount(self):
        return self._order_amount.param_value

    def set_order_amount(self, value):
        self._order_amount.set_value(value)
        return self

    @property
    def order_currency(self):
        return self._order_currency.param_value

    def set_order_currency(self, value):
        self._order_currency.set_value(value)
        return self

    @property
    def customer_email(self):
        return self._customer_email.param_value

    def set_customer_email(self, value):
        self._customer_email.set_value(value)
        return self

    @property
    def customer_first_name(self):
        return self._customer_first_name.param_value

    def set_customer_first_name(self, value):
        self._customer_first_name.set_value(value)
        return self

    @property
    def customer_last_name(self):
        return self._customer_last_name.param_value

    def set_customer_last_name(self, value):
        self._customer_last_name.set_value(value)
        return self

    @property
    def customer_phone(self):
        return self._customer_phone.param_value

    def set_customer_phone(self, value):
        self._customer_phone.set_value(value)
        return self

    @property
    def customer_ip(self):
        return self._customer_ip.param_value

    def set_customer_ip(self, value):
        self._customer_ip.set_value(value)
        return self

    @property
    def customer_bank_code(self):
        return self._customer_bank_code.param_value

    def set_customer_bank_code(self, value):
        self._customer_bank_code.set_value(value)
        return self

    @property
    def customer_bank_account_number(self):
        return self._customer_bank_account_number.param_value

    def set_customer_bank_account_number(self, value):
        self._customer_bank_account_number.set_value(value)
        return self

    @property
    def customer_bank_account_name(self):
        return self._customer_bank_account_name.param_value

    def set_customer_bank_account_name(self, value):
        self._customer_bank_account_name.set_value(value)
        return self

    @property
    def customer_bank_branch(self):
        return self._customer_bank_branch.param_value

    def set_customer_bank_branch(self, value):
        self._customer_bank_branch.set_value(value)
        return self

    @property
    def customer_bank_address(self):
        return self._customer_bank_address.param_value

    def set_customer_bank_address(self, value):
        self._customer_bank_address.set_value(value)
        return self

    @property
    def customer_bank_zip_code(self):
        return self._customer_bank_zip_code.param_value

    def set_customer_bank_zip_code(self, value):
        self._customer_bank_zip_code.set_value(value)
        return self

    @property
    def customer_bank_routing_number(self):
        return self._customer_bank_routing_number.param_value

    def set_customer_bank_routing_number(self, value):
        self._customer_bank_routing_number.set_value(value)
        return self

    @property
    def customer_bank_province(self):
        return self._customer_bank_province.param_value

    def set_customer_bank_province(self, value):
        self._customer_bank_province.set_value(value)
        return self

    @property
    def customer_bank_area(self):
        return self._customer_bank_area.param_value

    def set_customer_bank_area(self, value):
        self._customer_bank_area.set_value(value)
        return self

    @property
    def callback_url(self):
        return self._callback_url.param_value

    def set_callback_url(self, value):
        self._callback_url.set_value(value)
        return self

    @property
    def custom_param(self):
        return self._custom_param.param_value

    def set_custom_param(self, value):
        self._custom_param.set_value(value)
        return self

    @property
    def redirect_url(self):
        return self._redirect_url

    def set_redirect_url(self, value):
        self._redirect_url = value
        return self

    # def to_signed_payload(self, signature):
    #     payload = {}
    #     for _, value in self.__dict__.items():
    #         if isinstance(value, MGRequestParam):
    #             payload[value.param_name] = value.param_value
    #     payload[MGRequest.PayoutRequestParameters.SIGNATURE.request_param_name] = signature
    #     return payload
