"""
Python module generated from Java source file dev.magicmq.pyspigot.bukkit.PySpigot

Java source file obtained from artifact pyspigot-bukkit version 0.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot import PlatformAdapter
from dev.magicmq.pyspigot import PyCore
from dev.magicmq.pyspigot.bukkit import *
from dev.magicmq.pyspigot.bukkit.command import BukkitPluginCommand
from dev.magicmq.pyspigot.bukkit.config import BukkitPluginConfig
from dev.magicmq.pyspigot.bukkit.manager.command import BukkitCommandManager
from dev.magicmq.pyspigot.bukkit.manager.config import BukkitConfigManager
from dev.magicmq.pyspigot.bukkit.manager.listener import BukkitListenerManager
from dev.magicmq.pyspigot.bukkit.manager.placeholder import PlaceholderManager
from dev.magicmq.pyspigot.bukkit.manager.protocol import ProtocolManager
from dev.magicmq.pyspigot.bukkit.manager.script import BukkitScriptManager
from dev.magicmq.pyspigot.bukkit.manager.task import BukkitTaskManager
from dev.magicmq.pyspigot.config import PluginConfig
from dev.magicmq.pyspigot.manager.script import ScriptManager
from java.nio.file import Path
from java.nio.file import Paths
from org.bstats.bukkit import Metrics
from org.bstats.charts import SimplePie
from org.bukkit import Bukkit
from org.bukkit.command import PluginCommand
from org.bukkit.command import SimpleCommandMap
from org.bukkit.help import IndexHelpTopic
from org.bukkit.plugin import Plugin
from org.bukkit.plugin.java import JavaPlugin
from org.bukkit.scheduler import BukkitTask
from typing import Any, Callable, Iterable, Tuple


class PySpigot(JavaPlugin, PlatformAdapter):
    """
    Entry point of PySpigot for Bukkit servers.
    """

    def onEnable(self) -> None:
        ...


    def onDisable(self) -> None:
        ...


    def initConfig(self) -> "PluginConfig":
        ...


    def initCommands(self) -> None:
        ...


    def initListeners(self) -> None:
        ...


    def initPlatformManagers(self) -> None:
        ...


    def initVersionChecking(self) -> None:
        ...


    def setupMetrics(self) -> None:
        ...


    def shutdownMetrics(self) -> None:
        ...


    def shutdownVersionChecking(self) -> None:
        ...


    def getDataFolderPath(self) -> "Path":
        ...


    def getPluginClassLoader(self) -> "ClassLoader":
        ...


    def getVersion(self) -> str:
        ...


    def getPluginIdentifier(self) -> str:
        ...


    def isProtocolLibAvailable(self) -> bool:
        """
        Check if ProtocolLib is available on the server.

        Returns
        - True if ProtocolLib is loaded and enabled, False if otherwise
        """
        ...


    def isPlaceholderApiAvailable(self) -> bool:
        """
        Check if PlacehodlerAPI is available on the server.

        Returns
        - True if PlaceholderAPI is loaded and enabled, False if otherwise
        """
        ...


    @staticmethod
    def get() -> "PySpigot":
        """
        Get the instance of this plugin.

        Returns
        - The instance
        """
        ...
