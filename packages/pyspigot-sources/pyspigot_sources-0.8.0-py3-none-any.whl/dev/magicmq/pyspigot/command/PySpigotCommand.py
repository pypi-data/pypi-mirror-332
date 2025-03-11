"""
Python module generated from Java source file dev.magicmq.pyspigot.command.PySpigotCommand

Java source file obtained from artifact pyspigot-core version 0.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot import PyCore
from dev.magicmq.pyspigot.command import *
from dev.magicmq.pyspigot.command.subcommands import HelpCommand
from dev.magicmq.pyspigot.command.subcommands import InfoCommand
from dev.magicmq.pyspigot.command.subcommands import ListScriptsCommand
from dev.magicmq.pyspigot.command.subcommands import LoadCommand
from dev.magicmq.pyspigot.command.subcommands import LoadLibraryCommand
from dev.magicmq.pyspigot.command.subcommands import ReloadAllCommand
from dev.magicmq.pyspigot.command.subcommands import ReloadCommand
from dev.magicmq.pyspigot.command.subcommands import ReloadConfigCommand
from dev.magicmq.pyspigot.command.subcommands import UnloadCommand
from dev.magicmq.pyspigot.util.player import CommandSenderAdapter
from java.util import Arrays
from net.md_5.bungee.api import ChatColor
from typing import Any, Callable, Iterable, Tuple


class PySpigotCommand:

    def __init__(self):
        ...


    def onCommand(self, sender: "CommandSenderAdapter", label: str, args: list[str]) -> bool:
        ...


    def onTabComplete(self, sender: "CommandSenderAdapter", args: list[str]) -> list[str]:
        ...
