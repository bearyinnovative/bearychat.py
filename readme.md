Python SDK for BearyChat
====

## Requirements
- `python`: 2.7/3.5
- [requests](https://github.com/kennethreitz/requests)

## Installation

```bash
$ git clone https://github.com/bearyinnovative/pybearychat.git
$ cd pybearychat
$ python setup.py install
```

## Examples

### Incoming

```python

from bearychat import incoming


def main():
    data = {
        "text": "hello, **world**",
        "markdown": True,
        "noification": "Hello, BearyChat in Notification",
        "channel": "testing"
    }

    resp = incoming.send(
        "https://hook.bearychat.com/****/incoming/*****",
        data)


if __name__ == "__main__":
    main()
```

### Real Time Message

## License
> MIT
