"""
bearychat.openapi.client
~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the OpenAPI client.
"""

import sys
PY3 = sys.version_info[0] == 3

if PY3:
    import urllib.parse as urlparse
else:
    import urlparse

import requests


class RequestFailedError(ValueError):
    """Request to OpenAPI failed. Caller can use `e.resp` to access
    the response instance.

    Args:
        - resp: A requests.Response instance representing this request.
        - message: Error reason. Optional.
    """
    def __init__(self, resp, message=None):
        super(ValueError, self).__init__(message)

        self.resp = resp


# TODO(hbc): allow specify requester in client
class Requester(object):

    def __init__(self, base_url):
        self.base_url = urlparse.urlparse(base_url.rstrip('/'))

    def _build_url(self, api_method):
        path = '{}/{}'.format(self.base_url.path, api_method.lstrip('/'))
        url = self.base_url._replace(path=path)
        return urlparse.urlunparse(url).rstrip('/')

    def request(self, request_method, api_method, *args, **kwargs):
        """Perform a request.

        Args:
            request_method: HTTP method for this request.
            api_method: API method name for this request.
            *args: Extra arguments to pass to the request.
            **kwargs: Extra keyword arguments to pass to the request.

        Returns:
            A dict contains the request response data.

        Raises:
            RequestFailedError: Raises when BearyChat's OpenAPI responses
                with status code != 2xx
        """
        url = self._build_url(api_method)
        resp = requests.request(request_method, url, *args, **kwargs)

        try:
            rv = resp.json()
        except ValueError as e:
            raise RequestFailedError(resp, 'not a json body')

        if not resp.ok:
            raise RequestFailedError(resp, rv.get('error'))

        return rv


class Client(object):
    """OpenAPI request client

    Basic Usage::

        >>> from bearychat import openapi
        >>> c = openapi.Client('your-token-here')
        >>> c.meta()
        {'version': '1'}

    Args:
        token: OpenAPI token.
        base_url: OpenAPI url's base url,
            defaults to `https://api.bearychat.com/v1`
    """

    def __init__(self, token, base_url=None):
        self.token = token
        self.requester = Requester(base_url or 'https://api.bearychat.com/v1')
