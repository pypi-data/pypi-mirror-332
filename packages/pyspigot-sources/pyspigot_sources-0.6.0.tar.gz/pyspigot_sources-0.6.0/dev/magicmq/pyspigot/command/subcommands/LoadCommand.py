"""
Python module generated from Java source file dev.magicmq.pyspigot.command.subcommands.LoadCommand

Java source file obtained from artifact pyspigot version 0.6.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.command import SubCommand
from dev.magicmq.pyspigot.command import SubCommandMeta
from dev.magicmq.pyspigot.command.subcommands import *
from dev.magicmq.pyspigot.manager.script import RunResult
from dev.magicmq.pyspigot.manager.script import ScriptManager
from java.io import FileNotFoundException
from java.io import IOException
from org.bukkit import ChatColor
from org.bukkit.command import CommandSender
from typing import Any, Callable, Iterable, Tuple


class LoadCommand(SubCommand):

    def onCommand(self, sender: "CommandSender", args: list[str]) -> bool:
        ...


    def onTabComplete(self, sender: "CommandSender", args: list[str]) -> list[str]:
        ...
