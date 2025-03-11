"""
Python module generated from Java source file dev.magicmq.pyspigot.config.PluginConfig

Java source file obtained from artifact pyspigot version 0.7.1

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot import PySpigot
from dev.magicmq.pyspigot.config import *
from java.time.format import DateTimeFormatter
from org.bukkit import ChatColor
from org.bukkit.configuration.file import FileConfiguration
from typing import Any, Callable, Iterable, Tuple


class PluginConfig:
    """
    Helper class to retrieve configuration values from the plugin config.
    """

    @staticmethod
    def reload() -> None:
        ...


    @staticmethod
    def getMetricsEnabled() -> bool:
        ...


    @staticmethod
    def getScriptLoadDelay() -> int:
        ...


    @staticmethod
    def getLibraryRelocations() -> dict[str, str]:
        ...


    @staticmethod
    def getLogTimestamp() -> "DateTimeFormatter":
        ...


    @staticmethod
    def doScriptActionLogging() -> bool:
        ...


    @staticmethod
    def doVerboseRedisLogging() -> bool:
        ...


    @staticmethod
    def doScriptUnloadOnPluginDisable() -> bool:
        ...


    @staticmethod
    def scriptOptionEnabled() -> bool:
        ...


    @staticmethod
    def scriptOptionLoadPriority() -> int:
        ...


    @staticmethod
    def scriptOptionPluginDepend() -> list[str]:
        ...


    @staticmethod
    def scriptOptionFileLoggingEnabled() -> bool:
        ...


    @staticmethod
    def scriptOptionMinLoggingLevel() -> str:
        ...


    @staticmethod
    def scriptOptionPermissionDefault() -> str:
        ...


    @staticmethod
    def scriptOptionPermissions() -> dict[Any, Any]:
        ...


    @staticmethod
    def shouldPrintStackTraces() -> bool:
        ...


    @staticmethod
    def shouldShowUpdateMessages() -> bool:
        ...


    @staticmethod
    def shouldUpdatePySpigotLib() -> bool:
        ...


    @staticmethod
    def getMessage(key: str, withPrefix: bool) -> str:
        ...


    @staticmethod
    def getPrefix() -> str:
        ...
