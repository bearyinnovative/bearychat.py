import pytest

from bearychat.openapi.client import Requester


_build_url_testcases = [
    ('foo', 'bar', 'foo/bar'),
    ('', 'bar', '/bar'),
    ('foo', '', 'foo'),
    ('foo', '', 'foo'),
    ('foo/', 'bar', 'foo/bar'),
    ('foo', '/bar', 'foo/bar'),
    ('foo/', '/bar', 'foo/bar'),
    ('foo/', 'bar/', 'foo/bar'),
]


@pytest.mark.parametrize('base_url,api_method,expected', _build_url_testcases)
def test_requester___build_url(base_url, api_method, expected):
    requester = Requester(base_url)
    assert requester._build_url(api_method) == expected
