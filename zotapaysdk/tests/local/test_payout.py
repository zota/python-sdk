from zotapaysdk.testing_tools import generate_test_payout_w_ok_response, MockResponse, \
    generate_test_payout_w_nok_response
from zotapaysdk.mg_requests.payout_response import MGPayoutResponse
from zotapaysdk.mg_requests.payout_request import MGPayoutRequest


def test_payout_request_object_init(example_payout_payload):
    """
    Test that the constructor of the Payout Request behaves as expected.

    Assumes that naming convention is followed.

    Args:
        example_payout_payload: A test fixture with an example payload

    Returns:

    """
    payout_request = MGPayoutRequest(**example_payout_payload)
    for x in payout_request.__dict__.keys():
        assert getattr(payout_request, x).param_value == example_payout_payload.get(x[1:])

    for x in payout_request.__dict__.keys():
        x = x[1:]
        assert getattr(payout_request, x) == example_payout_payload.get(x)


def test_payout_request_object_build(example_payout_payload):
    payout_request = MGPayoutRequest()
    for x in payout_request.__dict__.keys():
        getattr(payout_request, "set"+x)(example_payout_payload.get(x[1:]))
    for x in payout_request.__dict__.keys():
        assert getattr(payout_request, x).param_value == example_payout_payload.get(x[1:])


def test_payout_response_ok():
    _, ok_response_payload = generate_test_payout_w_ok_response()
    mock_response = MockResponse(code=200, payload=ok_response_payload)
    payout_response = MGPayoutResponse(mock_response)
    assert payout_response.is_ok
    assert payout_response.error is None
    assert payout_response.merchant_order_id == ok_response_payload.get(MGPayoutResponse.Fields.DATA).\
        get(MGPayoutResponse.Fields.MERCHANT_ORDER_ID)
    assert payout_response.order_id == ok_response_payload.get(MGPayoutResponse.Fields.DATA).\
        get(MGPayoutResponse.Fields.ORDER_ID)


def test_payout_response_nok():
    _, nok_response_payload = generate_test_payout_w_nok_response()
    mock_response = MockResponse(code=400, payload=nok_response_payload)
    payout_response = MGPayoutResponse(mock_response)
    assert not payout_response.is_ok