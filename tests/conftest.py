#!/usr/bin/python
# -*- coding: utf-8 -*-
import pytest


@pytest.fixture(scope="module")
def new_incoming():
    return {
        "text": "**good** incoming",
        "markdown": True,
        "channel": "testing",
        "attachments": [{
            "title": "title_1",
            "text": "attachment_text",
            "color": "#ffa500",
            "images": [{
                "url": "http://img3.douban.com/icon/ul15067564-30.jpg"
            }]
        }]
    }
