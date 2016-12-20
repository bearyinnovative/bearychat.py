#!/usr/bin/python
# -*- coding: utf-8 -*-
from requests import Request, Session
from .rtm_client_service import RTMChannel, RTMCurrentTeam, RTMUser
from .model import User


class RTMResponse(object):
    """Response of Real Time Message

    Attributes:
        resp(requests.Response): HTTP response object
        data(dict): the received data
    """
    def __init__(self, http_resp):
        self.resp = http_resp
        try:
            self.data = self.resp.json()
        except:
            self.data = {}

    def is_ok(self):
        """
        Returns:
            bool: True if the response is valid
        """
        return self.resp.status_code == 200 and self.data.get("code") == 0

    def is_fail(self):
        return not self.is_ok()


class RTMClient(object):
    """Real Time Message client

    Attributes:
        current_team(RTMCurrentTeam): service of current team
        user(RTMUser): service of current user
        channel(RTMChannel): service of current channel
    """
    def __init__(self, token, api_base="https://rtm.bearychat.com"):
        """
        Args:
            token(str): rtm token
            api_base(str): api url base
        """
        self._token = token
        self._api_base = api_base
        self.current_team = RTMCurrentTeam(self)
        self.user = RTMUser(self)
        self.channel = RTMChannel(self)

    def start(self):
        """Gets the rtm ws_host and user information

        Returns:
            None if request failed,
            else a dict containing "user"(User) and "ws_host"
        """
        resp = self.post("start")
        if resp.is_fail() or "result" not in resp.data:
            return None
        return {
            "user": User(resp.data["result"]["user"]),
            "ws_host": resp.data["result"]["ws_host"]
        }

    def do(self,
           resource,
           method,
           params=None,
           data=None,
           json=None,
           headers=None):
        """Does the request job

        Args:
            resource(str): resource uri(relative path)
            method(str): HTTP method
            params(dict): uri queries
            data(dict): HTTP body(form)
            json(dict): HTTP body(json)
            headers(dict): HTTP headers

        Returns:
            RTMResponse
        """
        uri = "{0}/{1}".format(self._api_base, resource)
        if not params:
            params = {}
        params.update({"token": self._token})

        req = Request(
            method=method,
            url=uri,
            params=params,
            headers=headers,
            data=data,
            json=json)
        s = Session()
        prepped = s.prepare_request(req)
        resp = s.send(prepped)

        return RTMResponse(resp)

    def get(self, resource, params=None, headers=None):
        """Sends a GET request

        Returns:
            RTMResponse
        """
        return self.do(resource, "GET", params=params, headers=headers)

    def post(self, resource, data=None, json=None):
        """Sends a POST request

        Returns:
            RTMResponse
        """
        return self.do(resource, "POST", data=data, json=json)
