[![PyPI](https://img.shields.io/badge/zotasdk-v1.2.1-blue)](https://pypi.org/project/zotasdk/)
[![Codecov](https://codecov.io/gh/zota/python-sdk/branch/master/graph/badge.svg?token=5L1EYONUCU)](https://codecov.io/gh/zota/python-sdk)
![Python Matrix Test](https://github.com/zota/python-sdk/workflows/Python%20Matrix%20Test/badge.svg)
[![Python Versions](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12)](https://pypi.org/project/zotasdk/)

![python-github](https://user-images.githubusercontent.com/174284/106497606-f0221600-64c6-11eb-9d98-a6ad1b355e6a.jpg)

# Official Python REST API SDK

This is the **official** page of the [Zota](http://www.zota.com) Python SDK. It is intended to be used by
developers who run modern Python applications and would like to integrate our next generation payments platform.

## REST API Docs

> **[Official Deposit Documentation](https://doc.zota.com/deposit/1.0/#introduction)**

> **[Official Payout Documentation](https://doc.zota.com/payout/1.0/#introduction)**

## Introduction

This Python SDK provides all the necessary methods for integrating the Zota Merchant API.
This SDK is to be used by clients, as well as all the related eCommerce plugins for Python applications.

The SDK covers all available functionality that Zota's Merchant API exposes.

### Requirements

* A functioning Zota Sandbox or Production account and related credentials
* Python 3.8 (or higher)

### Installation

```sh
pip install zotasdk
```

## Configuration

[API CONFIGURATION DOCS](https://doc.zota.com/deposit/1.0/?python#before-you-begin)

Credentials for the SDK can be passed in 3 different ways:

1. To the `MGClient` itself
2. Through environment variables
3. Through a configuration file

This part of the documentation will guide you on how to configure and use this SDK.

### Before you begin

To use this API, obtain the following credentials from Zota:

```
MerchantID         A merchant unique identifier, used for identification.
MerchantSecretKey A secret key to keep privately and securely, used for authentication.
EndpointID         One or more unique endpoint identifiers to use in API requests.
```

Contact [Zota](https://zota.com/contact/) to start your onboarding process and obtain all the credentials.

### API Url

There are two environments to use with the Zota API:

> Sandbox environment, used for integration and testing purposes.
`https://api.zota-sandbox.com`

> Live environment.
`https://api.zota.com`

### Configuration in the code

The implementation fo the Zota API SDK depends on creating an instance of the `MGClient`. First priority
configuration is the one passed to the client itself.

Example:

```python
client = zotasdk.MGClient(
    merchant_id=<MerchantID as received from Zota>, 
    merchant_secret_key=<MerchantSecretKey as received from Zota>, 
    endpoint_id=<EndpointID as received from Zota>, 
    request_url=<MGClient.LIVE_API_URL or MGClient.SANDBOX_API_URL or "https://api.Zota-sandbox.com"...>
)
```

Passing configuration to the client itself is best when supporting multiple clients.

### Environment variables configuration

There are 4 environment variables that need to be set for the API SDK to be configured correctly:

```
Zota_MERCHANT_ID             - MerchantID as received from Zota
Zota_MERCHANT_SECRET_KEY     - MerchantSecretKey as received from Zota
Zota_ENDPOINT_ID             - EndpointID as received from Zota
Zota_REQUEST_URL             - https://api.Zota-sandbox.com or https://api.zota.com
```

### Configuration file

Configuration parameters can be passed through a `.mg_env` file placed in the user's home directory.

The structure of the files follows Python's [configparser](https://docs.python.org/3/library/configparser.html)

Example of a '~/.mg_env' :

```
[MG]
merchant_id=<MerchantID as received from Zota>, 
merchant_secret_key=<MerchantSecretKey as received from Zota>, 
endpoint_id=<EndpointID as received from Zota>, 
request_url=<MGClient.LIVE_API_URL or MGClient.SANDBOX_API_URL or "https://api.zota-sandbox.com"...>
```

## Usage

In order to use the SDK we need to instantiate a client:

```python
from zotasdk.client import MGClient

mg_client = MGClient()
```

### Deposit

A deposit request can be generated in two different ways:

```python
from zotasdk.mg_requests import MGDepositRequest

example_deposit_request_with_kwargs = MGDepositRequest(
    merchant_order_id="QvE8dZshpKhaOmHY",
    merchant_order_desc="Test order",
    order_amount="500.00",
    order_currency="THB",
    customer_email="customer@email-address.com",
    customer_first_name="John",
    customer_last_name="Doe",
    customer_address="5/5 Moo 5 Thong Nai Pan Noi Beach, Baan Tai, Koh Phangan",
    customer_country_code="TH",
    customer_city="Surat Thani",
    customer_zip_code="84280",
    customer_phone="+66-77999110",
    customer_ip="103.106.8.104",
    redirect_url="https://www.example-merchant.com/payment-return/",
    callback_url="https://www.example-merchant.com/payment-callback/",
    custom_param="{\"UserId\": \"e139b447\"}",
    checkout_url="https://www.example-merchant.com/account/deposit/?uid=e139b447",
)

```

or alternatively

```python
example_deposit_request = MGDepositRequest(). \
    set_merchant_order_id("QvE8dZshpKhaOmHY"). \
    set_merchant_order_desc("Test order"). \
    set_order_amount("500"). \
    set_order_currency("USD"). \
    set_customer_email("test@test.com"). \
    set_customer_first_name("John"). \
    set_customer_last_name("Doe"). \
    set_customer_address("5/5 Moo 5 Thong Nai Pan Noi Beach, Baan Tai, Koh Phangan"). \
    set_customer_country_code("TH"). \
    set_customer_city("Surat Thani"). \
    set_customer_zip_code("84280"). \
    set_customer_phone("+66-66006600"). \
    set_customer_ip("103.106.8.104"). \
    set_redirect_url("https://www.example-merchant.com/payment-return/"). \
    set_callback_url("https://www.example-merchant.com/payment-callback/"). \
    set_custom_param("{\"UserId\": \"e139b447\"}"). \
    set_checkout_url("https://www.example-merchant.com/account/deposit/?uid=e139b447")
```

Sending the request to Zota happens through the client:

```python
deposit_response = mg_client.send_deposit_request(example_deposit_request)
print("Deposit Request is " + str(deposit_response.is_ok))
```

In order to send a `Credit Card Deposit` we need to append the appropriate [Credit Card Params](https://doc.zota.com/deposit/1.0/?python#card-payment-integration-2)
which is achieved through sending a `MGCardDepositRequest`

```python
example_cc_deposit_request = MGCardDepositRequest(
    merchant_order_id="QvE8dZshpKhaOmHY",
    merchant_order_desc="Test order",
    order_amount="500.00",
    order_currency="THB",
    customer_email="customer@email-address.com",
    customer_first_name="John",
    customer_last_name="Doe",
    customer_address="5/5 Moo 5 Thong Nai Pan Noi Beach, Baan Tai, Koh Phangan",
    customer_country_code="TH",
    customer_city="Surat Thani",
    customer_zip_code="84280",
    customer_phone="+66-77999110",
    customer_ip="103.106.8.104",
    redirect_url="https://www.example-merchant.com/payment-return/",
    callback_url="https://www.example-merchant.com/payment-callback/",
    custom_param="{\"UserId\": \"e139b447\"}",
    checkout_url="https://www.example-merchant.com/account/deposit/?uid=e139b447",
    
    # CC PARAMS HERE
    card_number="3453789023457890",
    card_holder_name="John Doe",
    card_expiration_month="08",
    card_expiration_year="2027",
    card_cvv="123"
)

deposit_response = mg_client.send_deposit_request(example_cc_deposit_request)
print("Deposit Request is " + str(deposit_response.is_ok))
```

### Working with `Deposit Response`

Each deposit attempt against a Zota returns either a `MGDepositResponse` or `MGCardDepositResponse`.

The above objects are simply a wrapper around the standard HTTP response as described [here](https://doc.zota.com/deposit/1.0/?python#issue-a-deposit-request).

The response classes contain an additional helper method that validates the signature of the response when provided with a `merchant_secret_key`

## Payout

Sending a payout request is almost identical to sending a deposit request.

The request is built:

```python
from zotasdk.mg_requests import MGPayoutRequest

example_payout_request = \
    MGPayoutRequest(merchant_order_id="TbbQzewLWwDW6goc",
                    merchant_order_desc="Test order",
                    order_amount="500.00",
                    order_currency="MYR",
                    customer_email="customer@email-address.com",
                    customer_first_name="John",
                    customer_last_name="Doe",
                    customer_phone="+66-77999110",
                    customer_ip="103.106.8.104",
                    callback_url="https://www.example-merchant.com/payout-callback/",
                    customer_bank_code="BBL",
                    customer_bank_account_number="100200",
                    customer_bank_account_name="John Doe",
                    customer_bank_branch="Bank Branch",
                    customer_bank_address="Thong Nai Pan Noi Beach, Baan Tai, Koh Phangan",
                    customer_bank_zip_code="84280",
                    customer_bank_province="Bank Province",
                    customer_bank_area="Bank Area / City",
                    customer_bank_routing_number="000",
                    custom_param="{\"UserId\": \"e139b447\"}",
                    checkout_url="https://www.example-merchant.com/account/withdrawal/?uid=e139b447")
```

The client returns `MGPayoutResponse` which is again a wrapper around the standard HTTP response.

## Callbacks

`MGCallback` is a class that parses the raw HTTP Request sent from Zota to the configured endpoint. It's purpose
is to make working with callbacks manageable.

## Validations

The `MGRequest` class implements a `validate()` method which can be used for parameter validation of the request
offline before the request is being sent. It's purpose is to check whether all the values passsed to the different
parameters is in-line with what Zota's endpoint expects. See the API DOCS for more info and guidance about the
format of the different parameters.

## Test Coverage

[![codecov](https://codecov.io/gh/Zota/python-sdk/graphs/tree.svg?width=650&height=150&src=pr&token=5L1EYONUCU)](https://codecov.io/gh/Zota/python-sdk/)
