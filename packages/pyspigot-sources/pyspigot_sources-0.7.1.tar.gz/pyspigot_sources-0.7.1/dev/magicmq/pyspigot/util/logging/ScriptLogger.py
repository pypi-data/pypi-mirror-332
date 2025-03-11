"""
Python module generated from Java source file dev.magicmq.pyspigot.util.logging.ScriptLogger

Java source file obtained from artifact pyspigot version 0.7.1

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot import PySpigot
from dev.magicmq.pyspigot.config import PluginConfig
from dev.magicmq.pyspigot.manager.script import Script
from dev.magicmq.pyspigot.util.logging import *
from java.io import File
from java.io import IOException
from java.io import PrintWriter
from java.io import StringWriter
from java.time import ZoneId
from java.time import ZonedDateTime
from typing import Any, Callable, Iterable, Tuple


class ScriptLogger(Logger):
    """
    A subclass of Logger that represents a script's logger.

    See
    - Logger
    """

    def __init__(self, script: "Script"):
        """
        Arguments
        - script: The script associated with this logger
        """
        ...


    def initFileHandler(self) -> None:
        """
        Initializes the FileHandler to log script log messages to its respective log file.

        Raises
        - IOException: If there was an IOException when initializing the FileHandler for this logger
        """
        ...


    def closeFileHandler(self) -> None:
        """
        Closes the FileHandler for this logger. Should only be called if script file logging is enabled.
        """
        ...


    def print(self, logText: str) -> None:
        """
        A convenience method added for a script to print debug information to console and its log file.

        Arguments
        - logText: The message to print
        """
        ...


    def debug(self, logText: str) -> None:
        """
        A convenience method added for a script to print debug information to console and its log file.

        Arguments
        - logText: The message to print
        """
        ...


    def log(self, logRecord: "LogRecord") -> None:
        """

        """
        ...
