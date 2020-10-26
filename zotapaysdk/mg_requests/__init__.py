from zotapaysdk.mg_requests.payout_request import MGPayoutRequest
from zotapaysdk.mg_requests.deposit_request import MGDepositRequest
from zotapaysdk.mg_requests.card_deposit_request import MGCardDepositRequest
from zotapaysdk.mg_requests.order_status_request import MGOrderStatusRequest
from zotapaysdk.mg_requests.deposit_response import MGDepositResponse
from zotapaysdk.mg_requests.order_status_response import MGOrderStatusResponse
from zotapaysdk.mg_requests.card_deposit_response import MGCardDepositResponse

__all__ = ["MGDepositRequest",
           "MGCardDepositRequest",
           "MGOrderStatusRequest",
           "MGCardDepositResponse",
           "MGOrderStatusResponse",
           "MGDepositResponse",
           "MGPayoutRequest"]
