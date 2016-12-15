#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests


def validate(data):
    """Validates incoming data

    Args:
        data(dict): the incoming data

    Returns:
        True if the data is valid

    Raises:
        ValueError: the data is not valid
    """
    if not isinstance(data, dict):
        raise ValueError("data should be dict")
    if "text" not in data or not isinstance(data["text"],
                                            str) or len(data["text"]) < 1:
        raise ValueError("text field is required and should not be empty")
    if "markdown" in data and not isinstance(data["markdown"], bool):
        raise ValueError("markdown field should be bool")

    if "attachments" in data:
        if not isinstance(data["attachments"], list):
            raise ValueError("attachments field should be list")
        for attachment in data["attachments"]:
            if "text" not in attachment and "title" not in attachment:
                raise ValueError("text or title is required in attachment")

    return True


def send(url, data):
    """Sends an incoming message

    Args:
        url(str): the incoming hook url
        data(dict): the sending data

    Returns:
        requests.Response
    """
    validate(data)
    return requests.post(url, json=data)
