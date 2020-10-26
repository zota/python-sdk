import uuid
import json

from zotapaysdk.mg_requests.payout_response import MGPayoutResponse
from zotapaysdk.mg_requests import MGDepositResponse, MGCardDepositResponse, MGOrderStatusRequest
from zotapaysdk.mg_requests.mg_request import MGRequest


class MockResponse:
    def __init__(self, code, payload):
        """
        Basic mock for the requests.Response class.

        It only has the same attributes as required by the parsing function.
        """
        self.status_code = code
        self.text = json.dumps(payload)


class TestCreditCards:
    """
    Contains all the test cards that can be used against the ZotaPay Sandbox API
    """
    @staticmethod
    def visa_approved_no_3d():
        return {
            MGRequest.CardDepositRequestParameters.CARD_NUMBER.arg_name: "4222222222222222",
            MGRequest.CardDepositRequestParameters.CARD_EXPIRATION_MONTH.arg_name: "11",
            MGRequest.CardDepositRequestParameters.CARD_EXPIRATION_YEAR.arg_name: "2030",
            MGRequest.CardDepositRequestParameters.CARD_HOLDER_NAME.arg_name: "John Doe",
            MGRequest.CardDepositRequestParameters.CARD_CVV.arg_name: "191"
        }

    @staticmethod
    def visa_pending_3d():
        return {
            MGRequest.CardDepositRequestParameters.CARD_NUMBER.arg_name: "4222222222347466",
            MGRequest.CardDepositRequestParameters.CARD_EXPIRATION_MONTH.arg_name: "11",
            MGRequest.CardDepositRequestParameters.CARD_EXPIRATION_YEAR.arg_name: "2030",
            MGRequest.CardDepositRequestParameters.CARD_HOLDER_NAME.arg_name: "John Doe",
            MGRequest.CardDepositRequestParameters.CARD_CVV.arg_name: "191"
        }

    @staticmethod
    def mastercard_approved_no_3d():
        return {
            MGRequest.CardDepositRequestParameters.CARD_NUMBER.arg_name: "5555555555555557",
            MGRequest.CardDepositRequestParameters.CARD_EXPIRATION_MONTH.arg_name: "11",
            MGRequest.CardDepositRequestParameters.CARD_EXPIRATION_YEAR.arg_name: "2030",
            MGRequest.CardDepositRequestParameters.CARD_HOLDER_NAME.arg_name: "John Doe",
            MGRequest.CardDepositRequestParameters.CARD_CVV.arg_name: "191"
        }

    @staticmethod
    def mastercard_pending_3d():
        return {
            MGRequest.CardDepositRequestParameters.CARD_NUMBER.arg_name: "5595883393160089",
            MGRequest.CardDepositRequestParameters.CARD_EXPIRATION_MONTH.arg_name: "11",
            MGRequest.CardDepositRequestParameters.CARD_EXPIRATION_YEAR.arg_name: "2030",
            MGRequest.CardDepositRequestParameters.CARD_HOLDER_NAME.arg_name: "John Doe",
            MGRequest.CardDepositRequestParameters.CARD_CVV.arg_name: "191"
        }

    @staticmethod
    def jcb_approved_no_3d():
        return {
            MGRequest.CardDepositRequestParameters.CARD_NUMBER.arg_name: "3555555555555552",
            MGRequest.CardDepositRequestParameters.CARD_EXPIRATION_MONTH.arg_name: "11",
            MGRequest.CardDepositRequestParameters.CARD_EXPIRATION_YEAR.arg_name: "2030",
            MGRequest.CardDepositRequestParameters.CARD_HOLDER_NAME.arg_name: "John Doe",
            MGRequest.CardDepositRequestParameters.CARD_CVV.arg_name: "191"
        }

    @staticmethod
    def jcb_pending_3d():
        return {
            MGRequest.CardDepositRequestParameters.CARD_NUMBER.arg_name: "3530185156387088",
            MGRequest.CardDepositRequestParameters.CARD_EXPIRATION_MONTH.arg_name: "11",
            MGRequest.CardDepositRequestParameters.CARD_EXPIRATION_YEAR.arg_name: "2030",
            MGRequest.CardDepositRequestParameters.CARD_HOLDER_NAME.arg_name: "John Doe",
            MGRequest.CardDepositRequestParameters.CARD_CVV.arg_name: "191"
        }


