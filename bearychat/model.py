#!/usr/bin/python
# -*- coding: utf-8 -*-

from .utils import accepts


class UserType(object):
    Normal = "normal"
    Assistant = "assistant"
    Hubot = "hubot"


class UserRole(object):
    Owner = "owner"
    Admin = "admin"
    Normal = "normal"
    Visitor = "visitor"


@accepts(dict)
def is_user_online(user):
    return user["conn"] == "connected"


@accepts(dict)
def is_user_normal(user):
    return (user["type"] == UserType.Normal and
            user["role"] != UserRole.Visitor)
