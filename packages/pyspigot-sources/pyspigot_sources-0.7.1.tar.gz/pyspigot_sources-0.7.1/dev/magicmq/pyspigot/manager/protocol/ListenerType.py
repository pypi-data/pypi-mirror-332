"""
Python module generated from Java source file dev.magicmq.pyspigot.manager.protocol.ListenerType

Java source file obtained from artifact pyspigot version 0.7.1

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.manager.protocol import *
from enum import Enum
from typing import Any, Callable, Iterable, Tuple


class ListenerType(Enum):
    """
    An enum representing the type of protocol listener that a script has registered.
    """

    NORMAL = 0
    """
    A normal listner.
    """
    ASYNCHRONOUS = 1
    """
    An asynchronous listener.
    """
    ASYNCHRONOUS_TIMEOUT = 2
    """
    An asynchronous timeout listener.
    """
