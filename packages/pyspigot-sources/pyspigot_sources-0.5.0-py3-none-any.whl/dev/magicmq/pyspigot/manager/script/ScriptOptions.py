"""
Python module generated from Java source file dev.magicmq.pyspigot.manager.script.ScriptOptions

Java source file obtained from artifact pyspigot version 0.5.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.config import PluginConfig
from dev.magicmq.pyspigot.manager.script import *
from org.bukkit.configuration import ConfigurationSection
from typing import Any, Callable, Iterable, Tuple


class ScriptOptions:
    """
    A class representing various runtime options belonging to a certain script.
    """

    def __init__(self, config: "ConfigurationSection"):
        """
        Initialize a new ScriptOptions using values from the provided ConfigurationSection. If this constructor is passed a null value for the config parameter, then the default script options will be used.

        Arguments
        - config: The configuration section from which script options should be read, or null if the default script options should be used
        """
        ...


    def isEnabled(self) -> bool:
        """
        Get if this script is enabled.

        Returns
        - True if the script is enabled, False if otherwise
        """
        ...


    def getDependencies(self) -> list[str]:
        """
        Get a list of dependencies for this script.

        Returns
        - A list of dependencies for this script. Will return an empty list if this script has no dependencies
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
