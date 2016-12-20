#!/usr/bin/python
# -*- coding: utf-8 -*-
import json


class RTMMessageType(object):
    """types of Message of Real Time Message
    """
    Unknown = "unknown"
    Ping = "ping"
    Pong = "pong"
    Reply = "reply"
    Ok = "ok"
    P2PMessage = "message"
    P2PTyping = "typing"
    ChannelMessage = "channel_message"
    ChannelTyping = "channel_typing"
    UpdateUserConnection = "update_user_connection"


class RTMMessage(object):
    """Message of Real Time Message
    """
    def __init__(self, data):
        """
        Args:
            data(dict): message content

        Raises:
            TypeError: if data is not dict
        """
        if not isinstance(data, dict):
            raise TypeError
        self._data = data

    def __setitem__(self, name, value):
        self._data[name] = value

    def __getitem__(self, name):
        return self._data[name]

    def __contains__(self, name):
        return name in self._data

    def reply(self, text):
        """Replys a text message

        Args:
            text(str): message content

        Returns:
            RTMMessage
        """
        data = {"text": text, "vchannel_id": self["vchannel_id"]}
        if self.is_p2p():
            data["type"] = RTMMessageType.P2PMessage
            data["to_uid"] = self["uid"]
        else:
            data["type"] = RTMMessageType.ChannelMessage
            data["channel_id"] = self["channel_id"]
        return RTMMessage(data)

    def refer(self, text):
        """Refers current message and replys a new message

        Args:
            text(str): message content

        Returns:
            RTMMessage
        """
        data = self.reply(text)
        data["refer_key"] = self["key"]
        return data

    def is_p2p(self):
        """
        Returns:
            True if current message is p2p message
        """
        t = self["type"]
        return (t == RTMMessageType.P2PMessage or
                t == RTMMessageType.P2PTyping)

    def is_chat_message(self):
        """
        Returns:
            True if current message is chatting message
        """
        t = self["type"]
        return (t == RTMMessageType.P2PMessage or
                t == RTMMessageType.ChannelMessage)

    def is_from(self, user):
        """Checks if current message is sent by user

        Args:
            user(User)

        Returns:
            True if current message is sent by the user
        """
        return self["uid"] == user["id"]

    def to_json(self):
        """Transfers current message to json

        Returns:
            json
        """
        return json.dumps(self._data)
