#!/usr/bin/python
# -*- coding: utf-8 -*-


class UserType(object):
    Normal = "normal"
    Assistant = "assistant"
    Hubot = "hubot"


class UserRole(object):
    Owner = "owner"
    Admin = "admin"
    Normal = "normal"
    Visitor = "visitor"


def is_user_online(user):
    # type: (Dict) -> bool
    return user["conn"] == "connected"


def is_user_normal(user):
    # type: (Dict) -> bool
    return (user["type"] == UserType.Normal and
            user["role"] != UserRole.Visitor)
