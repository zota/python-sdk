import pytest
from zotapaysdk.mg_requests import MGDepositResponse
from zotapaysdk.client import MGClient
from zotapaysdk.urls import MGUrlsFormatter
from zotapaysdk.mg_requests import MGCardDepositResponse
from zotapaysdk.exceptions import MGException
from zotapaysdk.testing_tools import generate_test_order, TestCreditCards, MockResponse, \
    generate_test_order_with_ok_response
from zotapaysdk.mg_requests import MGDepositRequest
from zotapaysdk.mg_requests import MGCardDepositRequest


def test_deposit_ok(httpserver):
    deposit_payload, response_payload = generate_test_order_with_ok_response(500, "MYR")

    client_properties = {
                            'merchant_id': "test_merchant",
                            'merchant_secret_key': "test_merchant_key",
                            'endpoint_id': "503364",
                            'request_url': None,
    }
    # Obtain and set the target url
    generic_deposit_url = MGUrlsFormatter.get_deposit_url(client_properties['endpoint_id'])
    base_url = httpserver.url_for(generic_deposit_url).split(generic_deposit_url)[0]
    client_properties['request_url'] = base_url

    # Build a client for sending requests
    mg_client = MGClient(**client_properties)

    # Set the mock endpoint
    httpserver.expect_request(mg_client.deposit_request_url).respond_with_json(response_payload)

    # Execute the deposit
    deposit_request = MGDepositRequest(**deposit_payload)
    response = mg_client.send_deposit_request(deposit_request)

    assert response.is_ok
    assert response.merchant_order_id == \
        response_payload[MGDepositResponse.Fields.DATA][MGDepositResponse.Fields.MERCHANT_ORDER_ID]
    assert response.order_id == \
        response_payload[MGDepositResponse.Fields.DATA][MGDepositResponse.Fields.ORDER_ID]


def test_customer_validation_function_fail(monkeypatch, example_deposit_payload):
    test_payload = example_deposit_payload.copy()
    for country in ["US", "CA", "AU"]:
        test_payload['customer_country_code'] = country
        deposit_request = MGDepositRequest(**test_payload)
        ok, reason = deposit_request.validate()
        assert not ok


def test_customer_validation_function_ok(monkeypatch, example_deposit_payload):
    test_payload = example_deposit_payload.copy()
    # ensure there is state in the request
    test_payload['customer_state'] = "NY"
    for country in ["US", "CA", "AU"]:
        test_payload['customer_country_code'] = country
        deposit_request = MGDepositRequest(**test_payload)
        ok, reason = deposit_request.validate()
        assert ok


def test_deposit_request_values(example_deposit_payload):
    test_payload = example_deposit_payload.copy()
    deposit_request = MGDepositRequest(**test_payload)
    for x in test_payload.keys():
        assert getattr(deposit_request, x) == test_payload[x]


def test_card_deposit_request_validate_ok():
    order_payload = generate_test_order(currency="USD", **TestCreditCards.visa_approved_no_3d())
    card_deposit_request = MGCardDepositRequest(**order_payload)
    ok, reason = card_deposit_request.validate()
    assert ok


def test_card_deposit_request_validate_nok_month():
    # card_deposit_payload = generate_random_order(with_card_data=True)
    card_deposit_payload = generate_test_order(**TestCreditCards.visa_approved_no_3d())
    # Modify wrong payload
    card_deposit_payload['card_expiration_month'] = "002"
    card_deposit_request = MGCardDepositRequest(**card_deposit_payload)
    ok, reason = card_deposit_request.validate()
    assert not ok and 'cardExpirationMonth failed validation' in reason


def test_card_deposit_request_validate_nok_year():
    # card_deposit_payload = generate_random_order(with_card_data=True)
    card_deposit_payload = generate_test_order(**TestCreditCards.visa_approved_no_3d())
    card_deposit_payload['card_expiration_year'] = "20210"
    card_deposit_request = MGCardDepositRequest(**card_deposit_payload)
    ok, reason = card_deposit_request.validate()
    assert not ok and 'cardExpirationYear failed validation' in reason


def test_card_deposit_request_validate_nok_number():
    # card_deposit_payload = generate_random_order(with_card_data=True)
    card_deposit_payload = generate_test_order(**TestCreditCards.visa_approved_no_3d())
    card_deposit_payload['card_number'] = "202101239"
    card_deposit_request = MGCardDepositRequest(**card_deposit_payload)
    ok, reason = card_deposit_request.validate()
    assert ok


def test_mg_client_deposit_unsupported(mg_client_usd_cc):
    with pytest.raises(MGException):
        mg_client_usd_cc.send_deposit_request(object())


def test_mg_card_deposit_request():
    card_deposit_payload = generate_test_order(**TestCreditCards.visa_pending_3d())
    card_deposit_request = MGCardDepositRequest(**card_deposit_payload)
    assert card_deposit_request.card_number == \
        card_deposit_payload.get(MGDepositRequest.CardDepositRequestParameters.CARD_NUMBER.arg_name)
    assert card_deposit_request.card_holder_name == \
        card_deposit_payload.get(MGDepositRequest.CardDepositRequestParameters.CARD_HOLDER_NAME.arg_name)
    assert card_deposit_request.card_expiration_month == \
        card_deposit_payload.get(MGDepositRequest.CardDepositRequestParameters.CARD_EXPIRATION_MONTH.arg_name)
    assert card_deposit_request.card_expiration_year == \
        card_deposit_payload.get(MGDepositRequest.CardDepositRequestParameters.CARD_EXPIRATION_YEAR.arg_name)
    assert card_deposit_request.card_cvv == \
        card_deposit_payload.get(MGDepositRequest.CardDepositRequestParameters.CARD_CVV.arg_name)


def test_mg_card_deposit_response(card_deposit_request_response_ok_payload):
    mock_response_ok = MockResponse(code=200, payload=card_deposit_request_response_ok_payload)
    response = MGCardDepositResponse(mock_response_ok)
    assert response.is_ok
    assert response.error is None
    assert response.status == card_deposit_request_response_ok_payload.\
        get(MGCardDepositResponse.Fields.DATA).\
        get(MGCardDepositResponse.Fields.STATUS)
    assert response.order_id == card_deposit_request_response_ok_payload.\
        get(MGCardDepositResponse.Fields.DATA).\
        get(MGCardDepositResponse.Fields.ORDER_ID)
    assert response.merchant_order_id == card_deposit_request_response_ok_payload.\
        get(MGCardDepositResponse.Fields.DATA).\
        get(MGCardDepositResponse.Fields.MERCHANT_ORDER_ID)


def test_mg_build_deposit_cc_nested():
    deposit_request = MGCardDepositRequest()
    deposit_request_payload = generate_test_order(amount=250, **TestCreditCards.mastercard_pending_3d())
    for k, v in deposit_request_payload.items():
        getattr(deposit_request, "set_" + k)(v)

    for x in MGDepositRequest.CardDepositRequestParameters.get_arg_names():
        assert getattr(deposit_request, x) == deposit_request_payload.get(x)


def test_mg_build_deposit_nested():
    deposit_request = MGDepositRequest()
    deposit_request_payload = generate_test_order(250)
    for k, v in deposit_request_payload.items():
        getattr(deposit_request, "set_" + k)(v)

    for x in MGDepositRequest.DepositRequestParameters.get_arg_names():
        assert getattr(deposit_request, x) == deposit_request_payload.get(x)