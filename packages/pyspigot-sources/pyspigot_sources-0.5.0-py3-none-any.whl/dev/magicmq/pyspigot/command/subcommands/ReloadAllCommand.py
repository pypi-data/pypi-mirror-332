"""
Python module generated from Java source file dev.magicmq.pyspigot.command.subcommands.ReloadAllCommand

Java source file obtained from artifact pyspigot version 0.5.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot import PySpigot
from dev.magicmq.pyspigot.command import SubCommand
from dev.magicmq.pyspigot.command import SubCommandMeta
from dev.magicmq.pyspigot.command.subcommands import *
from dev.magicmq.pyspigot.manager.libraries import LibraryManager
from dev.magicmq.pyspigot.manager.script import ScriptManager
from org.bukkit import ChatColor
from org.bukkit.command import CommandSender
from typing import Any, Callable, Iterable, Tuple


class ReloadAllCommand(SubCommand):

    def onCommand(self, sender: "CommandSender", args: list[str]) -> bool:
        ...
