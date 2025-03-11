"""
Python module generated from Java source file dev.magicmq.pyspigot.event.ScriptExceptionEvent

Java source file obtained from artifact pyspigot version 0.7.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.event import *
from dev.magicmq.pyspigot.manager.script import Script
from org.bukkit.event import HandlerList
from org.python.core import PyException
from typing import Any, Callable, Iterable, Tuple


class ScriptExceptionEvent(ScriptEvent):
    """
    Called when a script throws an unhandled error/exception. This event could be called asynchronously if the exception occurred in an asynchronous context. To check if the event is asynchronous, call org.bukkit.event.Event.isAsynchronous()
    
    The exception will be a org.python.core.PyException, which will include Java exceptions thrown by calls to Java code from scripts. Use org.python.core.PyException.getCause to determine if there was an underlying Java exception.
    """

    def __init__(self, script: "Script", exception: "PyException", async: bool):
        """
        Arguments
        - script: The script that caused the error/exception
        - exception: The org.python.core.PyException that was thrown
        - async: Whether the exception occurred in an asychronous context
        """
        ...


    def getException(self) -> "PyException":
        """
        Get the org.python.core.PyException that was thrown.

        Returns
        - The org.python.core.PyException that was thrown
        """
        ...


    def doReportException(self) -> bool:
        """
        Get if the exception should be reported to console and/or a script's log file.

        Returns
        - True if the exception should be reported to console and/or a script's log file, False if otherwise
        """
        ...


    def setReportException(self, reportException: bool) -> None:
        """
        Set if the exception should be reported to console and/or the script's log file.

        Arguments
        - reportException: Whether the exception should be reported.
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
