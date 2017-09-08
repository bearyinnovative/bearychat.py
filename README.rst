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
