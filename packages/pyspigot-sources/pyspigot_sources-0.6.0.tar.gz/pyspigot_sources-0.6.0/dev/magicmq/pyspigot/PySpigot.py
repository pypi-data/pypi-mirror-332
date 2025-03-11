"""
Python module generated from Java source file dev.magicmq.pyspigot.PySpigot

Java source file obtained from artifact pyspigot version 0.6.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot import *
from dev.magicmq.pyspigot.command import PySpigotCommand
from dev.magicmq.pyspigot.config import PluginConfig
from dev.magicmq.pyspigot.manager.command import CommandManager
from dev.magicmq.pyspigot.manager.config import ConfigManager
from dev.magicmq.pyspigot.manager.libraries import LibraryManager
from dev.magicmq.pyspigot.manager.listener import ListenerManager
from dev.magicmq.pyspigot.manager.placeholder import PlaceholderManager
from dev.magicmq.pyspigot.manager.protocol import ProtocolManager
from dev.magicmq.pyspigot.manager.script import GlobalVariables
from dev.magicmq.pyspigot.manager.script import ScriptManager
from dev.magicmq.pyspigot.manager.task import TaskManager
from dev.magicmq.pyspigot.util import StringUtils
from java.io import *
from java.net import URL
from java.net import URLConnection
from java.util import Scanner
from org.bstats.bukkit import Metrics
from org.bstats.charts import SimplePie
from org.bukkit import Bukkit
from org.bukkit.command import PluginCommand
from org.bukkit.command import SimpleCommandMap
from org.bukkit.configuration.file import FileConfiguration
from org.bukkit.configuration.file import YamlConfiguration
from org.bukkit.help import IndexHelpTopic
from org.bukkit.plugin import Plugin
from org.bukkit.plugin.java import JavaPlugin
from org.bukkit.scheduler import BukkitTask
from typing import Any, Callable, Iterable, Tuple


class PySpigot(JavaPlugin):
    """
    Main class of the plugin.
    """

    script = None
    """
    Can be used by scripts to access the ScriptManager.
    """
    global_vars = None
    """
    Can be used by scripts to access the GlobalVariables
    """
    listener = None
    """
    Can be used by scripts to access the ListenerManager.
    """
    command = None
    """
    Can be used by scripts to access the CommandManager.
    """
    scheduler = None
    """
    Can be used by scripts to access the TaskManager.
    """
    config = None
    """
    Can be used by scripts to access the ConfigManager.
    """
    protocol = None
    """
    Can be used by scripts to access the ProtocolManager.
    """
    placeholder = None
    """
    Can be used by scripts to access the PlaceholderManager.
    """


    def onEnable(self) -> None:
        ...


    def onDisable(self) -> None:
        ...


    def reload(self) -> None:
        """
        Reload the plugin configuration.
        """
        ...


    def getPluginClassLoader(self) -> "ClassLoader":
        """
        Get the ClassLoader for PySpigot.

        Returns
        - The ClassLoader
        """
        ...


    def getScriptOptionsConfig(self) -> "FileConfiguration":
        """
        Get the script_options.yml configuration file.

        Returns
        - The script_options.yml configuration file
        """
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
