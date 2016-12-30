#!/usr/bin/python
# -*- coding: utf-8 -*-


class Team(dict):
    def __init__(self, data):
        if not isinstance(data, dict):
            raise TypeError
        self._data = data

    def __setitem__(self, name, value):
        self._data[name] = value

    def __getitem__(self, name):
        return self._data[name]


class UserType(object):
    Normal = "normal"
    Assistant = "assistant"
    Hubot = "hubot"


class UserRole(object):
    Owner = "owner"
    Admin = "admin"
    Normal = "normal"
    Visitor = "visitor"


class User(object):
    def __init__(self, data):
        if not isinstance(data, dict):
            raise TypeError
        self._data = data

    def __setitem__(self, name, value):
        self._data[name] = value

    def __getitem__(self, name):
        return self._data[name]

    def is_online(self):
        return self["conn"] == "connected"

    def is_normal(self):
        return (self["type"] == UserType.Normal and
                self["role"] != UserRole.Visitor)


class Channel(object):
    def __init__(self, data):
        if not isinstance(data, dict):
            raise TypeError
        self._data = data

    def __setitem__(self, name, value):
        self._data[name] = value

    def __getitem__(self, name):
        return self._data[name]
