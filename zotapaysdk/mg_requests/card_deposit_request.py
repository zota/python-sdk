# pylint: disable=missing-class-docstring
from zotapaysdk.mg_requests import MGDepositRequest
from zotapaysdk.mg_requests.objects import MGRequestParam


class MGCardDepositRequest(MGDepositRequest):
    """
    Class for the card deposit request. Implements all required functionality for sending a Credit Card request.
    """
    def __init__(self, **kwargs):
        """
        Class defining all that is necessary for sending a Credit Card Deposit Request.

        See Also https://doc.zotapay.com/deposit/1.0/#card-payment-integration-2

        Args:
            *args:
            **kwargs:
        """
        super().__init__(**kwargs)

        self._card_number = \
            MGRequestParam(
                self.CardDepositRequestParameters.CARD_NUMBER.request_param_name,
                kwargs.get(self.CardDepositRequestParameters.CARD_NUMBER.arg_name, None),
                max_size=16,
                required=True)

        self._card_holder_name = \
            MGRequestParam(
                self.CardDepositRequestParameters.CARD_HOLDER_NAME.request_param_name,
                kwargs.get(self.CardDepositRequestParameters.CARD_HOLDER_NAME.arg_name, None),
                max_size=64,
                required=True)

        self._card_expiration_month = \
            MGRequestParam(
                self.CardDepositRequestParameters.CARD_EXPIRATION_MONTH.request_param_name,
                kwargs.get(self.CardDepositRequestParameters.CARD_EXPIRATION_MONTH.arg_name, None),
                max_size=2,
                required=True)

        self._card_expiration_year = \
            MGRequestParam(
                self.CardDepositRequestParameters.CARD_EXPIRATION_YEAR.request_param_name,
                kwargs.get(self.CardDepositRequestParameters.CARD_EXPIRATION_YEAR.arg_name, None),
                max_size=4,
                required=True)

        self._card_cvv = \
            MGRequestParam(
                self.CardDepositRequestParameters.CARD_CVV.request_param_name,
                kwargs.get(self.CardDepositRequestParameters.CARD_CVV.arg_name, None),
                max_size=4,
                required=True)

    @property
    def card_number(self):
        return self._card_number.param_value

    def set_card_number(self, value):
        self._card_number.set_value(value)
        return self

    @property
    def card_holder_name(self):
        return self._card_holder_name.param_value

    def set_card_holder_name(self, value):
        self._card_holder_name.set_value(value)
        return self

    @property
    def card_expiration_month(self):
        return self._card_expiration_month.param_value

    def set_card_expiration_month(self, value):
        self._card_expiration_month.set_value(value)
        return self

    @property
    def card_expiration_year(self):
        return self._card_expiration_year.param_value

    def set_card_expiration_year(self, value):
        self._card_expiration_year.set_value(value)
        return self

    @property
    def card_cvv(self):
        return self._card_cvv.param_value

    def set_card_cvv(self, value):
        self._card_cvv.set_value(value)
        return self
