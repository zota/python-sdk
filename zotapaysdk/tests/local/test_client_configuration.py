import pytest

from zotapaysdk.client import MGClient
from zotapaysdk.config import CredentialsKeys, MGCredentialsManager
from zotapaysdk.exceptions import MGMissingCredentialsException


def test_client_environment_configuration_fail_request_url(monkeypatch):
    """
    Checks if env var test fails for missing request url
    Args:
        monkeypatch:

    Returns:

    """
    monkeypatch.setenv(CredentialsKeys.Env.ENDPOINT_ID, "test")
    monkeypatch.setenv(CredentialsKeys.Env.MERCHANT_SECRET_KEY, "test")
    monkeypatch.setenv(CredentialsKeys.Env.MERCHANT_ID, "test")
    with pytest.raises(MGMissingCredentialsException):
        MGClient()


def test_client_environment_configuration_fail_endpoint_id(monkeypatch):
    """
    Checks if env var test fails for missing endpoint_id
    Args:
        monkeypatch:

    Returns:

    """
    monkeypatch.setenv(CredentialsKeys.Env.REQUEST_URL, "www.test.com")
    monkeypatch.setenv(CredentialsKeys.Env.MERCHANT_SECRET_KEY, "test")
    monkeypatch.setenv(CredentialsKeys.Env.MERCHANT_ID, "test")
    with pytest.raises(MGMissingCredentialsException):
        MGClient()


def test_client_environment_configuration_fail_merchant_secret_key(monkeypatch):
    """
    Checks if env var test fails for missing merchant secret key
    Args:
        monkeypatch:

    Returns:

    """
    monkeypatch.setenv(CredentialsKeys.Env.REQUEST_URL, "www.test.com")
    monkeypatch.setenv(CredentialsKeys.Env.ENDPOINT_ID, "test")
    monkeypatch.setenv(CredentialsKeys.Env.MERCHANT_ID, "test")
    with pytest.raises(MGMissingCredentialsException):
        MGClient()


def test_client_environment_configuration_fail_merchant_id(monkeypatch):
    """
    Checks if env var test fails for missing merchant id
    Args:
        monkeypatch:

    Returns:

    """
    monkeypatch.setenv(CredentialsKeys.Env.REQUEST_URL, "www.test.com")
    monkeypatch.setenv(CredentialsKeys.Env.ENDPOINT_ID, "test")
    monkeypatch.setenv(CredentialsKeys.Env.MERCHANT_SECRET_KEY, "test")
    with pytest.raises(MGMissingCredentialsException):
        MGClient()


def test_client_environment_configuration_ok(monkeypatch):
    """
    Asserts MGClient instance is created ok with proper credentials
    Args:
        monkeypatch:

    Returns:

    """
    monkeypatch.setenv(CredentialsKeys.Env.REQUEST_URL, "www.test.com")
    monkeypatch.setenv(CredentialsKeys.Env.ENDPOINT_ID, "test")
    monkeypatch.setenv(CredentialsKeys.Env.MERCHANT_SECRET_KEY, "test")
    monkeypatch.setenv(CredentialsKeys.Env.MERCHANT_ID, "test")
    MGClient()


def test_client_environment_configuration_with_bad_creds(monkeypatch):
    """
    Extra test for bad credentials.
    Args:
        monkeypatch:

    Returns:

    """
    monkeypatch.setenv(CredentialsKeys.Env.REQUEST_URL, " ")
    monkeypatch.setenv(CredentialsKeys.Env.ENDPOINT_ID, " ")
    monkeypatch.setenv(CredentialsKeys.Env.MERCHANT_SECRET_KEY, " ")
    monkeypatch.setenv(CredentialsKeys.Env.MERCHANT_ID, " ")
    with pytest.raises(MGMissingCredentialsException):
        MGClient()


def test_credentials_manager():
    with pytest.raises(MGMissingCredentialsException):
        MGCredentialsManager(merchant_id="a", merchant_secret_key="a", endpoint_id="a", request_url="a")

    with pytest.raises(MGMissingCredentialsException):
        MGCredentialsManager(merchant_id="teststestse",
                             merchant_secret_key="testets",
                             endpoint_id="testests")

    with pytest.raises(MGMissingCredentialsException):
        MGCredentialsManager(merchant_id="testsetes", merchant_secret_key="testestes", request_url="testsetes")
