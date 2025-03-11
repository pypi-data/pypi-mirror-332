"""
Python module generated from Java source file dev.magicmq.pyspigot.command.SubCommandMeta

Java source file obtained from artifact pyspigot version 0.7.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.command import *
from typing import Any, Callable, Iterable, Tuple


class SubCommandMeta:

    def command(self) -> str:
        ...


    def aliases(self) -> list[str]:
        return {}


    def permission(self) -> str:
        return ""


    def playerOnly(self) -> bool:
        return False


    def usage(self) -> str:
        return ""


    def description(self) -> str:
        return "No description provided."
