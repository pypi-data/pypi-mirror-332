"""
Python module generated from Java source file dev.magicmq.pyspigot.manager.config.ConfigManager

Java source file obtained from artifact pyspigot version 0.6.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot import PySpigot
from dev.magicmq.pyspigot.manager.config import *
from java.io import File
from java.io import IOException
from org.bukkit.configuration import InvalidConfigurationException
from typing import Any, Callable, Iterable, Tuple


class ConfigManager:
    """
    Manager for scripts to interface with configuration files. Primarily used by scripts to load, write to, and save .yml files.
    """

    def loadConfig(self, fileName: str) -> "ScriptConfig":
        """
        Load a config file with the given name.
        
        **Note:** This should be called from scripts only!

        Arguments
        - fileName: The name of the config file to load

        Returns
        - A ScriptConfig representing the config file that was loaded

        Raises
        - IOException: If there was an IOException when loading the config
        - org.bukkit.configuration.InvalidConfigurationException: If there was an InvalidConfigurationException when loading the config
        """
        ...


    def reloadConfig(self, config: "ScriptConfig") -> "ScriptConfig":
        """
        Reload an already loaded ScriptConfig.
        
        **Note:** This should be called from scripts only!

        Arguments
        - config: The ScriptConfig to reload

        Returns
        - A new ScriptConfig representing the reloaded config file

        Raises
        - IOException: If there was an IOException when reloading the config
        - org.bukkit.configuration.InvalidConfigurationException: If there was an InvalidConfigurationException when reloading the config
        """
        ...


    def getConfigFolder(self) -> "File":
        """
        Get the folder where script config files are stored.

        Returns
        - The folder where script config files are stored
        """
        ...


    @staticmethod
    def get() -> "ConfigManager":
        """
        Get the singleton instance of this ConfigManager

        Returns
        - The instance
        """
        ...
