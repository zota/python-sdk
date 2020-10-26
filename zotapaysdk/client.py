# pylint: disable=missing-module-docstring,missing-class-docstring
import os
import time
import json
from hashlib import sha256
import sys
import requests

from zotapaysdk.constants import POST, GET
from zotapaysdk.helpers import UA_STRING
from zotapaysdk.mg_comms import mg_request
from zotapaysdk.mg_requests.payout_response import MGPayoutResponse
from zotapaysdk.exceptions import MGException
from zotapaysdk.urls import MGUrlsFormatter
from zotapaysdk.config import MGCredentialsManager
from zotapaysdk.mg_requests import (
    MGCardDepositResponse,
    MGOrderStatusResponse,
    MGCardDepositRequest,
    MGDepositRequest)
from zotapaysdk.mg_requests import MGDepositResponse
import zotapaysdk


class MGClient:

    LIVE_API_URL = "https://api.zotapay.com"
    SANDBOX_API_URL = "https://api.zotapay-sandbox.com"

    def __init__(self, merchant_id=None, merchant_secret_key=None, endpoint_id=None,
                 request_url=None):
        """
        Main client for working with Zotapay's API.

        See more info https://doc.zotapay.com/deposit/1.0/?python#introduction

        Args:
            merchant_id: A merchant unique identifier, used for identification.
            merchant_secret_key: A authetication secret key to keep privately and securely.
            endpoint_id: Unique endpoint identifier to use in API mg_requests.
            request_url: Environment URL
        """
        self._credentials_manager = MGCredentialsManager(merchant_id=merchant_id,
                                                         merchant_secret_key=merchant_secret_key,
                                                         endpoint_id=endpoint_id,
                                                         request_url=request_url)

    @property
    def merchant_id(self):
        """
        Getter for the Merchant ID.

        Returns:

        """
        return self._credentials_manager.merchant_id

    @property
    def request_url(self):
        """
        Getter for the Request Url.

        Returns:

        """
        return self._credentials_manager.request_url

    @property
    def merchant_secret_key(self):
        """
        Getter for the Merchant Secret Key.

        Returns:

        """
        return self._credentials_manager.merchant_secret_key

    @property
    def endpoint_id(self):
        """
        Getter for the Endpoint ID.

        Returns:

        """
        return self._credentials_manager.endpoint_id

    @property
    def deposit_request_url(self):
        """
        Returns the url where deposit requests should be sent.

        https://doc.zotapay.com/deposit/1.0/?python#deposit-request

        Returns:

        """
        return MGUrlsFormatter.get_deposit_url(self.endpoint_id)

    @property
    def order_status_request_url(self):
        """
        Returns the url where order status check requests should be sent.

        https://doc.zotapay.com/deposit/1.0/?python#order-status-request

        Returns:

        """
        return MGUrlsFormatter.get_order_status_url()

    @property
    def payout_request_url(self):
        """
        Returns the url where payout requests should be sent.

        https://mg-docs.zotapay.com/payout/1.0/#payout-request

        Returns:

        """
        return MGUrlsFormatter.get_payout_url(self.endpoint_id)

    def _generate_deposit_request_signature(self, deposit_request):
        """
        Generates the signature for Deposit Requests as expected by Zotapay's API.

        See https://doc.zotapay.com/deposit/1.0/?python#signature

        Args:
            deposit_request: An instance of the Deposit Request that is to be signed

        Returns:

        """

        signature_template = "{endpoint_id}" \
                             "{merchant_order_id}" \
                             "{order_amount}" \
                             "{customer_email}" \
                             "{merchant_secret_key}"

        signature = signature_template.format(
            **{
                "endpoint_id": self.endpoint_id,
                "merchant_order_id": deposit_request.merchant_order_id,
                "order_amount": deposit_request.order_amount,
                "customer_email": deposit_request.customer_email,
                "merchant_secret_key": self.merchant_secret_key
            }
        )
        return sha256(signature.encode('utf-8')).hexdigest()

    def _generate_order_status_request_signature(self, order_status_request, ts):
        """
        Generates the signature for Order Status Requests as expected by Zotapay's API.

        See https://doc.zotapay.com/deposit/1.0/?python#signature-2

        Args:
            order_status_request (MGOrderStatusRequest): An instance of the status request
            ts (timestamp): a timestamp for the signature (as required)

        Returns:

        """
        signature_template = "{merchant_id}" \
                             "{merchant_order_id}" \
                             "{order_id}" \
                             "{ts}" \
                             "{merchant_secret_key}"
        signature = signature_template.format(
            **{
                "merchant_id": self.merchant_id,
                "merchant_order_id": order_status_request.merchant_order_id,
                "order_id": order_status_request.order_id,
                "ts": ts,
                "merchant_secret_key": self.merchant_secret_key
            }
        )

        return sha256(signature.encode('utf-8')).hexdigest()

    def _generate_payout_request_signature(self, payout_request):
        """
        Generates the signature for Payout Requests as expected by ZotaPay's API.

        See https://mg-docs.zotapay.com/payout/1.0/#signature

        Args:
            payout_request (MGPayoutRequest): An instance of the payout request

        Returns:

        """
        signature_template = "{endpoint_id}" \
                             "{merchant_order_id}" \
                             "{order_amount}" \
                             "{customer_email}" \
                             "{customer_bank_account_number}" \
                             "{merchant_secret_key}"

        signature = signature_template.format(
            **{
                "endpoint_id": self.endpoint_id,
                "merchant_order_id": payout_request.merchant_order_id,
                "order_amount": payout_request.order_amount,
                "customer_email": payout_request.customer_email,
                "customer_bank_account_number": payout_request.customer_bank_account_number,
                "merchant_secret_key": self.merchant_secret_key
            }
        )

        return sha256(signature.encode('utf-8')).hexdigest()

    def _prepare_user_agent_for_request(self):
        """

        Returns:
            Example:
                zotapaysdk/0.1
                (
                    Darwin; 19.3.0;
                    Darwin Kernel Version 19.3.0:
                    Thu Jan  9 20:58:23 PST 2020;
                    root:xnu-6153.81.5~1/RELEASE_X86_64;
                    x86_64;
                )
                Python SDK
                (
                    Python 3.7.4 (default, Aug 13 2019, 15:17:50)
                        [Clang 4.0.1 (tags/RELEASE_401/final)];
                    Requests: 2.22.0;
                )

        """
        _system = os.uname()
        user_agent = UA_STRING.format(
            **{
                'sdk_version': zotapaysdk.__version__,
                'os_sysname': getattr(_system, "sysname", "-"),
                'os_release': getattr(_system, "release", "-"),
                "os_version": getattr(_system, "version", "-"),
                'os_arch': getattr(_system, "machine", "-"),
                'python_version': sys.version,
                'requests_version': requests.__version__
            }
        )

        user_agent = user_agent.replace('\n', "")
        return user_agent

    def _generate_deposit_request_headers(self):
        return {
            "content-type": "application/json",
            "user-agent": self._prepare_user_agent_for_request(),
        }

    def _generate_order_status_request_headers(self):
        return {
            "content-type": "application/json",
            "user-agent": self._prepare_user_agent_for_request()
        }

    def _generate_payout_request_headers(self):
        return {
            "content-type": "application/json",
            "user-agent": self._prepare_user_agent_for_request()
        }

    def _send_request(self, method, url, payload, headers):
        """
        Send the call to the API.

        Args:
            url (str): The actual url to send to.
            payload: The payout after it's converted to string values
            headers: The expected headers.

        Returns:

        """
        if payload:
            # If there is a payload to validate and serialize then do
            payload = json.dumps(self._assert_all_values_as_strings(payload))
        response = mg_request(method=method,
                              url=url,
                              data=payload,
                              headers=headers)
        return response

    def _assert_all_values_as_strings(self, payload):
        """
        Iterates over the request payload and ensures that all values are cast to strings
        as expected by the ZotaPay API.

        Args:
            payload (dict): A dict of parameters that are to be send as the API call payload.

        Returns (dict): The same payload dict with all values converted to strings.

        """
        return {
            k: str(v) for k, v in payload.items()
        }

    def _send_deposit_request(self, deposit_request):
        """
        Sends a general deposit request to the ZotaPay API

        Args:
            deposit_request (MGDepositRequest):
                See class implementation for more detailed information.
        Returns:

        """
        signature = self._generate_deposit_request_signature(deposit_request)
        payload = deposit_request.to_signed_payload(signature)
        headers = self._generate_deposit_request_headers()
        url = self.request_url + self.deposit_request_url
        response = self._send_request(POST, url, payload, headers)
        mg_response = MGDepositResponse(response)
        return mg_response

    def _send_credit_card_deposit_request(self, deposit_request):
        """

        Args:
            deposit_request (MGCardDepositRequest):

        Returns:

        """
        signature = self._generate_deposit_request_signature(deposit_request)
        payload = deposit_request.to_signed_payload(signature)
        headers = self._generate_deposit_request_headers()
        url = self.request_url + self.deposit_request_url
        response = self._send_request(POST, url, payload, headers)
        mg_response = MGCardDepositResponse(response)
        return mg_response

    def send_deposit_request(self, deposit_request):
        """
        Signs and sends the deposit request to the Zotapay Deposit API.

        Args:
            deposit_request: An instance of the Deposit Request Class
                See class implementation for more detailed information.
        Returns:
            An instance of the MGResponse class
        """

        if type(deposit_request) == MGDepositRequest:
            return self._send_deposit_request(deposit_request)
        if type(deposit_request) == MGCardDepositRequest:
            return self._send_credit_card_deposit_request(deposit_request)

        raise MGException("Unsupported request type {}".format(deposit_request.__class__.__name__))

    def send_order_status_request(self, order_status_request):
        """

        Args:
            order_status_request (MGOrderStatusRequest):
                See class implementation for more detailed information.
        Returns (MGOrderStatusResponse):
            See class implementation for more detailed information.
        """
        ts = int(time.time())
        signature = self._generate_order_status_request_signature(order_status_request, ts)
        payload = order_status_request.to_signed_payload(self.merchant_id, ts, signature)
        headers = self._generate_order_status_request_headers()
        url = self.request_url + self.order_status_request_url + payload
        response = self._send_request(GET, url, None, headers)
        return MGOrderStatusResponse(http_response=response)

    def send_payout_request(self, payout_request):
        """
        Executes the payout request against the api.

        Args:
            payout_request (MGPayoutRequest):
                See class implementation for more detailed information.

        Returns (MGPayoutResponse):
            See class implementation for more detailed information.
        """
        signature = self._generate_payout_request_signature(payout_request)
        payload = payout_request.to_signed_payload(signature)
        headers = self._generate_payout_request_headers()
        url = self.request_url + self.payout_request_url
        response = self._send_request(POST, url, payload, headers)
        mg_response = MGPayoutResponse(response)
        return mg_response
