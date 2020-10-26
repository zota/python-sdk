# pylint: disable=missing-module-docstring
from zotapaysdk.config import ZOTAPAY_REST_API_VERSION

BASE_URL = "/api/{version}".format(**{'version': ZOTAPAY_REST_API_VERSION})
MG_DEPOSIT_RAW_URL = BASE_URL + "/deposit/request/{endpoint_id}/"
MG_ORDER_STATUS_RAW_URL = BASE_URL + "/query/order-status/"
MG_PAYOUT_RAW_URL = BASE_URL + "/payout/request/{endpoint_id}/"


class MGUrlsFormatter:
    """
    Class containing the logic for building the different url patters for the different requests.
    """

    @staticmethod
    def get_deposit_url(endpoint_id):
        """
        Generates the actual URL for deposit against the ZotaPay API.
        Args:
            endpoint_id:

        Returns:

        """
        return MG_DEPOSIT_RAW_URL.format(
            endpoint_id=endpoint_id
        )

    @staticmethod
    def get_order_status_url():
        """
        Generates the actual URL for status check against the ZotaPay API.
        Returns:

        """
        return MG_ORDER_STATUS_RAW_URL

    @staticmethod
    def get_payout_url(endpoint_id):
        """
        Generates the actual URL for payout against the ZotaPay API.
        Args:
            endpoint_id:

        Returns:

        """
        return MG_PAYOUT_RAW_URL.format(
            endpoint_id=endpoint_id
        )
