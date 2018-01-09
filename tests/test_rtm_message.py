from bearychat.rtm_message import RTMMessage, RTMMessageType


def test_is_mention_user():

    # testing channel message

    msg = RTMMessage({'type': RTMMessageType.ChannelMessage, 'text': 'foobar'})
    assert len(msg.mention_user_ids) == 0
    assert not msg.is_mention_user({'id': 'foobar'})

    msg = RTMMessage({
        'type': RTMMessageType.ChannelMessage,
        'text': '@<===> '
    })
    assert len(msg.mention_user_ids) == 0

    msg = RTMMessage({
        'type': RTMMessageType.ChannelMessage,
        'text': 'hello @<==42=> '
    })
    assert len(msg.mention_user_ids) == 1
    assert msg.is_mention_user({'id': '=42'})

    msg = RTMMessage({
        'type': RTMMessageType.ChannelMessage,
        'text': 'hello @<==42=> , and @<==bw52O=> '
    })
    assert len(msg.mention_user_ids) == 2
    assert msg.is_mention_user({'id': '=42'})
    assert msg.is_mention_user({'id': '=bw52O'})

    msg = RTMMessage({
        'type': RTMMessageType.ChannelMessage,
        'text': '@<==42=> , and @<==42=> '
    })
    assert len(msg.mention_user_ids) == 1
    assert msg.is_mention_user({'id': '=42'})
    assert not msg.is_mention_user({'id': '=bw52O'})

    # testing p2p message

    msg = RTMMessage({'type': RTMMessageType.P2PMessage, 'text': 'foobar'})
    assert len(msg.mention_user_ids) == 0
    assert not msg.is_mention_user({'id': 'foobar'})

    msg = RTMMessage({
        'type': RTMMessageType.P2PMessage,
        'text': '@<===> '
    })
    assert len(msg.mention_user_ids) == 0

    msg = RTMMessage({
        'type': RTMMessageType.P2PMessage,
        'text': 'hello @<==42=> '
    })
    assert len(msg.mention_user_ids) == 1
    assert msg.is_mention_user({'id': '=42'})

    msg = RTMMessage({
        'type': RTMMessageType.P2PMessage,
        'text': 'hello @<==42=> , and @<==bw52O=> '
    })
    assert len(msg.mention_user_ids) == 2
    assert msg.is_mention_user({'id': '=42'})
    assert msg.is_mention_user({'id': '=bw52O'})

    msg = RTMMessage({
        'type': RTMMessageType.P2PMessage,
        'text': '@<==42=> , and @<==42=> '
    })
    assert len(msg.mention_user_ids) == 1
    assert msg.is_mention_user({'id': '=42'})
    assert not msg.is_mention_user({'id': '=bw52O'})

    # testing other type message

    msg = RTMMessage({'type': RTMMessageType.Ping})
    assert not msg.is_mention_user({'id': '=bw52O'})

    msg = RTMMessage({'type': RTMMessageType.P2PTyping})
    assert not msg.is_mention_user({'id': '=bw52O'})
