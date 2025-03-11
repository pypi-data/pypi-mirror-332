"""
Python module generated from Java source file dev.magicmq.pyspigot.manager.listener.ScriptEventExecutor

Java source file obtained from artifact pyspigot version 0.7.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.event import ScriptExceptionEvent
from dev.magicmq.pyspigot.manager.listener import *
from dev.magicmq.pyspigot.manager.script import Script
from dev.magicmq.pyspigot.manager.script import ScriptManager
from org.bukkit.event import Event
from org.bukkit.event import Listener
from org.bukkit.plugin import EventExecutor
from org.python.core import Py
from org.python.core import PyException
from org.python.core import PyObject
from typing import Any, Callable, Iterable, Tuple


class ScriptEventExecutor(EventExecutor):
    """
    Represents an event executor for script event listeners.

    See
    - org.bukkit.plugin.EventExecutor
    """

    def __init__(self, scriptEventListener: "ScriptEventListener", eventClass: type["Event"]):
        """
        Arguments
        - scriptEventListener: The ScriptEventListener associated with this ScriptEventExecutor
        - eventClass: The Bukkit event associated with this ScriptEventExecutor. Should be a Class of the Bukkit event
        """
        ...


    def execute(self, listener: "Listener", event: "Event") -> None:
        """
        Called internally when the event occurs.

        Arguments
        - listener: The listener associated with this EventExecutor
        - event: The event that occurred
        """
        ...
