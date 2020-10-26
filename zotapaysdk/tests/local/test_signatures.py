from zotapaysdk.mg_requests.payout_request import MGPayoutRequest
from zotapaysdk.mg_requests import MGDepositRequest


def test_mg_deposit_signature(mg_client_myr_sa, example_deposit_payload):
    expected_signature = "e2f97591b19ea8ad9d2421e0bafb333349eca03e94940a91fae68dec891e419c"

    # Create the deposit request
    deposit_request = MGDepositRequest(**example_deposit_payload)

    # Generate the signature
    signature = mg_client_myr_sa._generate_deposit_request_signature(deposit_request=deposit_request)

    assert signature == expected_signature


def test_mg_payout_signature(mg_client_myr_sa, example_payout_payload):
    expected_signature = "6a7394981a9543c2eb963cfbd1847eaf7c635d0e896e31b56d6bcba902717312"
    # d04ccb6a14d2c9e6f566766b8158bc4dd5ab6c3bb964a446da92aa61b882d88b

    payout_request = MGPayoutRequest(**example_payout_payload)

    signature = mg_client_myr_sa._generate_payout_request_signature(payout_request)

    assert signature == expected_signature


# def test_order_status_signature(mg_client_myr_sa):
#     mid = "EXAMPLE-MERCHANT-ID"
#     moid = "QvE8dZshpKhaOmHY"
#     oid = "8b3a6b89697e8ac8f45d964bcc90c7ba41764acd"
#     ts = "1564617600"  # str(int(time.time()))
#
#     client = MGClient(merchant_id=mid, merchant_secret_key="EXAMPLE-SECRET-KEY", endpoint_id="123", request_url="localhost")
#
#     sig = client._generate_order_status_request_signature(
#         MGOrderStatusRequest(
#             **{
#                 MGRequest.OrderStatusRequestParameters.MERCHANT_ORDER_ID.arg_name: moid,
#                 MGRequest.OrderStatusRequestParameters.ORDER_ID.arg_name: oid
#             }
#         ),
#         ts
#     )
#
#     assert sig == "4a01f6cc95e6a7a771afe0e49f59fb572dbadec449f175d978e722b97ee9785d"
