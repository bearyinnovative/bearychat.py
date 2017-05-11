import json


class RTMMessageType(object):
    """RTM Message constants"""

    Unknown = 'unknown'
    Ping = 'ping'
    Pong = 'pong'
    Reply = 'reply'
    Ok = 'ok'
    P2PMessage = 'message'
    P2PTyping = 'typing'
    ChannelMessage = 'channel_message'
    ChannelTyping = 'channel_typing'
    UpdateUserConnection = 'update_user_connection'


class RTMMessage(object):
    """RTM Message

    Args:
        data(dict): message dict
    """

    def __init__(self, data):
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
        data = {'text': text, 'vchannel_id': self['vchannel_id']}
        if self.is_p2p():
            data['type'] = RTMMessageType.P2PMessage
            data['to_uid'] = self['uid']
        else:
            data['type'] = RTMMessageType.ChannelMessage
            data['channel_id'] = self['channel_id']
        return RTMMessage(data)

    def refer(self, text):
        """Refers current message and replys a new message

        Args:
            text(str): message content

        Returns:
            RTMMessage
        """
        data = self.reply(text)
        data['refer_key'] = self['key']
        return data

    def is_p2p(self):
        """
        Returns:
            True if current message is p2p message
        """
        return self['type'] in (RTMMessageType.P2PMessage,
                                RTMMessageType.P2PTyping)

    def is_chat_message(self):
        """
        Returns:
            True if current message is chatting message
        """
        return self['type'] in (RTMMessageType.P2PMessage,
                                RTMMessageType.ChannelMessage)

    def is_from(self, user):
        """Checks if current message is sent by user

        Args:
            user(User)

        Returns:
            True if current message is sent by the user
        """
        return self['id'] == user.get('id')

    def to_json(self):
        """Transfers current message to json

        Returns:
            json
        """
        return json.dumps(self._data)
