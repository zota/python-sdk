from unittest.mock import MagicMock

from zotapaysdk.testing_tools import MockResponse
from zotapaysdk.mg_requests import MGOrderStatusRequest


def test_mg_order_status_response_ok(monkeypatch, mg_client_myr_sa, example_deposit_payload,
                                     order_status_check_response_ok_payload):

    order_status_check = MGOrderStatusRequest(order_id="justatestid", merchant_order_id="justatestid")

    mock_response_ok = MockResponse(code=200, payload=order_status_check_response_ok_payload)

    # Mock the request sending method to return the mock payload
    mg_client_myr_sa._send_request = MagicMock(return_value=mock_response_ok)
    order_status_response = mg_client_myr_sa.send_order_status_request(order_status_check)

    mock_response_data = order_status_check_response_ok_payload.get("data")

    assert order_status_response.raw_response is not None
    assert order_status_response.merchant_order_id == \
        mock_response_data.get(order_status_response.Fields.MERCHANT_ORDER_ID)
    assert order_status_response.order_id == mock_response_data.get(order_status_response.Fields.ORDER_ID)
    assert order_status_response.customer_email == mock_response_data.get(order_status_response.Fields.CUSTOMER_EMAIL)
    assert order_status_response.custom_param == mock_response_data.get(order_status_response.Fields.CUSTOM_PARAM)
    assert order_status_response.request == mock_response_data.get(order_status_response.Fields.REQUEST)
    assert order_status_response.status == mock_response_data.get(order_status_response.Fields.STATUS)
    assert order_status_response.amount == mock_response_data.get(order_status_response.Fields.AMOUNT)
    assert order_status_response.currency == mock_response_data.get(order_status_response.Fields.CURRENCY)
    assert order_status_response.processor_transaction_id == \
        mock_response_data.get(order_status_response.Fields.PROCESSOR_TRANSACTION_ID)


def test_mg_order_status_response_nok(monkeypatch, mg_client_myr_sa, example_deposit_payload,
                                      order_status_check_response_nok_payload):
    order_status_check = MGOrderStatusRequest(order_id="justatestid", merchant_order_id="justatestid")

    mock_response_nok = MockResponse(code=400, payload=order_status_check_response_nok_payload)

    # Mock the request sending method to return the mock payload
    mg_client_myr_sa._send_request = MagicMock(return_value=mock_response_nok)
    order_status_response = mg_client_myr_sa.send_order_status_request(order_status_check)

    mock_response_data = order_status_check_response_nok_payload
    assert order_status_response.raw_response is not None
    assert order_status_response.error_message == mock_response_data.get(order_status_response.Fields.MESSAGE)

