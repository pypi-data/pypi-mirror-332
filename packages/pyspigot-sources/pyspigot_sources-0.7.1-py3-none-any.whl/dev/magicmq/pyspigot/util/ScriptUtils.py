"""
Python module generated from Java source file dev.magicmq.pyspigot.util.ScriptUtils

Java source file obtained from artifact pyspigot version 0.7.1

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.manager.libraries import LibraryManager
from dev.magicmq.pyspigot.manager.script import Script
from dev.magicmq.pyspigot.manager.script import ScriptManager
from dev.magicmq.pyspigot.util import *
from java.util import Optional
from org.python.core import PyString
from org.python.core import PySystemState
from typing import Any, Callable, Iterable, Tuple


class ScriptUtils:
    """
    A collection of utility methods related to scripts.
    """

    @staticmethod
    def getScriptFromCallStack() -> "Script":
        """
        Attempts to get the script involved in a Java method call by analyzing the call stack.

        Returns
        - The script associated with the method call, or null if no script was found in the call stack
        """
        ...


    @staticmethod
    def initPySystemState() -> "PySystemState":
        """
        Initializes a new PySystemState for a new org.python.util.PythonInterpreter when a script is loaded.
        
        This method will also do the following with the new PySystemState: set its class loader to the class loader provided by the LibraryManager, and add "./plugins/PySpigot/python-libs/" and "./plugins/PySpigot/scripts/" to the path.

        Returns
        - The PySystemState that was created
        """
        ...
