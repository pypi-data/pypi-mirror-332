"""
Python module generated from Java source file dev.magicmq.pyspigot.event.ScriptUnloadEvent

Java source file obtained from artifact pyspigot version 0.5.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.event import *
from dev.magicmq.pyspigot.manager.script import Script
from org.bukkit.event import HandlerList
from typing import Any, Callable, Iterable, Tuple


class ScriptUnloadEvent(ScriptEvent):
    """
    Called when a script is unloaded.
    """

    def __init__(self, script: "Script", error: bool):
        """
        Arguments
        - script: The script that was unloaded
        - error: Whether the script was unloaded due to an error
        """
        ...


    def isError(self) -> bool:
        """
        Get if this unload event was due to a script error.

        Returns
        - True if the script was unloaded due to an error/exception, False if otherwise
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
