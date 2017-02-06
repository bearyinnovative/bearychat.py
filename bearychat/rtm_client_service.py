#!/usr/bin/python
# -*- coding: utf-8 -*-


class RTMServiceError(RuntimeError):
    def __init__(self, message, err_data):
        super(RTMServiceError, self).__init__(message)
        self.err_data = err_data


class RTMService(object):
    """service of Real Time Message
    """

    def __init__(self, rtm_client):
        self._rtm_client = rtm_client


class RTMCurrentTeam(RTMService):
    """
    """

    def info(self):
        """Gets current team infomation

        Returns:
            Team if success

        Throws:
            RTMServiceError when request failed
        """
        resp = self._rtm_client.get("v1/current_team.info")
        if resp.is_fail():
            raise RTMServiceError("Failed to get current team infomation",
                                  resp)
        return resp.data["result"]

    def members(self):
        """Gets members of current team

        Returns:
            list of User

        Throws:
            RTMServiceError when request failed
        """
        resp = self._rtm_client.get("v1/current_team.members?all=true")
        if resp.is_fail():
            raise RTMServiceError("Failed to get members of current team",
                                  resp)
        members = []
        for member in resp.data["result"]:
            members.append(member)
        return members

    def channels(self):
        """Gets channels of current team

        Returns:
            list of Channel

        Throws:
            RTMServiceError when request failed
        """
        resp = self._rtm_client.get("v1/current_team.channels")
        if resp.is_fail():
            raise RTMServiceError("Failed to get channels of current team",
                                  resp)
        channels = []
        for channel in resp.data["result"]:
            channels.append(channel)
        return channels


class RTMUser(RTMService):
    def info(self, user_id):
        """Gets user information by user id

        Args:
            user_id(int): the id of user

        Returns:
            User

        Throws:
            RTMServiceError when request failed
        """
        resp = self._rtm_client.get("v1/user.info?user_id={0}".format(user_id))
        if resp.is_fail():
            raise RTMServiceError("Failed to get user information", resp)
        return resp.data["result"]


class RTMChannel(RTMService):
    def info(self, channel_id):
        """Gets channel information by channel id

        Args:
            channel_id(int): the id of channel

        Returns:
            Channel

        Throws:
            RTMServiceError when request failed
        """
        resp = self._rtm_client.get("v1/channel.info?channel_id={0}".format(
            channel_id))
        if resp.is_fail():
            raise RTMServiceError("Failed to get channel information", resp)
        return resp.data["result"]
