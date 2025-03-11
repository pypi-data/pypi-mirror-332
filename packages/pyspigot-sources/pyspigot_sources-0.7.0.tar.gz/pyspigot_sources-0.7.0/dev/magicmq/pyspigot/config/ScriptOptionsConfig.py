"""
Python module generated from Java source file dev.magicmq.pyspigot.config.ScriptOptionsConfig

Java source file obtained from artifact pyspigot version 0.7.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot import PySpigot
from dev.magicmq.pyspigot.config import *
from java.io import File
from java.io import FileInputStream
from java.io import IOException
from java.io import InputStream
from org.bukkit.configuration import InvalidConfigurationException
from org.yaml.snakeyaml import DumperOptions
from org.yaml.snakeyaml import LoaderOptions
from org.yaml.snakeyaml import Yaml
from org.yaml.snakeyaml.constructor import SafeConstructor
from org.yaml.snakeyaml.nodes import Tag
from org.yaml.snakeyaml.representer import Representer
from org.yaml.snakeyaml.resolver import Resolver
from typing import Any, Callable, Iterable, Tuple


class ScriptOptionsConfig:
    """
    Helper class to retrieve configuration values from the script options config.
    """

    @staticmethod
    def reload() -> None:
        ...


    @staticmethod
    def contains(key: str) -> bool:
        ...


    @staticmethod
    def getScriptSection(scriptName: str) -> dict[Any, Any]:
        ...


    @staticmethod
    def getEnabled(scriptName: str, defaultValue: bool) -> bool:
        ...


    @staticmethod
    def getLoadPriority(scriptName: str, defaultValue: int) -> int:
        ...


    @staticmethod
    def getPluginDepend(scriptName: str, defaultValue: list[str]) -> list[str]:
        ...


    @staticmethod
    def getFileLoggingEnabled(scriptName: str, defaultValue: bool) -> bool:
        ...


    @staticmethod
    def getMinLoggingLevel(scriptName: str, defaultValue: str) -> str:
        ...


    @staticmethod
    def getPermissionDefault(scriptName: str, defaultValue: str) -> str:
        ...


    @staticmethod
    def getPermissions(scriptName: str, defaultValue: dict[Any, Any]) -> dict[Any, Any]:
        ...
