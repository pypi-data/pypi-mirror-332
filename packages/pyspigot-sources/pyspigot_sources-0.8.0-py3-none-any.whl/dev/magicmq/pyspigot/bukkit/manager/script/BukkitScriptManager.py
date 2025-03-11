"""
Python module generated from Java source file dev.magicmq.pyspigot.bukkit.manager.script.BukkitScriptManager

Java source file obtained from artifact pyspigot-bukkit version 0.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot import PyCore
from dev.magicmq.pyspigot.bukkit import PySpigot
from dev.magicmq.pyspigot.bukkit.event import ScriptExceptionEvent
from dev.magicmq.pyspigot.bukkit.event import ScriptLoadEvent
from dev.magicmq.pyspigot.bukkit.event import ScriptUnloadEvent
from dev.magicmq.pyspigot.bukkit.manager.placeholder import PlaceholderManager
from dev.magicmq.pyspigot.bukkit.manager.protocol import ProtocolManager
from dev.magicmq.pyspigot.bukkit.manager.script import *
from dev.magicmq.pyspigot.exception import InvalidConfigurationException
from dev.magicmq.pyspigot.manager.script import Script
from dev.magicmq.pyspigot.manager.script import ScriptManager
from dev.magicmq.pyspigot.manager.script import ScriptOptions
from java.nio.file import Path
from org.bukkit import Bukkit
from org.bukkit.scheduler import BukkitTask
from org.python.core import PyException
from typing import Any, Callable, Iterable, Tuple


class BukkitScriptManager(ScriptManager):
    """
    The Bukkit-specific implementation of the script manager.
    """

    def scheduleStartScriptTask(self) -> None:
        ...


    def cancelStartScriptTask(self) -> None:
        ...


    def isPluginDependencyMissing(self, dependency: str) -> bool:
        ...


    def callScriptExceptionEvent(self, script: "Script", exception: "PyException") -> bool:
        ...


    def callScriptLoadEvent(self, script: "Script") -> None:
        ...


    def callScriptUnloadEvent(self, script: "Script", error: bool) -> None:
        ...


    def newScriptOptions(self) -> "ScriptOptions":
        ...


    def newScriptOptions(self, scriptName: str) -> "ScriptOptions":
        ...


    def newScript(self, path: "Path", name: str, options: "ScriptOptions") -> "Script":
        ...


    def initScriptPermissions(self, script: "Script") -> None:
        ...


    def removeScriptPermissions(self, script: "Script") -> None:
        ...


    def unregisterFromPlatformManagers(self, script: "Script") -> None:
        ...


    @staticmethod
    def get() -> "BukkitScriptManager":
        """
        Get the singleton instance of this BukkitScriptManager.

        Returns
        - The instance
        """
        ...
