from bearychat.rtm_message import RTMMessage


def test_is_mention_user():
    msg = RTMMessage({"text": "foobar"})
    assert len(msg.mention_user_ids) == 0
    assert not msg.is_mention_user({"id": "foobar"})

    msg = RTMMessage({"text": "@<===> "})
    assert len(msg.mention_user_ids) == 0

    msg = RTMMessage({"text": "hello @<==42=> "})
    assert len(msg.mention_user_ids) == 1
    assert msg.is_mention_user({"id": "=42"})

    msg = RTMMessage({"text": "hello @<==42=> , and @<==bw52O=> "})
    assert len(msg.mention_user_ids) == 2
    assert msg.is_mention_user({"id": "=42"})
    assert msg.is_mention_user({"id": "=bw52O"})

    msg = RTMMessage({"text": "@<==42=> , and @<==42=> "})
    assert len(msg.mention_user_ids) == 1
    assert msg.is_mention_user({"id": "=42"})
    assert not msg.is_mention_user({"id": "=bw52O"})
