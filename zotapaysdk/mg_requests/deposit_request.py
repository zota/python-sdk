"""
Definition of the Deposit Request object.
"""
from zotapaysdk.mg_requests.mg_request import MGRequest
from zotapaysdk.mg_requests.objects import MGRequestParam


class MGDepositRequest(MGRequest):
    # pylint: disable=too-many-instance-attributes
    # pylint: disable=too-many-public-methods
    # pylint: disable=missing-function-docstring
    """
    Class containing all the parameters and logic for creating a non-CC
    deposit request through the Zotapay API SDK.
    """

    def __init__(self, **kwargs):  # pylint: disable=too-many-instance-attributes
        """
        See https://doc.zotapay.com/deposit/1.0/?python#deposit-request for more info.


        :param merchant_order_id:
            Merchant-defined unique order identifier
        :param merchant_order_desc:
            Brief order description
        :param order_amount:
            Amount to be charged, must be specified with delimiter,
            e.g. 1.50 for USD is 1 dollar and 50 cents
        :param order_currency:
            Currency to be charged in, three-letter ISO 4217 currency code.
        :param customer_email:
            End user email address
        :param customer_first_name:
            End user first name
        :param customer_last_name:
            End user last name
        :param customer_address:
            End user address
        :param customer_country_code:
            End user country, two-letter ISO 3166-1 Alpha-2 country code.
        :param customer_city:
            End user city
        :param customer_state:
            Required for US, CA and AU countries.
            End user state/province, two-letter state code.
        :param customer_zip_code:
            End user postal code
        :param customer_phone:
            End user full international telephone number, including country code
        :param customer_ip:
            End user IPv4/IPv6 address
        :param customer_bank_code:
            End user bank code
        :param redirect_url:
            URL for end user redirection upon transaction completion.
        :param callback_url:
            URL the order status will be sent to this URL/
        :param checkout_url:
            The original URL where the user started the deposit (a URL in Merchants' website)
        :param custom_param:
            Merchant-defined optional custom parameter
        :param language:
            Preferred payment form language (ISO 639-1 code)

        """
        self._merchant_order_id = \
            MGRequestParam(self.DepositRequestParameters.MERCHANT_ORDER_ID.request_param_name,
                           kwargs.get(
                               self.DepositRequestParameters.MERCHANT_ORDER_ID.arg_name,
                               None),
                           max_size=128,
                           required=True)

        self._merchant_order_desc = \
            MGRequestParam(self.DepositRequestParameters.MERCHANT_ORDER_DESC.request_param_name,
                           kwargs.get(
                               self.DepositRequestParameters.MERCHANT_ORDER_DESC.arg_name,
                               None),
                           max_size=128,
                           required=True)

        self._order_amount = \
            MGRequestParam(self.DepositRequestParameters.ORDER_AMOUNT.request_param_name,
                           kwargs.get(
                               self.DepositRequestParameters.ORDER_AMOUNT.arg_name,
                               None),
                           max_size=12,
                           required=True)

        self._order_currency = \
            MGRequestParam(self.DepositRequestParameters.ORDER_CURRENCY.request_param_name,
                           kwargs.get(
                               self.DepositRequestParameters.ORDER_CURRENCY.arg_name,
                               None),
                           max_size=3,
                           required=True)

        self._customer_email = \
            MGRequestParam(self.DepositRequestParameters.CUSTOMER_EMAIL.request_param_name,
                           kwargs.get(
                               self.DepositRequestParameters.CUSTOMER_EMAIL.arg_name,
                               None),
                           max_size=50,
                           required=True)

        self._customer_first_name = \
            MGRequestParam(self.DepositRequestParameters.CUSTOMER_FIRST_NAME.request_param_name,
                           kwargs.get(
                               self.DepositRequestParameters.CUSTOMER_FIRST_NAME.arg_name,
                               None),
                           max_size=50,
                           required=True)

        self._customer_last_name = \
            MGRequestParam(self.DepositRequestParameters.CUSTOMER_LAST_NAME.request_param_name,
                           kwargs.get(
                               self.DepositRequestParameters.CUSTOMER_LAST_NAME.arg_name,
                               None),
                           max_size=50,
                           required=True)

        self._customer_address = \
            MGRequestParam(self.DepositRequestParameters.CUSTOMER_ADDRESS.request_param_name,
                           kwargs.get(
                               self.DepositRequestParameters.CUSTOMER_ADDRESS.arg_name,
                               None),
                           max_size=50,
                           required=True)

        self._customer_country_code = \
            MGRequestParam(self.DepositRequestParameters.CUSTOMER_COUNTRY_CODE.request_param_name,
                           kwargs.get(
                               self.DepositRequestParameters.CUSTOMER_COUNTRY_CODE.arg_name,
                               None),
                           max_size=2,
                           required=True)

        self._customer_city = \
            MGRequestParam(self.DepositRequestParameters.CUSTOMER_CITY.request_param_name,
                           kwargs.get(
                               self.DepositRequestParameters.CUSTOMER_CITY.arg_name,
                               None),
                           max_size=50,
                           required=True)

        self._customer_state = \
            MGRequestParam(self.DepositRequestParameters.CUSTOMER_STATE.request_param_name,
                           kwargs.get(
                               self.DepositRequestParameters.CUSTOMER_STATE.arg_name,
                               None),
                           max_size=3,
                           required=False)

        self._customer_zip_code = \
            MGRequestParam(self.DepositRequestParameters.CUSTOMER_ZIP_CODE.request_param_name,
                           kwargs.get(
                               self.DepositRequestParameters.CUSTOMER_ZIP_CODE.arg_name,
                               None),
                           max_size=10,
                           required=True)

        self._customer_phone = \
            MGRequestParam(self.DepositRequestParameters.CUSTOMER_PHONE.request_param_name,
                           kwargs.get(
                               self.DepositRequestParameters.CUSTOMER_PHONE.arg_name,
                               None),
                           max_size=15,
                           required=True)

        self._customer_ip = \
            MGRequestParam(self.DepositRequestParameters.CUSTOMER_IP.request_param_name,
                           kwargs.get(
                               self.DepositRequestParameters.CUSTOMER_IP.arg_name,
                               None),
                           max_size=20,
                           required=True)

        self._customer_bank_code = \
            MGRequestParam(self.DepositRequestParameters.CUSTOMER_BANK_CODE.request_param_name,
                           kwargs.get(
                               self.DepositRequestParameters.CUSTOMER_BANK_CODE.arg_name,
                               None),
                           max_size=8,
                           required=False)

        self._redirect_url = \
            MGRequestParam(self.DepositRequestParameters.REDIRECT_URL.request_param_name,
                           kwargs.get(
                               self.DepositRequestParameters.REDIRECT_URL.arg_name,
                               None),
                           max_size=128,
                           required=True)

        self._callback_url = \
            MGRequestParam(self.DepositRequestParameters.CALLBACK_URL.request_param_name,
                           kwargs.get(
                               self.DepositRequestParameters.CALLBACK_URL.arg_name,
                               None),
                           max_size=128,
                           required=False)

        self._checkout_url = \
            MGRequestParam(self.DepositRequestParameters.CHECKOUT_URL.request_param_name,
                           kwargs.get(self.DepositRequestParameters.CHECKOUT_URL.arg_name, None),
                           max_size=128,
                           required=True)

        self._custom_param = \
            MGRequestParam(self.DepositRequestParameters.CUSTOM_PARAM.request_param_name,
                           kwargs.get(self.DepositRequestParameters.CUSTOM_PARAM.arg_name, None),
                           max_size=128,
                           required=False)

        self._language = \
            MGRequestParam(self.DepositRequestParameters.LANGUAGE.request_param_name,
                           kwargs.get(self.DepositRequestParameters.LANGUAGE.arg_name, None),
                           max_size=2,
                           required=False)

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
    def customer_address(self):
        return self._customer_address.param_value

    def set_customer_address(self, value):
        self._customer_address.set_value(value)
        return self

    @property
    def customer_country_code(self):
        return self._customer_country_code.param_value

    def set_customer_country_code(self, value):
        self._customer_country_code.set_value(value)
        return self

    @property
    def customer_city(self):
        return self._customer_city.param_value

    def set_customer_city(self, value):
        self._customer_city.set_value(value)
        return self

    @property
    def customer_state(self):
        return self._customer_state.param_value

    def set_customer_state(self, value):
        self._customer_state.set_value(value)
        return self

    @property
    def customer_zip_code(self):
        return self._customer_zip_code.param_value

    def set_customer_zip_code(self, value):
        self._customer_zip_code.set_value(value)
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
    def redirect_url(self):
        return self._redirect_url.param_value

    def set_redirect_url(self, value):
        self._redirect_url.set_value(value)
        return self

    @property
    def callback_url(self):
        return self._callback_url.param_value

    def set_callback_url(self, value):
        self._callback_url.set_value(value)
        return self

    @property
    def checkout_url(self):
        return self._checkout_url.param_value

    def set_checkout_url(self, value):
        self._checkout_url.set_value(value)
        return self

    @property
    def custom_param(self):
        return self._custom_param.param_value

    def set_custom_param(self, value):
        self._custom_param.set_value(value)
        return self

    @property
    def language(self):
        return self._language.param_value

    def set_language(self, value):
        self._language.set_value(value)
        return self

    def to_signed_payload(self, signature, **kwargs):
        payload = {}
        for _, value in self.__dict__.items():
            if isinstance(value, MGRequestParam):
                payload[value.param_name] = value.param_value
        payload[MGRequest.DepositRequestParameters.SIGNATURE.request_param_name] = signature
        return payload

    def _extra_validations(self):
        if self.customer_country_code in ["US", "CA", "AU"] and self.customer_state is None:
            return False, "State is required when country is {}".\
                format(str(self.customer_country_code))
        return True, ""