def build_random_id():
    return str(uuid.uuid4()).replace("-", "")


def generate_test_order(amount=500, currency="USD", **kwargs):
    deposit_request = {
        MGRequest.DepositRequestParameters.MERCHANT_ORDER_ID.arg_name: build_random_id(),
        MGRequest.DepositRequestParameters.MERCHANT_ORDER_DESC.arg_name: "Test order",
        MGRequest.DepositRequestParameters.ORDER_AMOUNT.arg_name: str(amount),
        MGRequest.DepositRequestParameters.ORDER_CURRENCY.arg_name: str(currency),
        MGRequest.DepositRequestParameters.CUSTOMER_EMAIL.arg_name: "customer@email-address.com",
        MGRequest.DepositRequestParameters.CUSTOMER_FIRST_NAME.arg_name: "John",
        MGRequest.DepositRequestParameters.CUSTOMER_LAST_NAME.arg_name: "Doe",
        MGRequest.DepositRequestParameters.CUSTOMER_ADDRESS.arg_name: "5/5 Moo 5 Thong",
        MGRequest.DepositRequestParameters.CUSTOMER_COUNTRY_CODE.arg_name: "TH",
        MGRequest.DepositRequestParameters.CUSTOMER_CITY.arg_name: "Surat Thani",
        MGRequest.DepositRequestParameters.CUSTOMER_ZIP_CODE.arg_name: "84280",
        MGRequest.DepositRequestParameters.CUSTOMER_PHONE.arg_name: "+66-77999110",
        MGRequest.DepositRequestParameters.CUSTOMER_IP.arg_name: "103.106.8.104",
        MGRequest.DepositRequestParameters.CUSTOMER_STATE.arg_name: "TS",
        MGRequest.DepositRequestParameters.LANGUAGE.arg_name: "en",
        MGRequest.DepositRequestParameters.REDIRECT_URL.arg_name:
            "https://www.example-merchant.com/payment-return/",
        MGRequest.DepositRequestParameters.CALLBACK_URL.arg_name:
            "https://www.example-merchant.com/payment-callback/",
        MGRequest.DepositRequestParameters.CUSTOM_PARAM.arg_name:
            "{\"UserId\": \"e139b447\"}",
        MGRequest.DepositRequestParameters.CHECKOUT_URL.arg_name:
            "https://www.example-merchant.com/account/deposit/?uid=e139b447",
    }

    for k, v in kwargs.items():
        deposit_request[k] = v

    return deposit_request


def generate_test_order_with_ok_response(amount=500, currency="USD", **kwargs):
    deposit_payload = generate_test_order(amount=amount, currency=currency, **kwargs)

    is_card = True if deposit_payload.get(MGRequest.CardDepositRequestParameters.CARD_NUMBER, False) \
        else False

    # Prepare the response
    response_payload = {
        MGDepositResponse.Fields.CODE: "200",
        MGDepositResponse.Fields.DATA: {
            MGDepositResponse.Fields.MERCHANT_ORDER_ID:
                deposit_payload[MGRequest.DepositRequestParameters.MERCHANT_ORDER_ID.arg_name],
            MGDepositResponse.Fields.ORDER_ID: build_random_id()
        }
    }

    if is_card:
        response_payload[MGDepositResponse.Fields.DATA][MGCardDepositResponse.Fields.STATUS] = \
            MGOrderStatusRequest.MGOrderStatus.PROCESSING
    else:
        response_payload[MGDepositResponse.Fields.DATA][MGDepositResponse.Fields.DEPOSIT_URL] = \
            "https://api.zotapay.com/api/v1/deposit/init/8b3a6b89697e8ac8f45d964bcc90c7ba41764acd/"

    return deposit_payload, response_payload


