import ssl
import requests

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
from requests.packages.urllib3.util import ssl_


class _MGTLSAdapter(HTTPAdapter):

    def __init__(self, ssl_options=0, **kwargs):
        self.ssl_options = ssl_options
        super(_MGTLSAdapter, self).__init__(**kwargs)

    def init_poolmanager(self, *pool_args, **pool_kwargs):
        ctx = ssl_.create_urllib3_context(ssl.PROTOCOL_TLS)
        # extend the default context options, which is to disable ssl2, ssl3
        # and ssl compression, see:
        # https://github.com/shazow/urllib3/blob/6a6cfe9/urllib3/util/ssl_.py#L241
        ctx.options |= self.ssl_options
        self.poolmanager = PoolManager(*pool_args,
                                       ssl_context=ctx,
                                       **pool_kwargs)


def mg_request(method="post", url=None, data=None, json=None, **kwargs):
    """
    Wrapper around the requests.post method that will enforce the usage of TLS 1.2 or higher when sending
    requests through this SDK.

    Args:
        method: The method for the request 'GET', 'POST', etc.
        url: There url to call
        data:
        json:
        **kwargs:

    Returns:

    """
    with requests.sessions.Session() as _session:
        _adapter = _MGTLSAdapter(ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1)

        _session.mount("http://", _adapter)
        _session.mount("https://", _adapter)

        return _session.request(method=method,
                                url=url,
                                data=data,
                                json=json, **kwargs)
