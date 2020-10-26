# pylint: disable=too-few-public-methods,missing-module-docstring
from configparser import RawConfigParser
from zotapaysdk.exceptions import MGMissingCredentialsException
from os.path import expanduser
import os

ZOTAPAY_REST_API_VERSION = "v1"

_home = expanduser("~")
MG_CONFIG_FILE_PATH = _home
MG_CONFIG_FILE_NAME = ".mg_env"

config = RawConfigParser()

if MG_CONFIG_FILE_NAME in os.listdir(os.path.expanduser(MG_CONFIG_FILE_PATH)):
    with open(MG_CONFIG_FILE_PATH + MG_CONFIG_FILE_NAME) as conf_file:
        config.read_file(conf_file)


class CredentialsKeys:
    """
    Static class with all the names of the credentials that need to be set.
    """
    class Env:
        """
        Environment Variable names
        """
        MERCHANT_ID = "ZOTAPAY_MERCHANT_ID"
        MERCHANT_SECRET_KEY = "ZOTAPAY_MERCHANT_SECRET_KEY"
        ENDPOINT_ID = "ZOTAPAY_ENDPOINT_ID"
        REQUEST_URL = "ZOTAPAY_REQUEST_URL"

    class ConfigFile:
        """
        Configuration file variable names
        """
        SECTION = "MG"
        MERCHANT_ID = "merchant_id"
        MERCHANT_SECRET_KEY = "merchant_secret_key"
        ENDPOINT_ID = "endpoint_id"
        REQUEST_URL = "request_url"


def _get_merchant_id_credentials():
    """
    Gets the Merchant ID from either the ENV VARS or from the config file.
    Returns:

    """
    env_merchant_id = os.environ.get(CredentialsKeys.Env.MERCHANT_ID)
    config_file_merchant_id = config.get(CredentialsKeys.ConfigFile.SECTION,
                                         CredentialsKeys.ConfigFile.MERCHANT_ID,
                                         fallback=None)
    return config_file_merchant_id if config_file_merchant_id else env_merchant_id


def _get_merchant_secret_key():
    """
    Gets the Merchant Secret Key from either the ENV VARS or from the config file.
    Returns:

    """
    env_merchant_secret_key = os.environ.get(CredentialsKeys.Env.MERCHANT_SECRET_KEY)
    config_file_merchant_secret_key = config.get(CredentialsKeys.ConfigFile.SECTION,
                                                 CredentialsKeys.ConfigFile.MERCHANT_SECRET_KEY,
                                                 fallback=None)
    return config_file_merchant_secret_key \
        if config_file_merchant_secret_key else env_merchant_secret_key


def _get_endpoint_id():
    """
    Gets the Endpoint ID from either the ENV VARS or from the config file.
    Returns:

    """
    env_endpoint_id = os.environ.get(CredentialsKeys.Env.ENDPOINT_ID)
    config_file_endpoint_id = config.get(CredentialsKeys.ConfigFile.SECTION,
                                         CredentialsKeys.ConfigFile.ENDPOINT_ID,
                                         fallback=None)
    return config_file_endpoint_id if config_file_endpoint_id else env_endpoint_id


def _get_request_url():
    """
    Gets the Request Url from either the ENV VARS or from the config file.
    Returns:

    """
    env_request_url = os.environ.get(CredentialsKeys.Env.REQUEST_URL)
    config_file_request_url = config.get(CredentialsKeys.ConfigFile.SECTION,
                                         CredentialsKeys.ConfigFile.REQUEST_URL,
                                         fallback=None)
    return config_file_request_url if config_file_request_url else env_request_url


class MGCredentialsManager:
    def __init__(self, merchant_id=None, merchant_secret_key=None, endpoint_id=None,
                 request_url=None):
        """
        Class containing logic for dealing with credentials for the Zota API.

        Parses the credentials from the keyword parameters, environment variables
        or a config file in this strict order.

        See Also https://doc.zotapay.com/deposit/1.0/?python#before-you-begin

        Args:
            merchant_id:
            merchant_secret_key:
            endpoint_id:
            request_url:
        """
        self.__merchant_id = merchant_id if merchant_id else _get_merchant_id_credentials()
        self.__merchant_secret_key = merchant_secret_key \
            if merchant_secret_key else _get_merchant_secret_key()
        self.__endpoint_id = endpoint_id if endpoint_id else _get_endpoint_id()
        self.__request_url = request_url if request_url else _get_request_url()
        self._verify_credentials()

    @property
    def merchant_id(self):
        """
        Getter for the merchant_id
        Returns:

        """
        return self.__merchant_id

    @property
    def merchant_secret_key(self):
        """
        Getter for the merchant_secret_key
        Returns:

        """
        return self.__merchant_secret_key

    @property
    def endpoint_id(self):
        """
        Getter for the endpoint_url
        Returns:

        """
        return self.__endpoint_id

    @property
    def request_url(self):
        """
        Getter for the request_url
        Returns:

        """
        return self.__request_url

    def _verify_credentials(self):
        """
        Carries out a validation that all expected configuration variables are set.

        Returns:

        """
        if not self.merchant_id or len(self.merchant_id) < 3:
            raise MGMissingCredentialsException("No Merchant Id is set.")
        if not self.merchant_secret_key or len(self.merchant_secret_key) < 3:
            raise MGMissingCredentialsException("No Merchant Secret Key is set.")
        if not self.endpoint_id or len(self.endpoint_id) < 3:
            raise MGMissingCredentialsException("No Endpoint Id is set.")
        if not self.request_url or len(self.request_url) < 3:
            raise MGMissingCredentialsException("No Request URL is set.")
