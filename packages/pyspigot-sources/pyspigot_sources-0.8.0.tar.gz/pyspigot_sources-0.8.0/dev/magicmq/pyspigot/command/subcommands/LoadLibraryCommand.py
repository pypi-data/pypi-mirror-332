"""
Python module generated from Java source file dev.magicmq.pyspigot.command.subcommands.LoadLibraryCommand

Java source file obtained from artifact pyspigot-core version 0.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.command import SubCommand
from dev.magicmq.pyspigot.command import SubCommandMeta
from dev.magicmq.pyspigot.command.subcommands import *
from dev.magicmq.pyspigot.manager.libraries import LibraryManager
from dev.magicmq.pyspigot.util.player import CommandSenderAdapter
from net.md_5.bungee.api import ChatColor
from typing import Any, Callable, Iterable, Tuple


class LoadLibraryCommand(SubCommand):

    def onCommand(self, sender: "CommandSenderAdapter", args: list[str]) -> bool:
        ...
