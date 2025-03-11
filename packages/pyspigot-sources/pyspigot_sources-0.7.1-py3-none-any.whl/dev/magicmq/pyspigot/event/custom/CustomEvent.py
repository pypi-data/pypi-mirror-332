"""
Python module generated from Java source file dev.magicmq.pyspigot.event.custom.CustomEvent

Java source file obtained from artifact pyspigot version 0.7.1

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.event import ScriptEvent
from dev.magicmq.pyspigot.event.custom import *
from dev.magicmq.pyspigot.util import ScriptUtils
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.python.core import Py
from org.python.core import PyObject
from typing import Any, Callable, Iterable, Tuple


class CustomEvent(ScriptEvent, Cancellable):
    """
    A custom event that scripts may instantiate and call for other plugins/scripts to listen to.
    """

    def __init__(self, name: str, data: Any):
        """
        
        **Note:** This class should be instantiated from scripts only!

        Arguments
        - name: The name of the event being created. Can be used to create subtypes of the generic custom event
        - data: The data to attach to the event
        """
        ...


    def __init__(self, name: str, data: Any, async: bool):
        """
        
        **Note:** This class should be instantiated from scripts only!

        Arguments
        - name: The name of the event being created. Can be used to create subtypes of the generic custom event
        - data: The data to attach to the event
        - async: Whether the event is being called from an asynchronous context
        """
        ...


    def getName(self) -> str:
        """
        Get the name of this event.

        Returns
        - The name of this event
        """
        ...


    def getData(self) -> Any:
        """
        Get the data attached to this event.

        Returns
        - The data attached to this event
        """
        ...


    def getDataAsType(self, clazz: str) -> "Object":
        """
        Attempt to convert the data attached to this event to a provided type.

        Arguments
        - clazz: The type that the data should be converted to

        Returns
        - An object of the specified type representing the converted data

        Raises
        - org.python.core.PyException: If the data could not be converted to the provided type
        """
        ...


    def getDataAsType(self, clazz: type["T"]) -> "T":
        """
        Attempt to convert the data attached to this event to a provided type.
        
        Type `<T>`: The type to which the data should be converted

        Arguments
        - clazz: The type that the data should be converted to

        Returns
        - An object of the specified type representing the converted data

        Raises
        - org.python.core.PyException: If the data could not be converted to the provided type
        """
        ...


    def isCancelled(self) -> bool:
        """

        """
        ...


    def setCancelled(self, cancelled: bool) -> None:
        """

        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
