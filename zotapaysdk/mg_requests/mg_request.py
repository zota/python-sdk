from zotapaysdk.mg_requests.objects import ArgRequestPair, MGRequestParam


class MGRequest:
    """
    Base class for all requests to against the ZotaPay API.
    """
    class CommonRequestParameters:
        """
        Define all common request fields.
        """
        MERCHANT_ORDER_ID = ArgRequestPair("merchant_order_id", "merchantOrderID")
        MERCHANT_ORDER_DESC = ArgRequestPair("merchant_order_desc", "merchantOrderDesc")
        ORDER_AMOUNT = ArgRequestPair("order_amount", "orderAmount")
        ORDER_CURRENCY = ArgRequestPair("order_currency", "orderCurrency")
        CUSTOMER_EMAIL = ArgRequestPair("customer_email", "customerEmail")
        CUSTOMER_FIRST_NAME = ArgRequestPair("customer_first_name", "customerFirstName")
        CUSTOMER_LAST_NAME = ArgRequestPair("customer_last_name", "customerLastName")
        CUSTOM_PARAM = ArgRequestPair("custom_param", "customParam")
        SIGNATURE = ArgRequestPair("signature", "signature")
        CALLBACK_URL = ArgRequestPair("callback_url", "callbackUrl")

    class DepositRequestParameters(CommonRequestParameters):
        """
        Defines all specific fields for the general Deposit Request
        """
        CUSTOMER_ADDRESS = ArgRequestPair("customer_address", "customerAddress")
        CUSTOMER_COUNTRY_CODE = ArgRequestPair("customer_country_code", "customerCountryCode")
        CUSTOMER_CITY = ArgRequestPair("customer_city", "customerCity")
        CUSTOMER_STATE = ArgRequestPair("customer_state", "customerState")
        CUSTOMER_ZIP_CODE = ArgRequestPair("customer_zip_code", "customerZipCode")
        CUSTOMER_PHONE = ArgRequestPair("customer_phone", "customerPhone")
        CUSTOMER_IP = ArgRequestPair("customer_ip", "customerIP")
        CUSTOMER_BANK_CODE = ArgRequestPair("customer_bank_code", "customerBankCode")
        REDIRECT_URL = ArgRequestPair("redirect_url", "redirectUrl")
        CHECKOUT_URL = ArgRequestPair("checkout_url", "checkoutUrl")
        LANGUAGE = ArgRequestPair("language", "language")

        @staticmethod
        def get_arg_names():
            """
            Returns the argument names for all fields that are used to send a deposit.
            Used for testing purposes mainly.
            Returns:

            """
            # Signature needs to be omitted as it is not a selectable field
            _omit = [MGRequest.CommonRequestParameters.SIGNATURE]
            return [
                v.arg_name for
                k, v in MGRequest.DepositRequestParameters.__dict__.items()
                if k.isupper() and v not in _omit
            ]

    class PayoutRequestParameters(CommonRequestParameters):
        """
        Defines all specific fields required for a Payout Request
        """

        CUSTOMER_PHONE = ArgRequestPair("customer_phone",
                                        "customerPhone")
        CUSTOMER_IP = ArgRequestPair("customer_ip",
                                     "customerIP")
        CUSTOMER_BANK_CODE = ArgRequestPair("customer_bank_code", "customerBankCode")
        CUSTOMER_BANK_ACCOUNT_NUMBER = ArgRequestPair("customer_bank_account_number",
                                                      "customerBankAccountNumber")
        CUSTOMER_BANK_ACCOUNT_NAME = ArgRequestPair("customer_bank_account_name",
                                                    "customerBankAccountName")
        CUSTOMER_BANK_BRANCH = ArgRequestPair("customer_bank_branch",
                                              "customerBankBranch")
        CUSTOMER_BANK_ADDRESS = ArgRequestPair("customer_bank_address",
                                               "customerBankAddress")
        CUSTOMER_BANK_ZIP_CODE = ArgRequestPair("customer_bank_zip_code",
                                                "customerBankZipCode")
        CUSTOMER_BANK_ROUTING_NUMBER = ArgRequestPair("customer_bank_routing_number",
                                                      "customerBankRoutingNumber")
        CUSTOMER_BANK_PROVINCE = ArgRequestPair("customer_bank_province",
                                                "customerBankProvince")
        CUSTOMER_BANK_AREA = ArgRequestPair("customer_bank_area",
                                            "customerBankArea")
        REDIRECT_URL = ArgRequestPair("redirect_url", "redirectUrl")

        @staticmethod
        def get_arg_names():
            """
            Returns the argument names for all fields that are used to send a deposit.
            Used for testing purposes mainly.

            Returns:

            """
            # Signature needs to be omitted as it is not a selectable field
            _omit = [MGRequest.CommonRequestParameters.SIGNATURE]
            return [
                v.arg_name
                for k, v in MGRequest.PayoutRequestParameters.__dict__.items()
                if k.isupper() and v not in _omit
            ]

    class CardDepositRequestParameters:
        """
        Defines all additional fields required for a Credit Card Deposit Request
        """
        CARD_NUMBER = ArgRequestPair("card_number", "cardNumber")
        CARD_HOLDER_NAME = ArgRequestPair("card_holder_name", "cardHolderName")
        CARD_EXPIRATION_MONTH = ArgRequestPair("card_expiration_month", "cardExpirationMonth")
        CARD_EXPIRATION_YEAR = ArgRequestPair("card_expiration_year", "cardExpirationYear")
        CARD_CVV = ArgRequestPair("card_cvv", "cardCvv")

        @staticmethod
        def get_arg_names():
            """
            Returns the argument names for all fields that are used to send a credit card deposit.
            Used for testing purposes mainly.

            Returns:

            """
            _omit = []
            general_deposit_fields = MGRequest.DepositRequestParameters.get_arg_names()
            cc_fields = [
                v.arg_name
                for k, v in MGRequest.CardDepositRequestParameters.__dict__.items()
                if k.isupper() and v not in _omit
            ]
            return general_deposit_fields + cc_fields

    class OrderStatusRequestParameters:
        """
        Defines all fields for the Order Status Request
        """
        MERCHANT_ID = ArgRequestPair("merchant_id", "merchantId")
        MERCHANT_ORDER_ID = ArgRequestPair("merchant_order_id", "merchantOrderId")
        ORDER_ID = ArgRequestPair("order_id", "orderId")
        TIMESTAMP = ArgRequestPair("timestamp", "timestamp")
        SIGNATURE = ArgRequestPair("signature", "signature")

    def _extra_validations(self):
        """
        Override this method to add any additional validations that
        require access to multiple properties.

        Returns:

        """
        return True, ""

    def validate(self):
        """
        Goes over all the instance properties and calls the _validate() method
        on the MGRequestParams instances.

        :return: A tuple of the type <Passed Validation Boolean, Validation Errors List>
        """
        failed_validations = []
        for var_name in self.__dict__:
            attribute = getattr(self, var_name)
            if type(attribute) != MGRequestParam:
                continue

            if attribute.required:
                result, result_msg = attribute.validate()
                if not result:
                    failed_validations.append(result_msg)

        extra_validation, extra_validation_fail_reason = self._extra_validations()

        if not extra_validation:
            failed_validations.append(extra_validation_fail_reason)

        return (False, failed_validations) if failed_validations else (True, failed_validations)

    def to_signed_payload(self, signature, **kwargs):
        """
        Needs to be overwritten.

        Args:
            signature:

        Returns:

        """
        payload = {}
        for _, value in self.__dict__.items():
            if isinstance(value, MGRequestParam):
                payload[value.param_name] = value.param_value
        payload[MGRequest.PayoutRequestParameters.SIGNATURE.request_param_name] = signature
        return payload
