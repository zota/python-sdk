from zotasdk.mg_requests import MGDepositRequest
from zotasdk.client import MGClient
from zotasdk.mg_requests import MGCardDepositRequest

client = MGClient()

example_deposit_request_with_kwargs = MGDepositRequest(
    merchant_order_id="QvE8dZshpKhaOmHY",
    merchant_order_desc="Test order",
    order_amount="500.00",
    order_currency="THB",
    customer_email="customer@email-address.com",
    customer_first_name="John",
    customer_last_name="Doe",
    customer_address="5/5 Moo 5 Thong Nai Pan Noi Beach, Baan Tai, Koh Phangan",
    customer_country_code="TH",
    customer_city="Surat Thani",
    customer_zip_code="84280",
    customer_phone="+66-77999110",
    customer_ip="103.106.8.104",
    redirect_url="https://www.example-merchant.com/payment-return/",
    callback_url="https://www.example-merchant.com/payment-callback/",
    custom_param="{\"UserId\": \"e139b447\"}",
    checkout_url="https://www.example-merchant.com/account/deposit/?uid=e139b447",
)

example_deposit_request = MGDepositRequest(). \
    set_merchant_order_id("QvE8dZshpKhaOmHY"). \
    set_merchant_order_desc("Test order"). \
    set_order_amount("500"). \
    set_order_currency("USD"). \
    set_customer_email("test@test.com"). \
    set_customer_first_name("John"). \
    set_customer_last_name("Doe"). \
    set_customer_address("5/5 Moo 5 Thong Nai Pan Noi Beach, Baan Tai, Koh Phangan"). \
    set_customer_country_code("TH"). \
    set_customer_city("Surat Thani"). \
    set_customer_zip_code("84280"). \
    set_customer_phone("+66-66006600"). \
    set_customer_ip("103.106.8.104"). \
    set_redirect_url("https://www.example-merchant.com/payment-return/"). \
    set_callback_url("https://www.example-merchant.com/payment-callback/"). \
    set_custom_param("{\"UserId\": \"e139b447\"}"). \
    set_checkout_url("https://www.example-merchant.com/account/deposit/?uid=e139b447")


resp = client.send_deposit_request(example_deposit_request)
print("Deposit Request is " + str(resp.is_ok))

example_cc_deposit_request = MGCardDepositRequest(
    merchant_order_id="QvE8dZshpKhaOmHY",
    merchant_order_desc="Test order",
    order_amount="500.00",
    order_currency="THB",
    customer_email="customer@email-address.com",
    customer_first_name="John",
    customer_last_name="Doe",
    customer_address="5/5 Moo 5 Thong Nai Pan Noi Beach, Baan Tai, Koh Phangan",
    customer_country_code="TH",
    customer_city="Surat Thani",
    customer_zip_code="84280",
    customer_phone="+66-77999110",
    customer_ip="103.106.8.104",
    redirect_url="https://www.example-merchant.com/payment-return/",
    callback_url="https://www.example-merchant.com/payment-callback/",
    custom_param="{\"UserId\": \"e139b447\"}",
    checkout_url="https://www.example-merchant.com/account/deposit/?uid=e139b447",
    # CC PARAMS HERE
    card_number="3453789023457890",
    card_holder_name="John Doe",
    card_expiration_month="08",
    card_expiration_year="2027",
    card_cvv="123"
)