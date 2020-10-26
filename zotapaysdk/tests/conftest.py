import pytest

from zotapaysdk.client import MGClient

TEST_MERCHANT_ID = "SDKEXPLORER"
TEST_MERCHANT_SECRET_KEY = "7801a7a3-0e81-481e-8f59-ee0bfef009bb"
MOCK_ENDPOINT_URL = "http://localhost:5000"


@pytest.fixture
def zotapaysdk_test_config():
    pass


class TestProfiles:
    @staticmethod
    def cc_usd():
        return {
            'merchant_id':  TEST_MERCHANT_ID,
            'merchant_secret_key': TEST_MERCHANT_SECRET_KEY,
            'endpoint_id': "503364",
            'request_url': MGClient.SANDBOX_API_URL,
        }

    @staticmethod
    def sa_myr():
        return {
            'merchant_id': TEST_MERCHANT_ID,
            'merchant_secret_key': TEST_MERCHANT_SECRET_KEY,
            'endpoint_id': "503368",
            'request_url': MGClient.SANDBOX_API_URL,
        }

    @staticmethod
    def cc_usd_localhost_mocked():
        return {
            'merchant_id': TEST_MERCHANT_ID,
            'merchant_secret_key': TEST_MERCHANT_SECRET_KEY,
            'endpoint_id': "503364",
            'request_url': MOCK_ENDPOINT_URL,
        }

    @staticmethod
    def sa_myr_localhost_mocked():
        return {
            'merchant_id': TEST_MERCHANT_ID,
            'merchant_secret_key': TEST_MERCHANT_SECRET_KEY,
            'endpoint_id': "503368",
            'request_url': MOCK_ENDPOINT_URL,
        }


@pytest.fixture
def example_deposit_payload():
    example_payload = dict(merchant_order_id='3384ea3b2819447ea1535644be90eb0c',
                           merchant_order_desc='Test order',
                           order_amount='500',
                           order_currency='MYR',
                           customer_email='customer@email-address.com',
                           customer_first_name='John',
                           customer_last_name='Doe',
                           customer_address='5/5 Moo 5 Thong',
                           customer_country_code='TH',
                           customer_city='Surat Thani',
                           customer_zip_code='84280',
                           customer_phone='+66-77999110',
                           customer_ip='103.106.8.104',
                           redirect_url='https://www.example-merchant.com/payment-return/',
                           callback_url='https://www.example-merchant.com/payment-callback/',
                           checkout_url='https://www.example-merchant.com/account/deposit/?uid=e139b447')
    return example_payload


@pytest.fixture
def example_payout_payload():
    example_payload = dict(merchant_order_id="TbbQzewLWwDW6goc",
                           merchant_order_desc="Test order",
                           order_amount="500.00",
                           order_currency="MYR",
                           customer_email="customer@email-address.com",
                           customer_first_name="John",
                           customer_last_name="Doe",
                           customer_phone="+66-77999110",
                           customer_ip="103.106.8.104",
                           callback_url="https://www.example-merchant.com/payout-callback/",
                           customer_bank_code="BBL",
                           customer_bank_account_number="100200",
                           customer_bank_account_name="John Doe",
                           customer_bank_branch="Bank Branch",
                           customer_bank_address="Thong Nai Pan Noi Beach, Baan Tai, Koh Phangan",
                           customer_bank_zip_code="84280",
                           customer_bank_province="Bank Province",
                           customer_bank_area="Bank Area / City",
                           customer_bank_routing_number="000",
                           custom_param="{\"UserId\": \"e139b447\"}",
                           checkout_url="https://www.example-merchant.com/account/withdrawal/?uid=e139b447")
    return example_payload


@pytest.fixture
def mg_client_usd_cc():
    return MGClient(**TestProfiles.cc_usd())


@pytest.fixture
def mg_client_myr_sa():
    return MGClient(**TestProfiles.sa_myr())


@pytest.fixture
def mg_client_usd_cc_mocked():
    return MGClient(**TestProfiles.cc_usd_localhost_mocked())


@pytest.fixture
def mg_client_myr_sa_mocked():
    return MGClient(**TestProfiles.sa_myr_localhost_mocked())


@pytest.fixture
def deposit_request_response_ok_payload():
    return {
        "code": "200",
        "data": {
            "depositUrl": "https://api.zotapay.com/api/v1/deposit/init/8b3a6b89697e8ac8f45d964bcc90c7ba41764acd/",
            "merchantOrderID": "QvE8dZshpKhaOmHY",
            "orderID": "8b3a6b89697e8ac8f45d964bcc90c7ba41764acd"
        }
    }


@pytest.fixture
def card_deposit_request_response_ok_payload():
    return {
        "code": "200",
        "data": {
            "status": "PROCESSING",
            "merchantOrderID": "QvE8dZshpKhaOmHY",
            "orderID": "8b3a6b89697e8ac8f45d964bcc90c7ba41764acd"
        }
    }


@pytest.fixture
def deposit_request_response_nok_payload():
    return {
        "code": "401",
        "message": "unauthorized"
    }


@pytest.fixture
def order_status_check_response_ok_payload():
    return {'code': "200", 'data': {
        "type": "SALE",
        "status": "PROCESSING",
        "errorMessage": "",
        "endpointID": "1050",
        "processorTransactionID": "",
        "orderID": "8b3a6b89697e8ac8f45d964bcc90c7ba41764acd",
        "merchantOrderID": "QvE8dZshpKhaOmHY",
        "amount": "500.00",
        "currency": "THB",
        "customerEmail": "customer@email-address.com",
        "customParam": "{\"UserId\": \"e139b447\"}",
        "extraData": "",
        "request": {
            "merchantID": "EXAMPLE-MERCHANT-ID",
            "orderID": "8b3a6b89697e8ac8f45d964bcc90c7ba41764acd",
            "merchantOrderID": "QvE8dZshpKhaOmHY",
            "timestamp": "1564617600"
        }
    }}


@pytest.fixture
def order_status_check_response_nok_payload():
    return {
        "code": "400",
        "message": "timestamp too old"
    }
