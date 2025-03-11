"""
Python module generated from Java source file dev.magicmq.pyspigot.manager.redis.ClientType

Java source file obtained from artifact pyspigot-core version 0.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.manager.redis import *
from dev.magicmq.pyspigot.manager.redis.client import RedisCommandClient
from dev.magicmq.pyspigot.manager.redis.client import RedisPubSubClient
from dev.magicmq.pyspigot.manager.redis.client import ScriptRedisClient
from enum import Enum
from typing import Any, Callable, Iterable, Tuple


class ClientType(Enum):
    """
    Utility enum to represent different types of redis clients available for scripts to use.
    """

    BASIC = (ScriptRedisClient)
    """
    A basic client type, used for initiating a standard RedisClient for further custom usage.
    """
    COMMAND = (RedisCommandClient)
    """
    A command client type, used for executing redis commands.
    """
    PUB_SUB = (RedisPubSubClient)
    """
    A pub/sub client type, used for publishing and subscribing to redis messaging.
    """


    def getClientClass(self) -> type["ScriptRedisClient"]:
        """
        Get the class that pertains to the client type. Will be a subclass of ScriptRedisClient

        Returns
        - The class associated with the client type
        """
        ...
