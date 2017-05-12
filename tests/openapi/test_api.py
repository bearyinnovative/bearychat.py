from bearychat.openapi import _api


def test_apis():
    assert isinstance(_api.apis, dict), 'apis should be a dict'
