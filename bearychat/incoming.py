import sys
PY3 = sys.version_info[0] == 3

import requests


if PY3:
    _string_types = str,
else:
    _string_types = basestring,  # noqa


def validate(data):
    """Validates incoming data

    Args:
        data(dict): the incoming data

    Returns:
        True if the data is valid

    Raises:
        ValueError: the data is not valid
    """
    text = data.get('text')
    if not isinstance(text, _string_types) or len(text) == 0:
        raise ValueError('text field is required and should not be empty')

    if 'markdown' in data and not type(data['markdown']) is bool:
        raise ValueError('markdown field should be bool')

    if 'attachments' in data:
        if not isinstance(data['attachments'], (list, tuple)):
            raise ValueError('attachments field should be list or tuple')

        for attachment in data['attachments']:
            if 'text' not in attachment and 'title' not in attachment:
                raise ValueError('text or title is required in attachment')

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
