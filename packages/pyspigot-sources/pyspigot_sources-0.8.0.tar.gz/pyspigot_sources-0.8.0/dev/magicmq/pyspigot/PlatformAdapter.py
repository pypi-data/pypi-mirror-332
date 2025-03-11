"""
Python module generated from Java source file dev.magicmq.pyspigot.PlatformAdapter

Java source file obtained from artifact pyspigot-core version 0.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot import *
from dev.magicmq.pyspigot.config import PluginConfig
from java.io import File
from java.nio.file import Path
from typing import Any, Callable, Iterable, Tuple


class PlatformAdapter:
    """
    An adapter class that wraps platform-specific code for plugin initialization, shutdown, and other plugin-related activities.
    """

    def initConfig(self) -> "PluginConfig":
        """
        Initialize the config file via a platform-specific implementation, saving the default config file in the process if it does not already exist.
        """
        ...


    def initCommands(self) -> None:
        """
        Initialize plugin commands via a platform-specific implementation.
        """
        ...


    def initListeners(self) -> None:
        """
        Initialize plugin listeners via a platform-specific implementation.
        """
        ...


    def initPlatformManagers(self) -> None:
        """
        Initialize managers that require a platform-specific implementation.
        
        Also initializes managers that are entirely specific to one platform (no core abstraction).
        """
        ...


    def initVersionChecking(self) -> None:
        """
        Initialize the version-checking task via a platform-specific implementation.
        """
        ...


    def setupMetrics(self) -> None:
        """
        Setup bStats metrics via a platform-specific implementation.
        """
        ...


    def shutdownMetrics(self) -> None:
        """
        Shutdown bStats metrics via a platform-specific implementation.
        """
        ...


    def shutdownVersionChecking(self) -> None:
        """
        Stop the version-checking task via a platform-specific implementation.
        """
        ...


    def getLogger(self) -> "Logger":
        """
        Get the logger for the plugin via a platform-specific implementation.

        Returns
        - The logger
        """
        ...


    def getDataFolder(self) -> "File":
        """
        Get the data folder for the plugin via a platform-specific implementation.

        Returns
        - The data folder
        """
        ...


    def getDataFolderPath(self) -> "Path":
        """
        Get the data folder path for the plugin via a platform-specific implementation.

        Returns
        - The data folder path
        """
        ...


    def getPluginClassLoader(self) -> "ClassLoader":
        """
        Get the class loader for the plugin via a platform-specific implementation.

        Returns
        - The class loader
        """
        ...


    def getVersion(self) -> str:
        """
        Get the plugin version via a platform-specific implementation.

        Returns
        - The plugin version
        """
        ...


    def getPluginIdentifier(self) -> str:
        """
        Get the appropriate plugin identifier, depending on the platform.

        Returns
        - The plugin identifier
        """
        ...
