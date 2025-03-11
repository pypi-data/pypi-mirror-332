"""
Python module generated from Java source file dev.magicmq.pyspigot.util.logging.PrintStreamWrapper

Java source file obtained from artifact pyspigot version 0.7.1

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.manager.script import Script
from dev.magicmq.pyspigot.util.logging import *
from java.io import OutputStream
from java.io import PrintStream
from java.nio.charset import StandardCharsets
from java.util import Arrays
from typing import Any, Callable, Iterable, Tuple


class PrintStreamWrapper(PrintStream):
    """
    A wrapper class that captures print statements and errors/exceptions from scripts and redirects them to the script's logger.
    """

    def __init__(self, out: "OutputStream", script: "Script", level: "Level", prefix: str):
        """
        Arguments
        - out: The parent OutputStream, usually System.out or System.err
        - script: The script to which this PrintStreamWrapper belongs
        - level: The logging level, usually Level.INFO for stdout and Level.SEVERE for stderr
        - prefix: The prefix to include before the log message, usually [STDOUT] for stdout and [STDERR] for stderr
        """
        ...


    def write(self, buf: list[int], off: int, len: int) -> None:
        """
        Captures writes to the PrintStream, converts the bytes into readable text (truncating according to the specified length and offset), and logs the text to the script's logger. This method also strips carriage returns/new line characters from the end of the text, because the script logger already inserts a new line when logging.

        Arguments
        - buf: A byte array
        - off: Offset from which to start taking bytes
        - len: Number of bytes to write
        """
        ...


    def write(self, buf: list[int]) -> None:
        """

        """
        ...
