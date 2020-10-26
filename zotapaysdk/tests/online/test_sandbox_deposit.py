"""
[!IMPORTANT] All tests here actually run against the sandbox environment.
"""
from unittest.mock import MagicMock

from zotapaysdk.mg_requests import \
    (
        MGPayoutRequest,
        MGOrderStatusRequest,
        MGCardDepositRequest,
        MGDepositRequest
    )

from zotapaysdk.testing_tools import generate_test_order, TestCreditCards, generate_test_payout


def test_mg_deposit_request_sandbox_ok_myr(mg_client_myr_sa):
    expected_currency = "MYR"
    order_payload = generate_test_order(currency=expected_currency)

    deposit_request = MGDepositRequest(**order_payload)
    response = mg_client_myr_sa.send_deposit_request(deposit_request)

    assert response.is_ok
    assert response.error is None
    assert response.deposit_url is not None
    assert response.merchant_order_id is not None
    assert response.order_id is not None


def test_mg_card_deposit_request_sandbox_ok(mg_client_usd_cc):
    card_deposit_payload = generate_test_order(**TestCreditCards.visa_pending_3d())
    card_deposit_request = MGCardDepositRequest(**card_deposit_payload)
    response = mg_client_usd_cc.send_deposit_request(card_deposit_request)
    assert response.is_ok
    assert response.status == MGOrderStatusRequest.MGOrderStatus.PROCESSING


def test_mg_card_deposit_request_sandbox_nok(mg_client_usd_cc):
    card_request_payload = generate_test_order(**TestCreditCards.mastercard_pending_3d())
    card_request_payload['card_number'] = "12321"
    card_deposit_request = MGCardDepositRequest(**card_request_payload)
    response = mg_client_usd_cc.send_deposit_request(card_deposit_request)
    assert not response.is_ok


def test_mg_deposit_request_sandbox_nok_myr(monkeypatch, mg_client_myr_sa):
    expected_currency = "MYR"
    # Mock the signature method to return a bad signature
    mg_client_myr_sa._generate_deposit_request_signature = MagicMock(return_value="g43p8rgjp2983jg")
    order_payload = generate_test_order(currency=expected_currency)
    deposit_request = MGDepositRequest(**order_payload)

    response = mg_client_myr_sa.send_deposit_request(deposit_request)
    assert not response.is_ok
    assert response.error == "unauthorized"


def test_mg_payout_request_sandbox_ok(monkeypatch, example_payout_payload, mg_client_myr_sa):
    expected_currency = "MYR"
    payout_payload = generate_test_payout(amount=500, currency=expected_currency)
    payout_request = MGPayoutRequest(**payout_payload)
    response = mg_client_myr_sa.send_payout_request(payout_request)
    assert response.is_ok
