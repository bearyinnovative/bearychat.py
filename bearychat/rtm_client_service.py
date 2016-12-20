#!/usr/bin/python
# -*- coding: utf-8 -*-
from .model import Team, Channel, User


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
        """
        resp = self._rtm_client.get("v1/current_team.info")
        if resp.is_fail():
            return None
        return Team(resp.data["result"])

    def members(self):
        """Gets members of current team

        Returns:
            list of User
        """
        resp = self._rtm_client.get("v1/current_team.members?all=true")
        if resp.is_fail():
            return None
        members = []
        for member in resp.data["result"]:
            members.append(User(member))
        return members

    def channels(self):
        """Gets channels of current team

        Returns:
            list of Channel
        """
        resp = self._rtm_client.get("v1/current_team.channels")
        if resp.is_fail():
            return None
        channels = []
        for channel in resp.data["result"]:
            channels.append(Channel(channel))
        return channels


class RTMUser(RTMService):
    def info(self, user_id):
        """Gets user information by user id

        Args:
            user_id(int): the id of user

        Returns:
            User
        """
        resp = self._rtm_client.get("v1/user.info?user_id={0}".format(user_id))
        if resp.is_fail():
            return None
        return User(resp.data["result"])


class RTMChannel(RTMService):
    def info(self, channel_id):
        """Gets channel information by channel id

        Args:
            channel_id(int): the id of channel

        Returns:
            Channel
        """
        resp = self._rtm_client.get("v1/channel.info?channel_id={0}".format(
            channel_id))
        if resp.is_fail():
            return None
        return Channel(resp.data["result"])
