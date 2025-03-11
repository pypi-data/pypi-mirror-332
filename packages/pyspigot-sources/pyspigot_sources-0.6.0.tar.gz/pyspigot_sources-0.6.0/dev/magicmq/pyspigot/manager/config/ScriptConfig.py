"""
Python module generated from Java source file dev.magicmq.pyspigot.manager.config.ScriptConfig

Java source file obtained from artifact pyspigot version 0.6.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.manager.config import *
from java.io import File
from java.io import IOException
from org.bukkit.configuration import InvalidConfigurationException
from org.bukkit.configuration.file import YamlConfiguration
from typing import Any, Callable, Iterable, Tuple


class ScriptConfig(YamlConfiguration):
    """
    A class representing a script configuration file.

    See
    - org.bukkit.configuration.file.YamlConfiguration
    """

    def getConfigFile(self) -> "File":
        """
        Get the file associated with this configuration.

        Returns
        - The file associated with this configuration
        """
        ...


    def save(self) -> None:
        """
        Save the config to its associated file.

        Raises
        - IOException: If there is an IOException when saving the file
        """
        ...
