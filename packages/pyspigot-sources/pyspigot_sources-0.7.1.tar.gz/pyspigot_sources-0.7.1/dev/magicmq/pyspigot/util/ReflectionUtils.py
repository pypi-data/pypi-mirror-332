"""
Python module generated from Java source file dev.magicmq.pyspigot.util.ReflectionUtils

Java source file obtained from artifact pyspigot version 0.7.1

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.util import *
from java.lang.reflect import Field
from java.lang.reflect import Method
from org.bukkit import Bukkit
from typing import Any, Callable, Iterable, Tuple


class ReflectionUtils:
    """
    A utility class to simplify reflection for working with CraftBukkit and NMS classes.
    """

    @staticmethod
    def getNMSClass(packageName: str, className: str) -> type[Any]:
        ...


    @staticmethod
    def getCraftBukkitClass(className: str) -> type[Any]:
        ...


    @staticmethod
    def getCraftBukkitClass(packageName: str, className: str) -> type[Any]:
        ...


    @staticmethod
    def getMethod(clazz: type[Any], methodName: str) -> "Method":
        ...


    @staticmethod
    def getField(clazz: type[Any], fieldName: str) -> "Field":
        ...
