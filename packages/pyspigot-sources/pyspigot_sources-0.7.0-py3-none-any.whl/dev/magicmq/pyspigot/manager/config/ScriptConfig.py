"""
Python module generated from Java source file dev.magicmq.pyspigot.manager.config.ScriptConfig

Java source file obtained from artifact pyspigot version 0.7.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.manager.config import *
from java.io import File
from java.io import IOException
from java.nio.file import Path
from java.nio.file import Paths
from org.bukkit.configuration import InvalidConfigurationException
from org.bukkit.configuration.file import YamlConfiguration
from typing import Any, Callable, Iterable, Tuple


class ScriptConfig(YamlConfiguration):
    """
    A class representing a script configuration file.

    See
    - org.bukkit.configuration.file.YamlConfiguration
    """

    def __init__(self, configFile: "File", defaults: str):
        """
        Arguments
        - configFile: The configuration file
        - defaults: A YAML-formatted string containing the desired default values for the configuration
        """
        ...


    def getConfigFile(self) -> "File":
        """
        Get the file associated with this configuration.

        Returns
        - The file associated with this configuration
        """
        ...


    def getConfigPath(self) -> "Path":
        """
        Get the absolute path of the file associated with this configuration.

        Returns
        - The path of the file
        """
        ...


    def setIfNotExists(self, path: str, value: "Object") -> bool:
        """
        Sets the specified path to the given value only if the path is not already set in the config file. Any specified default values are ignored when checking if the path is set.

        Arguments
        - path: Path of the object to set
        - value: Value to set the path to

        Returns
        - True if the path was set to the value (in other words the path was not previously set), False if the path was not set to the value (in other words the path was already previously set)

        See
        - org.bukkit.configuration.ConfigurationSection.set(String, Object)
        """
        ...


    def load(self) -> None:
        """
        Loads the config from the configuration file. Will also set defaults for the configuration, if they were specified.

        Raises
        - IOException: If there was an exception when loading the file
        - org.bukkit.configuration.InvalidConfigurationException: If there was an error when parsing the loaded file (invalid configuration)
        """
        ...


    def reload(self) -> None:
        """
        Reload the configuration. Will read all changes made to the configuration file since the configuration was last loaded/reloaded.

        Raises
        - IOException: If there was an exception when loading the file
        - org.bukkit.configuration.InvalidConfigurationException: If there was an error when parsing the loaded file (invalid configuration)
        """
        ...


    def save(self) -> None:
        """
        Save the configuration to its associated file. For continuity purposes, the configuration is also reloaded from the file after saving.

        Raises
        - IOException: If there is an IOException when saving the file
        - org.bukkit.configuration.InvalidConfigurationException: If there was an error when parsing the file when reloading (invalid configuration)
        """
        ...
