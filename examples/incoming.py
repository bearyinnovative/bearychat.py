#!/usr/bin/python
# -*- coding: utf-8 -*-

from bearychat import incoming


def main():
    data = {
        "text": "hello, **world**",
        "markdown": True,
        "notification": "Hello, BearyChat in Notification",
        "channel": "testing"
    }

    resp = incoming.send(
        "https://hook.bearychat.com/****/incoming/*****",
        data)

    print(resp.status_code)
    print(resp.text)


if __name__ == "__main__":
    main()
