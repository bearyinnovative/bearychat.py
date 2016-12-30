.. bearychat.py documentation master file, created by
   sphinx-quickstart on Fri Dec 30 15:17:02 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

BearyChat.py
============

BearyChat.py is a SDK for `BearyChat <https://bearychat.com>`_.

Quick links
-----------

* `Source(GitHub) <https://github.com/bearyinnovative/bearychat.py>`_
* `BearyChat Integrations <https://bearychat.com/integrations>`_

Hello, world
------------

Here is a simple "Hello, world" example app for BearyChat `Incoming <https://bearychat.com/integrations/incoming>`_::

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

Installation
------------

**Automatic installation**::

  pip install bearychat

BearyChat.py is listed in `PyPI <https://pypi.python.org/pypi/bearychat>`_, and
can be installed with ``pip`` or ``easy_install``.
  
**Prerequisites**: BearyChat.py runs on Python 2.6+ and Python 3.3+(`more <https://travis-ci.org/bearyinnovative/bearychat.py>`_). And HTTP library `request <https://github.com/kennethreitz/requests>`_ is required.

Documentation
-------------

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   guide

   releases

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Discussion and support
----------------------

You can report bugs on the `GitHub issue tracker <https://github.com/bearyinnovative/bearychat.py/issues>`_
