"""
Python module generated from Java source file dev.magicmq.pyspigot.manager.redis.client.RedisCommandClient

Java source file obtained from artifact pyspigot version 0.7.1

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.manager.redis.client import *
from dev.magicmq.pyspigot.manager.script import Script
from io.lettuce.core import ClientOptions
from io.lettuce.core import RedisURI
from io.lettuce.core.api import StatefulRedisConnection
from io.lettuce.core.api.async import RedisAsyncCommands
from io.lettuce.core.api.sync import RedisCommands
from typing import Any, Callable, Iterable, Tuple


class RedisCommandClient(ScriptRedisClient):
    """
    Extension of the ScriptRedisClient that provides ability to issue commands.

    See
    - io.lettuce.core.api.StatefulRedisConnection
    """

    def __init__(self, script: "Script", redisURI: "RedisURI", clientOptions: "ClientOptions"):
        """
        Arguments
        - script: The script to which this ScriptRedisCommandClient belongs
        - redisURI: The URI that specifies the connection details to the server
        - clientOptions: The io.lettuce.core.ClientOptions that should be used for the RedisClient
        """
        ...


    def open(self) -> None:
        """

        """
        ...


    def getConnection(self) -> "StatefulRedisConnection"[str, str]:
        """
        Get the underlying connection for this RedisCommandClient.

        Returns
        - The connection associated with this RedisCommandClient
        """
        ...


    def getCommands(self) -> "RedisCommands"[str, str]:
        """
        Get the io.lettuce.core.api.sync.RedisCommands object for executing commands **synchronously**.

        Returns
        - A RedisCommands object for executing commands

        See
        - io.lettuce.core.api.StatefulRedisConnection.sync()
        """
        ...


    def getAsyncCommands(self) -> "RedisAsyncCommands"[str, str]:
        """
        Get the io.lettuce.core.api.async.RedisAsyncCommands object for executing commands **asynchronously**.

        Returns
        - A RedisAsyncCommands object for executing commands

        See
        - io.lettuce.core.api.StatefulRedisConnection.async()
        """
        ...


    def toString(self) -> str:
        """
        Prints a representation of this RedisCommandClient in string format, including listeners

        Returns
        - A string representation of the RedisCommandClient
        """
        ...
