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

from bearychat.openapi._api import apis


def format_method(service_name, method_name):
    if method_name is None:
        return service_name
    return '{}.{}'.format(service_name, method_name)


def get_api(service_name, method_name):
    service = apis.get(service_name)
    if service is None:
        expected_method = format_method(service_name, method_name)
        raise RuntimeError('unknown method: {}'.format(expected_method))

    if method_name is None:
        method = service
    else:
        method = service.get(method_name)

    if method is None or 'method' not in method:
        expected_method = format_method(service_name, method_name)
        raise RuntimeError('unknown method: {}'.format(expected_method))

    return method


def get_methods(service_name):
    service = apis.get(service_name)
    if service is None:
        raise RuntimeError('unknown service: {}'.format(service_name))

    if 'method' in service:
        # only one level
        return [service_name]

    return list(service.keys())


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
        except ValueError:
            raise RequestFailedError(resp, 'not a json body')

        if not resp.ok:
            raise RequestFailedError(resp, rv.get('error'))

        return rv


# Oki-dokie-Loki here come the magic pony
class _Service(object):

    def __init__(self, base, client):
        self._base = base
        self._client = client

    def _build_requester(self, name):
        api_method = format_method(self._base, name)
        method_spec = get_api(self._base, name)
        request_method = method_spec['method']
        token = self._client.token
        need_auth = method_spec['authentication'] is not False

        requester = self._client.requester

        # TODO(hbc):
        #  - wraps method name
        #  - memoize method (stubs)
        def _call(params=None, *args, **kwargs):
            if params is None:
                params = {}
            if need_auth:
                params['token'] = token

            return requester.request(
                request_method,
                api_method,
                params=params,
                *args,
                **kwargs
            )
        return _call

    def __getattr__(self, name):
        return self._build_requester(name)

    def __call__(self, *args, **kwargs):
        return self._build_requester(None)(*args, **kwargs)

    def __dir__(self):
        return get_methods(self._base)


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

        self.meta = _Service('meta', self)
        self.team = _Service('team', self)
        self.user = _Service('user', self)
        self.vchannel = _Service('vchannel', self)
        self.channel = _Service('channel', self)
        self.session_channel = _Service('session_channel', self)
        self.p2p = _Service('p2p', self)
        self.message = _Service('message', self)
        self.sticker = _Service('sticker', self)
        self.emoji = _Service('emoji', self)
        self.rtm = _Service('rtm', self)
