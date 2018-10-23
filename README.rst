========================
Python SDK for BearyChat
========================

|@BearyChat|
|Build Status|
|Development Status|
|Documentation Status|

`Documentation <http://bearychat.readthedocs.io/en/latest/?badge=latest>`_

Requirements
------------

- Python: 2.7/3.5
- `requests <https://github.com/kennethreitz/requests>`_

Installation
------------

Use pip to install bearychat SDK.

::

    $ pip install bearychat

or for development:

::

    $ git clone https://github.com/bearyinnovative/bearychat.py.git
    $ cd bearychat.py
    $ python setup.py install

Examples
--------

Incoming
~~~~~~~~

.. code:: python

    from bearychat import incoming

    def main():
        data = {
            "text": "hello, **world**",
            "markdown": True,
            "notification": "Hello, BearyChat in Notification",
            "channel": "testing"
        }

        resp = incoming.send(
            "https://hook.bearychat.com/=bw52O/incoming/token",
            data)

        print(resp.status_code)
        print(resp.text)


    if __name__ == "__main__":
        main()


Real Time Message
~~~~~~~~~~~~~~~~~

BearyChat SDK **DOES NOT** provide rtm loop, you should implement it with your
favorite websocket library.

A reference implmenetation can be found at `examples/rtm_loop.py <./examples/rtm_loop.py>`_

OpenApi
~~~~~~~
.. code:: python

    from bearychat import openapi
    
    client = openapi.Client('<your token>')
    message_query_param = {
        "vchannel_id": "=bw52O",
        "query": {
            "latest": {
                "limit": 1
            }
        }
    }
    client.message.query(json = message_query_param)

    """
    {u'messages': [{u'updated': u'2018-10-19T07:23:51.000+0000', u'attachments': [], u'is_channel': True, u'created': u'2018-10-19T07:23:51.000+0000', u'text': u'hello \u9080\u8bf7 \u80e1\u4f2f\u673a\u5668\u4eba \u52a0\u5165\u8be5\u8ba8\u8bba\u7ec4', u'created_ts': 1539933830697, u'subtype': u'info', u'team_id': u'=bwDBo', u'key': u'1539933830697.0487', u'refer_key': None, u'robot_id': None, u'fallback': None, u'vchannel_id': u'=bwPzN', u'uid': u'=bwZbY'}]}
    """

OpenApi Online Document: http://openapi.bearychat.help


Development
-----------

OpenAPI Client Building
~~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell

  $ ./scripts/gen_api.py > bearychat/openapi/_api.py


Using Other Libraries
---------------------

- `aiobearychat <https://github.com/mozillazg/aiobearychat>`_ By `@mozillazg <https://github.com/mozillazg>`_

User Demos
---------------------

- `Websocket sample <https://gist.github.com/ficapy/8948348d4b8ea2adb9e3e4e5237cb0a3>`_ By `@ficapy <https://github.com/ficapy>`_


License
-------

MIT


.. |@BearyChat| image:: http://openapi.beary.chat/badge.svg
   :target: http://openapi.beary.chat/join
.. |Build Status| image:: https://travis-ci.org/bearyinnovative/bearychat.py.svg
   :target: https://travis-ci.org/bearyinnovative/bearychat.py
.. |Development Status| image:: https://img.shields.io/badge/status-WIP-yellow.svg?style=flat-square
.. |Documentation Status| image:: https://readthedocs.org/projects/bearychat/badge/?version=latest
   :target: http://bearychat.readthedocs.io/en/latest/?badge=latest
