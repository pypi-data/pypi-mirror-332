"""
Python module generated from Java source file dev.magicmq.pyspigot.manager.task.Task

Java source file obtained from artifact pyspigot version 0.7.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.manager.script import Script
from dev.magicmq.pyspigot.manager.script import ScriptManager
from dev.magicmq.pyspigot.manager.task import *
from java.util import Arrays
from org.bukkit.scheduler import BukkitRunnable
from org.python.core import *
from typing import Any, Callable, Iterable, Tuple


class Task(BukkitRunnable):
    """
    Represents a task defined by a script.
    """

    def __init__(self, script: "Script", function: Callable, functionArgs: list["Object"], async: bool, delay: int):
        """
        Arguments
        - script: The script associated with this task
        - function: The script function that should be called when the task executes
        - functionArgs: Any arguments that should be passed to the function
        - async: True if the task is asynchronous, False if otherwise
        - delay: The delay, in ticks, to wait until running the task
        """
        ...


    def run(self) -> None:
        """
        Called internally when the task executes.
        """
        ...


    def getScript(self) -> "Script":
        """
        Get the script associated with this task.

        Returns
        - The script associated with this task
        """
        ...


    def toString(self) -> str:
        """
        Prints a representation of this Task in string format, including the task ID, if it is async, and delay (if applicable)

        Returns
        - A string representation of the Task
        """
        ...
