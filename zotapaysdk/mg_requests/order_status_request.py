from zotapaysdk.mg_requests.objects import MGRequestParam
from zotapaysdk.mg_requests.mg_request import MGRequest


class MGOrderStatusRequest(MGRequest):
    # pylint: disable=too-few-public-methods,missing-module-docstring
    """
    Implementation of the Order Status Request class.
    """
    class MGOrderStatus:
        """
        Definition of all the possible statuses of an order.

        See https://mg-docs.zotapay.com/payout/1.0/#common-resources
        """
        CREATED = "CREATED"
        PROCESSING = "PROCESSING"
        APPROVED = "APPROVED"
        DECLINED = "DECLINED"
        FILTERED = "FILTERED"
        PENDING = "PENDING"
        UNKNOWN = "UNKNOWN"
        ERROR = "ERROR"

    def __init__(self, **kwargs):
        """
            See Also https://doc.zotapay.com/deposit/1.0/?python#issue-an-order-status-request
        Args:
            **kwargs:
        """
        self._merchant_order_id = \
            MGRequestParam(self.OrderStatusRequestParameters.MERCHANT_ORDER_ID.request_param_name,
                           kwargs.get(self.OrderStatusRequestParameters.MERCHANT_ORDER_ID.arg_name,
                                      None),
                           max_size=128,
                           required=True)

        self._order_id = \
            MGRequestParam(self.OrderStatusRequestParameters.ORDER_ID.request_param_name,
                           kwargs.get(self.OrderStatusRequestParameters.ORDER_ID.arg_name,
                                      None),
                           max_size=128,
                           required=True)

    @property
    def merchant_order_id(self):
        """
        Getter for the merchant order id.

        Returns:

        """
        return self._merchant_order_id.param_value

    @property
    def order_id(self):
        """
        Getter for the order id.

        Returns:

        """
        return self._order_id.param_value

    def to_signed_payload(self, merchant_id, ts, signature):
        signed_payload_query_arguments_template = "?merchantID={merchant_id}" \
            "&merchantOrderID={merchant_order_id}" \
            "&orderID={order_id}" \
            "&timestamp={ts}" \
            "&signature={signature}"

        return signed_payload_query_arguments_template.format(
            **{
                "merchant_id": merchant_id,
                "merchant_order_id": self.merchant_order_id,
                "order_id": self.order_id,
                "ts": ts,
                "signature": signature
            }
        )
