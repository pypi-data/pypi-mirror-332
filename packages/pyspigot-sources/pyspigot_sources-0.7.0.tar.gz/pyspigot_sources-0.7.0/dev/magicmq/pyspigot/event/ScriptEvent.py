"""
Python module generated from Java source file dev.magicmq.pyspigot.event.ScriptEvent

Java source file obtained from artifact pyspigot version 0.7.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.event import *
from dev.magicmq.pyspigot.manager.script import Script
from org.bukkit.event import Event
from org.bukkit.event import HandlerList
from typing import Any, Callable, Iterable, Tuple


class ScriptEvent(Event):
    """
    Script event superclass. All script events inherit from this class.
    """

    def __init__(self, script: "Script", async: bool):
        """
        Arguments
        - script: The script associated with this event
        - async: Whether the event is asynchronous
        """
        ...


    def getScript(self) -> "Script":
        """
        Get the script associated with this event.

        Returns
        - The script associated with this event
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
