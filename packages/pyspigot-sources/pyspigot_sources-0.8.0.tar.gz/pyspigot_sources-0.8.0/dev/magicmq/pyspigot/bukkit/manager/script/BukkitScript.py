"""
Python module generated from Java source file dev.magicmq.pyspigot.bukkit.manager.script.BukkitScript

Java source file obtained from artifact pyspigot-bukkit version 0.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.bukkit.manager.script import *
from dev.magicmq.pyspigot.manager.script import Script
from dev.magicmq.pyspigot.manager.script import ScriptOptions
from java.nio.file import Path
from org.bukkit import Bukkit
from org.bukkit.permissions import Permission
from typing import Any, Callable, Iterable, Tuple


class BukkitScript(Script):
    """
    An extension of the base Script class that includes Bukkit-specific code for initializing script permissions.
    """

    def __init__(self, path: "Path", name: str, options: "BukkitScriptOptions"):
        """
        Arguments
        - path: The path that corresponds to the file where the script lives
        - name: The name of this script. Should contain its extension (.py)
        - options: The ScriptOptions for this script
        """
        ...


    def initPermissions(self) -> None:
        """
        Adds the script's permission (from its options) to the server.
        """
        ...


    def removePermissions(self) -> None:
        """
        Removes the script's permissions from the server.
        """
        ...
