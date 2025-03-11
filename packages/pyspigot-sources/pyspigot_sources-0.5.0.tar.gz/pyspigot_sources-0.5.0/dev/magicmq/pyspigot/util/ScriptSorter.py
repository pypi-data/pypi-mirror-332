"""
Python module generated from Java source file dev.magicmq.pyspigot.util.ScriptSorter

Java source file obtained from artifact pyspigot version 0.5.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.manager.script import Script
from dev.magicmq.pyspigot.util import *
from java.util import *
from typing import Any, Callable, Iterable, Tuple


class ScriptSorter:
    """
    Utility class that places scripts into the proper loading order, taking into account dependencies. This class uses script dependencies as defined in dev.magicmq.pyspigot.manager.script.ScriptOptions.
    
    Under the hood, utilizes depth-first search algorithm to order scripts.
    """

    def __init__(self, scripts: list["Script"]):
        """
        Arguments
        - scripts: An unordered list of scripts
        """
        ...


    def getOptimalLoadOrder(self) -> list["Script"]:
        """
        Get a LinkedList, in the order that the scripts should be loaded. Ordering is done with respect to script dependencies. The first script in this list should load first, and the last script in this list should load last.

        Returns
        - An ordered list of scripts
        """
        ...
