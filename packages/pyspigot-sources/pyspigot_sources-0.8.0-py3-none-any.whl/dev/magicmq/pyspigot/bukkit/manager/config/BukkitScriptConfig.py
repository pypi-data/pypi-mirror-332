"""
Python module generated from Java source file dev.magicmq.pyspigot.bukkit.manager.config.BukkitScriptConfig

Java source file obtained from artifact pyspigot-bukkit version 0.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.bukkit.manager.config import *
from dev.magicmq.pyspigot.manager.config import ScriptConfig
from java.io import File
from java.io import IOException
from java.nio.file import Path
from java.nio.file import Paths
from org.bukkit.configuration import InvalidConfigurationException
from org.bukkit.configuration.file import YamlConfiguration
from typing import Any, Callable, Iterable, Tuple


class BukkitScriptConfig(YamlConfiguration, ScriptConfig):
    """
    A class representing a script configuration file, for the Bukkit implementation.

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
        ...


    def getConfigPath(self) -> "Path":
        ...


    def load(self) -> None:
        ...


    def reload(self) -> None:
        ...


    def save(self) -> None:
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
