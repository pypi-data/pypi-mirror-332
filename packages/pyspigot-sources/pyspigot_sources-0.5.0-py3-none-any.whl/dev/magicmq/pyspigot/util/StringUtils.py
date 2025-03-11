"""
Python module generated from Java source file dev.magicmq.pyspigot.util.StringUtils

Java source file obtained from artifact pyspigot version 0.5.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.util import *
from typing import Any, Callable, Iterable, Tuple


class StringUtils:
    """
    A utility class for various methods/classes related to Strings.
    """

    @staticmethod
    def replaceLastOccurrence(string: str, toReplace: str, replaceWith: str) -> str:
        ...


    class Version(Comparable):

        def __init__(self, version: str):
            ...


        def getVersion(self) -> str:
            ...


        def compareTo(self, that: "StringUtils.Version") -> int:
            ...
