"""
Python module generated from Java source file dev.magicmq.pyspigot.manager.task.SyncCallbackTask

Java source file obtained from artifact pyspigot-core version 0.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.manager.script import Script
from dev.magicmq.pyspigot.manager.script import ScriptManager
from dev.magicmq.pyspigot.manager.task import *
from org.python.core import Py
from org.python.core import PyException
from org.python.core import PyFunction
from org.python.core import PyNone
from org.python.core import PyObject
from typing import Any, Callable, Iterable, Tuple


class SyncCallbackTask(Task):
    """
    Represents an async task with a synchronous callback defined by a script.
    """

    def __init__(self, script: "Script", function: Callable, callbackFunction: Callable, functionArgs: list["Object"], delay: int):
        """
        Arguments
        - script: The script associated with this task
        - function: The script function that should be called when the async task executes
        - callbackFunction: The script function that should be called for the synchronous callback
        - functionArgs: Any arguments that should be passed to the function
        """
        ...


    def run(self) -> None:
        """
        Called internally when the task executes.
        """
        ...


    def toString(self) -> str:
        """
        Prints a representation of this SyncCallbackTask in string format, including the task ID, if it is async, and delay (if applicable)

        Returns
        - A string representation of the SyncCallbackTask
        """
        ...
