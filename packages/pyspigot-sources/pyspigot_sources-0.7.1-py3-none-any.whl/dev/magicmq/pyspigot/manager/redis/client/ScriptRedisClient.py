"""
Python module generated from Java source file dev.magicmq.pyspigot.manager.redis.client.ScriptRedisClient

Java source file obtained from artifact pyspigot version 0.7.1

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.config import PluginConfig
from dev.magicmq.pyspigot.manager.redis.client import *
from dev.magicmq.pyspigot.manager.script import Script
from io.lettuce.core import ClientOptions
from io.lettuce.core import RedisClient
from io.lettuce.core import RedisURI
from java.util.concurrent import CompletableFuture
from typing import Any, Callable, Iterable, Tuple


class ScriptRedisClient:
    """
    A wrapper class that wraps the RedisClient from lettuce for use by scripts.

    See
    - io.lettuce.core.RedisClient
    """

    def __init__(self, script: "Script", redisURI: "RedisURI", clientOptions: "ClientOptions"):
        """
        Arguments
        - script: The script to which this ScriptRedisClient belongs
        - redisURI: The URI that specifies the connection details to the server
        - clientOptions: The io.lettuce.core.ClientOptions that should be used for the RedisClient
        """
        ...


    def open(self) -> None:
        """
        Initialize a new io.lettuce.core.RedisClient and open a connection to the remote redis server.
        """
        ...


    def close(self) -> None:
        """
        Close the open to the remote redis server synchronously, blocking if necessary.
        """
        ...


    def closeAsync(self) -> "CompletableFuture"["Void"]:
        """
        Close the open connection to the remote redis server asynchronously.

        Returns
        - A CompletableFuture that completes when the shutdown is finished
        """
        ...


    def getScript(self) -> "Script":
        """
        Get the script associated with this redis client.

        Returns
        - The script associated with this redis client.
        """
        ...


    def getClientId(self) -> int:
        """
        Get the ID of this redis client.

        Returns
        - The ID
        """
        ...


    def getRedisURI(self) -> "RedisURI":
        """
        Get the io.lettuce.core.RedisURI of this redis client.

        Returns
        - The RedisURI
        """
        ...


    def getClientOptions(self) -> "ClientOptions":
        """
        Get the io.lettuce.core.ClientOptions of this redis client.

        Returns
        - The ClientOptions
        """
        ...


    def getRedisClient(self) -> "RedisClient":
        """
        Get the underlying lettuce io.lettuce.core.RedisClient for this ScriptRedisClient.

        Returns
        - The RedisClient associated with this ScriptRedisClient
        """
        ...


    def toString(self) -> str:
        """
        Prints a representation of this ScriptRedisClient in string format

        Returns
        - A string representation of the ScriptRedisClient
        """
        ...
