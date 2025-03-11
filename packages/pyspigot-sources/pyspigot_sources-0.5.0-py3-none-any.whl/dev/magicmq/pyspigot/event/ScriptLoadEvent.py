"""
Python module generated from Java source file dev.magicmq.pyspigot.event.ScriptLoadEvent

Java source file obtained from artifact pyspigot version 0.5.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.event import *
from dev.magicmq.pyspigot.manager.script import Script
from org.bukkit.event import HandlerList
from typing import Any, Callable, Iterable, Tuple


class ScriptLoadEvent(ScriptEvent):
    """
    Called when a script is loaded. This event fires at the end of a load operation on a script. The event will not fire for scripts that fail to load. Therefore, it is safe to assume the script within this event is currently running.
    """

    def __init__(self, script: "Script"):
        """
        Arguments
        - script: The script that was loaded
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