def generate_test_order_with_nok_response(amount=500, currency="USD", **kwargs):
    # TODOcccccchkrvikvtirejrlhhclcrhjijhfldilbftlvrtk

    pass


def generate_test_payout(amount=500, currency="USD", **kwargs):
    """
    Generates a test payout request payload that passes all parameter verifications.

    Args:
        amount:
        currency:
        **kwargs:

    Returns:

    """
    payout_request = {
        MGRequest.PayoutRequestParameters.MERCHANT_ORDER_ID.arg_name: build_random_id(),
        MGRequest.PayoutRequestParameters.MERCHANT_ORDER_DESC.arg_name: "Test Payout",
        MGRequest.PayoutRequestParameters.ORDER_AMOUNT.arg_name: amount,
        MGRequest.PayoutRequestParameters.ORDER_CURRENCY.arg_name: currency,
    }

    customer_email = kwargs.get(MGRequest.PayoutRequestParameters.CUSTOMER_EMAIL.arg_name,
                                None)
    payout_request[MGRequest.PayoutRequestParameters.CUSTOMER_EMAIL.arg_name] = \
        customer_email if customer_email else "customer@email-address.com"

    customer_first_name = kwargs.get(MGRequest.PayoutRequestParameters.CUSTOMER_FIRST_NAME.arg_name,
                                     None)
    payout_request[MGRequest.PayoutRequestParameters.CUSTOMER_FIRST_NAME.arg_name] = \
        customer_first_name if customer_first_name else "John"

    customer_last_name = kwargs.get(MGRequest.PayoutRequestParameters.CUSTOMER_LAST_NAME.arg_name,
                                    None)
    payout_request[MGRequest.PayoutRequestParameters.CUSTOMER_LAST_NAME.arg_name] = \
        customer_last_name if customer_last_name else "Doe"

    customer_phone = kwargs.get(MGRequest.PayoutRequestParameters.CUSTOMER_PHONE.arg_name,
                                None)
    payout_request[MGRequest.PayoutRequestParameters.CUSTOMER_PHONE.arg_name] = \
        customer_phone if customer_phone else "+66-77999110"

    customer_ip = kwargs.get(MGRequest.PayoutRequestParameters.CUSTOMER_IP.arg_name,
                             None)
    payout_request[MGRequest.PayoutRequestParameters.CUSTOMER_IP.arg_name] = \
        customer_ip if customer_ip else "103.106.8.104"

    customer_bank_code = kwargs.get(MGRequest.PayoutRequestParameters.CUSTOMER_BANK_CODE.arg_name,
                                    None)
    payout_request[MGRequest.PayoutRequestParameters.CUSTOMER_BANK_CODE.arg_name] = \
        customer_bank_code if customer_bank_code else "BBL"

    customer_bank_account_number = kwargs.get(MGRequest.PayoutRequestParameters.CUSTOMER_BANK_ACCOUNT_NUMBER.arg_name,
                                              None)
    payout_request[MGRequest.PayoutRequestParameters.CUSTOMER_BANK_ACCOUNT_NUMBER.arg_name] = \
        customer_bank_account_number if customer_bank_account_number else "3678094857345"

    customer_bank_account_name = kwargs.get(MGRequest.PayoutRequestParameters.CUSTOMER_BANK_ACCOUNT_NAME.arg_name,
                                            None)
    payout_request[MGRequest.PayoutRequestParameters.CUSTOMER_BANK_ACCOUNT_NAME.arg_name] = \
        customer_bank_account_name if customer_bank_account_name else "Test Account Name"

    customer_bank_branch = kwargs.get(MGRequest.PayoutRequestParameters.CUSTOMER_BANK_BRANCH.arg_name,
                                      None)
    payout_request[MGRequest.PayoutRequestParameters.CUSTOMER_BANK_BRANCH.arg_name] = \
        customer_bank_branch if customer_bank_branch else "Test Bank Branch"

    customer_bank_address = kwargs.get(MGRequest.PayoutRequestParameters.CUSTOMER_BANK_ADDRESS,
                                       None)
    payout_request[MGRequest.PayoutRequestParameters.CUSTOMER_BANK_ADDRESS.arg_name] = \
        customer_bank_address if customer_bank_address else "12 Test Address Bank"

    customer_bank_zip_code = kwargs.get(MGRequest.PayoutRequestParameters.CUSTOMER_BANK_ZIP_CODE.arg_name,
                                        None)
    payout_request[MGRequest.PayoutRequestParameters.CUSTOMER_BANK_ZIP_CODE.arg_name] = \
        customer_bank_zip_code if customer_bank_zip_code else "9EH 8QU"

    customer_bank_routing_number = kwargs.get(MGRequest.PayoutRequestParameters.CUSTOMER_BANK_ROUTING_NUMBER.arg_name,
                                              None)
    payout_request[MGRequest.PayoutRequestParameters.CUSTOMER_BANK_ROUTING_NUMBER.arg_name] = \
        customer_bank_routing_number if customer_bank_routing_number else "20496793023"

    customer_bank_province = kwargs.get(MGRequest.PayoutRequestParameters.CUSTOMER_BANK_PROVINCE.arg_name,
                                        None)
    payout_request[MGRequest.PayoutRequestParameters.CUSTOMER_BANK_PROVINCE.arg_name] = \
        customer_bank_province if customer_bank_province else "Test Province"

    customer_bank_area = kwargs.get(MGRequest.PayoutRequestParameters.CUSTOMER_BANK_AREA.arg_name,
                                    None)
    payout_request[MGRequest.PayoutRequestParameters.CUSTOMER_BANK_AREA.arg_name] = \
        customer_bank_area if customer_bank_area else "Test Area"

    callback_url = kwargs.get(MGRequest.PayoutRequestParameters.CALLBACK_URL.arg_name,
                              None)
    payout_request[MGRequest.PayoutRequestParameters.CALLBACK_URL.arg_name] = \
        callback_url if callback_url else "https://www.example-merchant.com/payment-callback/"

    custom_param = kwargs.get(MGRequest.PayoutRequestParameters.CUSTOM_PARAM.arg_name,
                              None)
    payout_request[MGRequest.PayoutRequestParameters.CUSTOM_PARAM.arg_name] = \
        custom_param if custom_param else "{\"UserId\": \"e139b447\"}"

    return payout_request


