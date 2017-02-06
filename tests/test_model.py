#!/usr/bin/python
# -*- coding: utf-8 -*-
import pytest
from bearychat.model import UserType, UserRole, is_user_online, is_user_normal


def test_is_user_online():
    assert is_user_online({"conn": False}) is False
    assert is_user_online({"conn": 42}) is False
    assert is_user_online({"conn": "disconnected"}) is False
    assert is_user_online({"conn": "connected"}) is True

    with pytest.raises(KeyError):
        is_user_online({})
    with pytest.raises(AssertionError):
        is_user_online(42)
    with pytest.raises(AssertionError):
        is_user_online(True)
    with pytest.raises(AssertionError):
        is_user_online("foo")


def test_is_user_normal():
    assert is_user_normal({"type": UserType.Assistant,
                           "role": UserRole.Normal}) is False
    assert is_user_normal({"type": 42,
                           "role": UserRole.Normal}) is False
    assert is_user_normal({"type": UserType.Normal,
                           "role": UserRole.Visitor}) is False
    assert is_user_normal({"type": UserType.Normal,
                           "role": UserRole.Normal}) is True
    with pytest.raises(KeyError):
        is_user_normal({})
    with pytest.raises(AssertionError):
        is_user_normal(42)
    with pytest.raises(AssertionError):
        is_user_normal(True)
    with pytest.raises(AssertionError):
        is_user_normal("foo")
