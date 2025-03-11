"""
Python module generated from Java source file dev.magicmq.pyspigot.command.PySpigotCommand

Java source file obtained from artifact pyspigot version 0.6.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot import PySpigot
from dev.magicmq.pyspigot.command import *
from dev.magicmq.pyspigot.command.subcommands import *
from dev.magicmq.pyspigot.config import PluginConfig
from dev.magicmq.pyspigot.util import StringUtils
from java.util import Arrays
from org.bukkit import ChatColor
from org.bukkit.command import Command
from org.bukkit.command import CommandSender
from org.bukkit.command import TabExecutor
from org.bukkit.entity import Player
from typing import Any, Callable, Iterable, Tuple


class PySpigotCommand(TabExecutor):

    def __init__(self):
        ...


    def onCommand(self, sender: "CommandSender", command: "Command", label: str, args: list[str]) -> bool:
        ...


    def onTabComplete(self, sender: "CommandSender", command: "Command", alias: str, args: list[str]) -> list[str]:
        ...
