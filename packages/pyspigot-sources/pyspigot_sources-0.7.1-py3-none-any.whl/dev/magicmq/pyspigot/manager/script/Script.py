"""
Python module generated from Java source file dev.magicmq.pyspigot.manager.script.Script

Java source file obtained from artifact pyspigot version 0.7.1

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot import PySpigot
from dev.magicmq.pyspigot.manager.script import *
from dev.magicmq.pyspigot.util import ScriptUtils
from dev.magicmq.pyspigot.util.logging import PrintStreamWrapper
from dev.magicmq.pyspigot.util.logging import ScriptLogger
from java.io import File
from java.io import IOException
from java.nio.file import Path
from org.bukkit import Bukkit
from org.bukkit.permissions import Permission
from org.python.util import PythonInterpreter
from typing import Any, Callable, Iterable, Tuple


class Script(Comparable):
    """
    An object that represents a loaded script. Because this object is instantiated some time before the script is actually executed (in order to fetch its options and order scripts to load according to dependencies), there may be a brief time when this object represents a loaded *but not running * script. To check if this script object represents a running script, call ScriptManager.isScriptRunning(String).
    """

    def __init__(self, path: "Path", name: str, options: "ScriptOptions"):
        """
        Arguments
        - path: The path that corresponds to the file where the script lives
        - name: The name of this script. Should contain its extension (.py)
        - options: The ScriptOptions for this script
        """
        ...


    def prepare(self) -> None:
        """
        Prepares this script for execution by initializing its interpreter and logger. Called just prior to executing the script's code.
        """
        ...


    def close(self) -> None:
        """
        Closes this script's file logger and interpreter. Called when a script is unloaded/stopped.
        """
        ...


    def initPermissions(self) -> None:
        ...


    def removePermissions(self) -> None:
        ...


    def getFile(self) -> "File":
        """
        Get the File associated with this script.

        Returns
        - The File associated with this script
        """
        ...


    def getPath(self) -> "Path":
        """
        Get the path corresponding to the script file.

        Returns
        - The path
        """
        ...


    def getName(self) -> str:
        """
        Get the name associated with this script.

        Returns
        - The name associated with this script. Will contain its extension (.py)
        """
        ...


    def getSimpleName(self) -> str:
        """
        Get the simple name (without the file extension, .py) associated with this script.

        Returns
        - The simple name associated with this script. Will contain only the file name, without the extension (.py)
        """
        ...


    def getOptions(self) -> "ScriptOptions":
        """
        Get the ScriptOptions for this script, which contains various runtime options associated with this script.

        Returns
        - The ScriptOptions for this script
        """
        ...


    def getInterpreter(self) -> "PythonInterpreter":
        """
        Get the org.python.util.PythonInterpreter associated wtih this script.

        Returns
        - The org.python.util.PythonInterpreter associated with this script
        """
        ...


    def getLogger(self) -> "ScriptLogger":
        """
        Get this scripts logger.

        Returns
        - This script's logger

        See
        - ScriptLogger
        """
        ...


    def getLogFileName(self) -> str:
        """
        Get the log file name for this script.

        Returns
        - The log file name for this script. Will contain its extension (.log)
        """
        ...


    def getUptime(self) -> int:
        """
        Get the millisecond duration that this script has been loaded

        Returns
        - The duration that the script has been loaded
        """
        ...


    def compareTo(self, other: "Script") -> int:
        """
        Compares this script to another script, using load order as the primary comparison. If the load order of this script is higher than other, then this script will be considered "less" than other (I.E. sorted earlier in a set than the other script). If the load order of this script is lower than other, then this script will be considered "greater" than the other script (I.E. sorted later in a set than other).
        
        If the load priority of this script is equal to other, then a comparison is performed based on the name of the two scripts (alphabetical).

        Arguments
        - other: The other script to be compared

        Returns
        - 1 if this script is greater than other, -1 if this script is less than other, and 0 if the two scripts are equal
        """
        ...


    def equals(self, other: "Object") -> bool:
        """
        Check if this script is the same as another script. Will check the names of both scripts to see if they match.

        Arguments
        - other: The other script to check against this script

        Returns
        - True if the scripts are equal, False if otherwise
        """
        ...
