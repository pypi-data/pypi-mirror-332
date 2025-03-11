"""
Python module generated from Java source file dev.magicmq.pyspigot.manager.task.RepeatingTask

Java source file obtained from artifact pyspigot version 0.5.0

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

    def __init__(self, script: "Script", function: Callable, functionArgs: list["Object"]):
        """
        Arguments
        - script: The script associated with this repeating task
        - function: The script function that should be called every time the repeating task executes
        - functionArgs: Any arguments that should be passed to the function
        """
        ...


    def run(self) -> None:
        """

        """
        ...
