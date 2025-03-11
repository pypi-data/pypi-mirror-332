"""
Python module generated from Java source file dev.magicmq.pyspigot.command.subcommands.HelpCommand

Java source file obtained from artifact pyspigot version 0.7.1

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.command import SubCommand
from dev.magicmq.pyspigot.command import SubCommandMeta
from dev.magicmq.pyspigot.command.subcommands import *
from dev.magicmq.pyspigot.config import PluginConfig
from net.md_5.bungee.api import ChatColor
from net.md_5.bungee.api.chat import *
from org.bukkit.command import CommandSender
from org.bukkit.entity import Player
from typing import Any, Callable, Iterable, Tuple


class HelpCommand(SubCommand):

    def onCommand(self, sender: "CommandSender", args: list[str]) -> bool:
        ...
