"""
Python module generated from Java source file dev.magicmq.pyspigot.manager.task.RepeatingTask

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
from org.python.core import PyObject
from typing import Any, Callable, Iterable, Tuple


class RepeatingTask(Task):
    """
    Represents a repeating task defined by a script.
    """

    def __init__(self, script: "Script", function: Callable, functionArgs: list["Object"], async: bool, delay: int, interval: int):
        """
        Arguments
        - script: The script associated with this repeating task
        - function: The script function that should be called every time the repeating task executes
        - functionArgs: Any arguments that should be passed to the function
        - async: True if the task is asynchronous, False if otherwise
        - delay: The delay, in ticks, to wait until running the task
        - interval: The interval, in ticks, between each repeat of the task
        """
        ...


    def run(self) -> None:
        """

        """
        ...


    def toString(self) -> str:
        """
        Prints a representation of this RepeatingTask in string format, including the task ID, if it is async, delay (if applicable), and interval (if applicable)

        Returns
        - A string representation of the RepeatingTask
        """
        ...
