from zotasdk.mg_requests.payout_request import MGPayoutRequest
from zotasdk.mg_requests.deposit_request import MGDepositRequest
from zotasdk.mg_requests.card_deposit_request import MGCardDepositRequest
from zotasdk.mg_requests.order_status_request import MGOrderStatusRequest
from zotasdk.mg_requests.deposit_response import MGDepositResponse
from zotasdk.mg_requests.order_status_response import MGOrderStatusResponse
from zotasdk.mg_requests.card_deposit_response import MGCardDepositResponse

__all__ = ["MGDepositRequest",
           "MGCardDepositRequest",
           "MGOrderStatusRequest",
           "MGCardDepositResponse",
           "MGOrderStatusResponse",
           "MGDepositResponse",
           "MGPayoutRequest"]