def generate_test_payout_w_ok_response(amount=500, currency="USD", **kwargs):
    """
    Generates a sample payout request payload and an OK response payload.

    Args:
        amount:
        currency:
        **kwargs:

    Returns:
        Two dictionaries
    """
    payout_payload = generate_test_payout(amount=amount, currency=currency, **kwargs)
    response_payload = {
        MGPayoutResponse.Fields.CODE: "200",
        MGPayoutResponse.Fields.DATA: {
            MGPayoutResponse.Fields.MERCHANT_ORDER_ID:
                payout_payload[MGRequest.PayoutRequestParameters.MERCHANT_ORDER_ID.arg_name],
            MGPayoutResponse.Fields.ORDER_ID: "beb3e2e1cf59b0d275984ceaf58cd7f7b4b5b09a"
        }
    }

    return payout_payload , response_payload


def generate_test_payout_w_nok_response(amount=500, currency="USD", **kwargs):
    """
        Generates a sample payout request payload and an not-OK response payload.

        Args:
            amount:
            currency:
            **kwargs:

        Returns:
            Two dictionaries
        """
    payout_payload = generate_test_payout(amount=amount, currency=currency, **kwargs)
    response_payload = {
        MGPayoutResponse.Fields.CODE: "401",
        MGPayoutResponse.Fields.MESSAGE: "unauthorized"
    }
    return payout_payload, response_payload
