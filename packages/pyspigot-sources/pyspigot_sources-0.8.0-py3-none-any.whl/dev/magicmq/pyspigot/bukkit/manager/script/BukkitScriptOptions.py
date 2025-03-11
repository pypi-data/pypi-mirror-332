"""
Python module generated from Java source file dev.magicmq.pyspigot.bukkit.manager.script.BukkitScriptOptions

Java source file obtained from artifact pyspigot-bukkit version 0.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot import PyCore
from dev.magicmq.pyspigot.bukkit.manager.script import *
from dev.magicmq.pyspigot.config import ScriptOptionsConfig
from dev.magicmq.pyspigot.exception import InvalidConfigurationException
from dev.magicmq.pyspigot.manager.script import ScriptOptions
from org.bukkit.permissions import Permission
from org.bukkit.permissions import PermissionDefault
from typing import Any, Callable, Iterable, Tuple


class BukkitScriptOptions(ScriptOptions):
    """
    An extension of the base ScriptOptions class that includes Bukkit-specific code for parsing and registering script permissions.
    """

    def __init__(self):
        """
        Initialize a new ScriptOptions with the default values.
        """
        ...


    def __init__(self, scriptName: str):
        """
        Initialize a new ScriptOptions using the appropriate values in the script_options.yml file, using the script name to search for the values.

        Arguments
        - scriptName: The name of the script whose script options should be initialized
        """
        ...


    def getPermissionDefault(self) -> "PermissionDefault":
        """
        Get the default permissions for permissions defined for this script.

        Returns
        - The default permission level
        """
        ...


    def getPermissions(self) -> list["Permission"]:
        """
        Get a list of permissions defined for this script.

        Returns
        - A list of permissions. Will return an empty list if this script has no permissions defined
        """
        ...


    def toString(self) -> str:
        ...
