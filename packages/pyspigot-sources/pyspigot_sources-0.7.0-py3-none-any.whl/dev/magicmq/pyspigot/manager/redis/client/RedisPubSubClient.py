"""
Python module generated from Java source file dev.magicmq.pyspigot.manager.redis.client.RedisPubSubClient

Java source file obtained from artifact pyspigot version 0.7.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.manager.redis import ScriptPubSubListener
from dev.magicmq.pyspigot.manager.redis.client import *
from dev.magicmq.pyspigot.manager.script import Script
from io.lettuce.core import ClientOptions
from io.lettuce.core import RedisFuture
from io.lettuce.core import RedisURI
from io.lettuce.core.pubsub import StatefulRedisPubSubConnection
from java.util import Iterator
from org.python.core import PyFunction
from typing import Any, Callable, Iterable, Tuple


class RedisPubSubClient(ScriptRedisClient):
    """
    Extension of the ScriptRedisClient that provides pub/sub messaging capabilities.

    See
    - io.lettuce.core.pubsub.StatefulRedisPubSubConnection
    """

    def __init__(self, script: "Script", redisURI: "RedisURI", clientOptions: "ClientOptions"):
        """
        Arguments
        - script: The script to which this RedisPubSubClient belongs
        - redisURI: The URI that specifies the connection details to the server
        - clientOptions: The io.lettuce.core.ClientOptions that should be used for the RedisClient
        """
        ...


    def open(self) -> None:
        """

        """
        ...


    def getConnection(self) -> "StatefulRedisPubSubConnection"[str, str]:
        """
        Get the underlying connection for this RedisPubSubClient.

        Returns
        - The connection associated with this RedisPubSubClient
        """
        ...


    def registerListener(self, function: Callable, channel: str) -> "ScriptPubSubListener":
        """
        Register a new synchronous listener.
        
        **Note:** This should be called from scripts only!

        Arguments
        - function: The function that should be called when a message on the specified channel is received
        - channel: The channel to listen on

        Returns
        - A ScriptPubSubListener representing the listener that was registered

        See
        - RedisPubSubClient.registerSyncListener(PyFunction, String)
        """
        ...


    def registerSyncListener(self, function: Callable, channel: str) -> "ScriptPubSubListener":
        """
        Register a new synchronous listener.
        
        **Note:** This should be called from scripts only!

        Arguments
        - function: The function that should be called when a message on the specified channel is received
        - channel: The channel to listen on

        Returns
        - A ScriptPubSubListener representing the listener that was registered
        """
        ...


    def registerAsyncListener(self, function: Callable, channel: str) -> "ScriptPubSubListener":
        """
        Register a new asynchronous listener.
        
        **Note:** This should be called from scripts only!

        Arguments
        - function: The function that should be called when a message on the specified channel is received
        - channel: The channel to listen on

        Returns
        - A ScriptPubSubListener representing the listener that was registered
        """
        ...


    def unregisterListener(self, listener: "ScriptPubSubListener") -> None:
        """
        Unregister the specified listener.
        
        **Note:** This should be called from scripts only!

        Arguments
        - listener: The listener to unregister
        """
        ...


    def unregisterListeners(self, channel: str) -> None:
        """
        Unregister all listeners (both synchronous and asynchronous) on the given channel
        
        **Note:** This should be called from scripts only!

        Arguments
        - channel: The channel on which all listeners should be unregistered
        """
        ...


    def publish(self, channel: str, message: str) -> "Long":
        """
        Synchronously publish a message to the given channel
        
        **Note:** This should be called from scripts only!

        Arguments
        - channel: The channel on which the message should be published
        - message: The message to publish

        Returns
        - The number of clients that received the message
        """
        ...


    def publishSync(self, channel: str, message: str) -> "Long":
        """
        Synchronously publish a message to the given channel
        
        **Note:** This should be called from scripts only!

        Arguments
        - channel: The channel on which the message should be published
        - message: The message to publish

        Returns
        - The number of clients that received the message
        """
        ...


    def publishAsync(self, channel: str, message: str) -> "RedisFuture"["Long"]:
        """
        Asynchronously publish a message to the given channel
        
        **Note:** This should be called from scripts only!

        Arguments
        - channel: The channel on which the message should be published
        - message: The message to publish
        """
        ...


    def toString(self) -> str:
        """
        Prints a representation of this RedisPubSubClient in string format, including listeners

        Returns
        - A string representation of the RedisPubSubClient
        """
        ...
