from zotasdk import MGClient
from zotasdk.mg_requests import MGPayoutRequest

mg_client = MGClient()

example_payout_request = \
    MGPayoutRequest(merchant_order_id="TbbQzewLWwDW6goc",
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

response = mg_client.send_payout_request(example_payout_request)
print(response.is_ok)
