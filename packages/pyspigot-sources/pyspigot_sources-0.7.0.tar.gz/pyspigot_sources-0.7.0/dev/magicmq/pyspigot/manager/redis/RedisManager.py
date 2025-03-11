"""
Python module generated from Java source file dev.magicmq.pyspigot.manager.redis.RedisManager

Java source file obtained from artifact pyspigot version 0.7.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.manager.redis import *
from dev.magicmq.pyspigot.manager.redis.client import RedisCommandClient
from dev.magicmq.pyspigot.manager.redis.client import RedisPubSubClient
from dev.magicmq.pyspigot.manager.redis.client import ScriptRedisClient
from dev.magicmq.pyspigot.manager.script import Script
from dev.magicmq.pyspigot.util import ScriptUtils
from io.lettuce.core import ClientOptions
from io.lettuce.core import RedisConnectionException
from io.lettuce.core import RedisURI
from java.util.concurrent import CompletableFuture
from typing import Any, Callable, Iterable, Tuple


class RedisManager:
    """
    Manager to interface with remote redis servers. Used by scripts to subscribe to pub/sub messaging and publish messages.
    """

    def newRedisURI(self) -> "RedisURI.Builder":
        """
        Get a new RedisURI builder for use when opening a new script redis client.

        Returns
        - A io.lettuce.core.RedisURI.Builder object used to build a URI with connection information
        """
        ...


    def newClientOptions(self) -> "ClientOptions.Builder":
        """
        Get a new client options builder for use when opening a new script redis client.

        Returns
        - A io.lettuce.core.ClientOptions.Builder object used to build ClientOptions for the RedisClient
        """
        ...


    def openRedisClient(self, clientType: "ClientType", ip: str, port: str, password: str) -> "ScriptRedisClient":
        """
        Initialize a new RedisPubSubClient with a connection to a remote redis server with the specified ip, port, and password, using the default client options. The connection to the remote redis server will be opened automatically when the client is created.
        
        **Note:** This should be called from scripts only!

        Arguments
        - clientType: The type of redis client to open, such as pub/sub or command
        - ip: The IP of the redis server to connect to
        - port: The port of the redis server to connect to
        - password: The password for the redis server

        Returns
        - A ScriptRedisClient representing a client that is connected to the remote redis server
        """
        ...


    def openRedisClient(self, clientType: "ClientType", ip: str, port: str, password: str, clientOptions: "ClientOptions") -> "ScriptRedisClient":
        """
        Initialize a new RedisPubSubClient with a connection to a remote redis server with the specified ip, port, and password, using the specified io.lettuce.core.ClientOptions. The connection to the remote redis server will be opened automatically when the client is created.
        
        **Note:** This should be called from scripts only!

        Arguments
        - clientType: The type of redis client to open, such as pub/sub or command
        - ip: The IP of the redis server to connect to
        - port: The port of the redis server to connect to
        - password: The password for the redis server
        - clientOptions: The io.lettuce.core.ClientOptions that should be used for the io.lettuce.core.RedisClient

        Returns
        - A ScriptRedisClient representing a client that is connected to the remote redis server
        """
        ...


    def openRedisClient(self, clientType: "ClientType", redisURI: "RedisURI") -> "ScriptRedisClient":
        """
        Initialize a new RedisPubSubClient with a connection to a remote redis server with the specified io.lettuce.core.RedisURI. The connection to the remote redis server will be opened automatically when the client is created.
        
        **Note:** This should be called from scripts only!

        Arguments
        - clientType: The type of redis client to open, such as pub/sub or command
        - redisURI: The URI specifying the connection details to the redis server

        Returns
        - A ScriptRedisClient representing a client that is connected to the remote redis server
        """
        ...


    def openRedisClient(self, clientType: "ClientType", redisURI: "RedisURI", clientOptions: "ClientOptions") -> "ScriptRedisClient":
        """
        Initialize a new RedisPubSubClient with a connection to a remote redis server with the specified io.lettuce.core.RedisURI and io.lettuce.core.ClientOptions. The connection to the remote redis server will be opened automatically when the client is created.
        
        **Note:** This should be called from scripts only!

        Arguments
        - clientType: The type of redis client to open, such as pub/sub or command
        - redisURI: The URI specifying the connection details to the redis server
        - clientOptions: The ClientOptions that should be used for the io.lettuce.core.RedisClient

        Returns
        - A ScriptRedisClient representing a client that is connected to the remote redis server
        """
        ...


    def closeRedisClient(self, client: "ScriptRedisClient") -> None:
        """
        Close the specified ScriptRedisClient synchronously. This method will block until the redis client is closed.
        
        **Note:** This should be called from scripts only!

        Arguments
        - client: The client to close
        """
        ...


    def closeRedisClientAsync(self, client: "ScriptRedisClient") -> "CompletableFuture"["Void"]:
        """
        Close the specified ScriptRedisClient asynchronously, without blocking.
        
        **Note:** This should be called from scripts only!

        Arguments
        - client: The client to close

        Returns
        - A CompletableFuture that completes when closing the client is finished
        """
        ...


    def closeRedisClients(self, script: "Script", async: bool) -> None:
        """
        Close all ScriptRedisClients belonging to a script.

        Arguments
        - script: The script whose ScriptRedisClients should be closed
        - async: Whether the client should be closed asynchronously
        """
        ...


    def getRedisClients(self, script: "Script") -> list["ScriptRedisClient"]:
        """
        Get all open ScriptRedisClients belonging to a script.

        Arguments
        - script: The script to get ScriptRedisClients from

        Returns
        - A List of ScriptRedisClient containing all clients associated with the script. Will return an empty list if there are no clients associated with the script
        """
        ...


    def getRedisClients(self, script: "Script", type: "ClientType") -> list["ScriptRedisClient"]:
        ...


    @staticmethod
    def get() -> "RedisManager":
        """
        Get the singleton instance of this RedisManager.

        Returns
        - The instance
        """
        ...
