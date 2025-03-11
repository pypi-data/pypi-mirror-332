"""
Python module generated from Java source file dev.magicmq.pyspigot.manager.redis.ScriptPubSubListener

Java source file obtained from artifact pyspigot version 0.7.1

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.manager.redis import *
from io.lettuce.core.pubsub import RedisPubSubListener
from org.python.core import Py
from org.python.core import PyFunction
from org.python.core import PyObject
from typing import Any, Callable, Iterable, Tuple


class ScriptPubSubListener(RedisPubSubListener):
    """
    A wrapper class that wraps the RedisPubSubListener from lettuce for use by scripts.

    See
    - io.lettuce.core.pubsub.RedisPubSubListener
    """

    def __init__(self, function: Callable, channel: str):
        """
        Arguments
        - function: The function that should be called when a message is received on the given channel
        - channel: The channel to listen on
        """
        ...


    def message(self, channel: str, message: str) -> None:
        """
        Called internally when a message is received on the given channel.

        Arguments
        - channel: The channel on which the message was received
        - message: The message that was received
        """
        ...


    def message(self, s: str, k1: str, s2: str) -> None:
        """
        Implemented from RedisPubSubListener, but unused.
        """
        ...


    def subscribed(self, s: str, l: int) -> None:
        """
        Implemented from RedisPubSubListener, but unused.
        """
        ...


    def psubscribed(self, s: str, l: int) -> None:
        """
        Implemented from RedisPubSubListener, but unused.
        """
        ...


    def unsubscribed(self, s: str, l: int) -> None:
        """
        Implemented from RedisPubSubListener, but unused.
        """
        ...


    def punsubscribed(self, s: str, l: int) -> None:
        """
        Implemented from RedisPubSubListener, but unused.
        """
        ...


    def getChannel(self) -> str:
        """
        Implemented from RedisPubSubListener, but unused.
        """
        ...


    def toString(self) -> str:
        """
        Prints a representation of this ScriptPubSubListener in string format, including the channel being listened to.

        Returns
        - A string representation of the ScriptPubSubListener
        """
        ...
