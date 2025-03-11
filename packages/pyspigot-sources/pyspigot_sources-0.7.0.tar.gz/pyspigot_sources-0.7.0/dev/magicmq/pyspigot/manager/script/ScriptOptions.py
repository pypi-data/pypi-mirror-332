"""
Python module generated from Java source file dev.magicmq.pyspigot.manager.script.ScriptOptions

Java source file obtained from artifact pyspigot version 0.7.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.config import PluginConfig
from dev.magicmq.pyspigot.config import ScriptOptionsConfig
from dev.magicmq.pyspigot.manager.script import *
from org.bukkit.configuration import InvalidConfigurationException
from org.bukkit.permissions import Permission
from org.bukkit.permissions import PermissionDefault
from typing import Any, Callable, Iterable, Tuple


class ScriptOptions:
    """
    A class representing various runtime options belonging to a certain script.
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


    def isEnabled(self) -> bool:
        """
        Get if this script is enabled.

        Returns
        - True if the script is enabled, False if otherwise
        """
        ...


    def getLoadPriority(self) -> int:
        """
        Get the load priority for this script. Scripts with greater load priority will load before scripts with lower load priority.

        Returns
        - The script's load priority
        """
        ...


    def getPluginDependencies(self) -> list[str]:
        """
        Get a list of plugin dependencies for this script.

        Returns
        - A list of plugin dependencies for this script. Will return an empty list if this script has no plugin dependencies
        """
        ...


    def isFileLoggingEnabled(self) -> bool:
        """
        Get if file logging is enabled for this script.

        Returns
        - True if file logging is enabled, False if otherwise
        """
        ...


    def getMinLoggingLevel(self) -> "Level":
        """
        Get the minimum logging level for this script, represented as a java.util.logging.Level

        Returns
        - The minimum logging level at which messages should be logged
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
        """
        Prints a representation of this ScriptOptions in string format, including all options as defined in script_options.yml

        Returns
        - A string representation of the ScriptOptions
        """
        ...
