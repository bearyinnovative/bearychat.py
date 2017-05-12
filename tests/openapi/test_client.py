import pytest

from bearychat.openapi import client


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
    requester = client.Requester(base_url)
    assert requester._build_url(api_method) == expected


format_method_testcases = [
    ('foo', 'bar', 'foo.bar'),
    ('foo', None, 'foo'),
]


@pytest.mark.parametrize('service_name,method_name,expected',
                         format_method_testcases)
def test_format_method(service_name, method_name, expected):
    assert client.format_method(service_name, method_name) == expected


def test_get_api():
    assert client.get_api('meta', None)
    assert client.get_api('channel', 'list')

    with pytest.raises(RuntimeError):
        client.get_api('foobar', None)

    with pytest.raises(RuntimeError):
        client.get_api('channel', 'foobar')


def test_get_methods():
    assert client.get_methods('meta') == ['meta']
    assert len(client.get_methods('channel')) > 0

    with pytest.raises(RuntimeError):
        client.get_methods('foobar')


def test_client_meta():
    c = client.Client('foobar')
    assert c.meta(), 'should return meta'
