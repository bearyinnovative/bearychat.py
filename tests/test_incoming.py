#!/usr/bin/python
# -*- coding: utf-8 -*-
import pytest
from bearychat.incoming import validate


def test_validate_success(new_incoming):
    assert validate(new_incoming) is True


def test_validate_data_type(new_incoming):
    assert validate(new_incoming) is True
    ts = [list, str, int, float, bool]
    for t in ts:
        incoming = t()
        with pytest.raises(ValueError, message="data should be dict"):
            validate(incoming)


def test_validate_markdown_field(new_incoming):
    ts = [list, str, int, float, dict]
    for t in ts:
        new_incoming["markdown"] = t()
        with pytest.raises(
                ValueError, message="markdown field should be bool"):
            validate(new_incoming)

    new_incoming["markdown"] = True
    assert validate(new_incoming) is True


def test_validate_text_field(new_incoming):
    ts = [list, int, float, dict, bool, str]
    for t in ts:
        new_incoming["text"] = t()
        with pytest.raises(
                ValueError,
                message="text field is required and should not be empty"):
            validate(new_incoming)
    new_incoming["text"] = "testing"
    assert validate(new_incoming) is True


def test_validate_attachments(new_incoming):
    ts = [int, float, dict, bool, str]
    for t in ts:
        new_incoming["attachments"] = t()
        with pytest.raises(
                ValueError, message="attachments field should be list"):
            validate(new_incoming)
    new_incoming["attachments"] = [{
        "color": "#ffa500",
        "images": [{
            "url": "http://img3.douban.com/icon/ul15067564-30.jpg"
        }]
    }]

    with pytest.raises(
            ValueError, message="text or title is required in attachment"):
        validate(new_incoming)

    new_incoming["attachments"] = [{
        "title": "testing",
        "color": "#ffa500",
        "images": [{
            "url": "http://img3.douban.com/icon/ul15067564-30.jpg"
        }]
    }]
    assert validate(new_incoming) is True

    new_incoming["attachments"] = [{
        "text": "testing",
        "color": "#ffa500",
        "images": [{
            "url": "http://img3.douban.com/icon/ul15067564-30.jpg"
        }]
    }]
    assert validate(new_incoming) is True
