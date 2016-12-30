Incoming
--------

`Incoming <https://bearychat.com/integrations/incoming>`_ is an integration of bearychat.

Examples
~~~~~~~~

Here is a simple incoming workflow::

  from bearychat import incoming

  data = {
      "text": "hello, **world**",
      "markdown": True,
      "notification": "Hello, BearyChat in Notification",
      "channel": "testing"
  }

  resp = incoming.send(
       "https://hook.bearychat.com/=bw52O/incoming/token",
       data)
