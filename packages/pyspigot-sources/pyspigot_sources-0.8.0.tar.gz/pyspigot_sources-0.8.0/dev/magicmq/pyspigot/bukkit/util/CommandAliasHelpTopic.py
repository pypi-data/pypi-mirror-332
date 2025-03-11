"""
Python module generated from Java source file dev.magicmq.pyspigot.bukkit.util.CommandAliasHelpTopic

Java source file obtained from artifact pyspigot-bukkit version 0.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.bukkit.util import *
from org.bukkit import ChatColor
from org.bukkit.command import CommandSender
from org.bukkit.help import HelpMap
from org.bukkit.help import HelpTopic
from typing import Any, Callable, Iterable, Tuple


class CommandAliasHelpTopic(HelpTopic):
    """
    Represents a help topic for an alias of a command.
    
    Copied from org.bukkit.craftbukkit.help.CommandAliasHelpTopic
    """

    def __init__(self, alias: str, aliasFor: str, helpMap: "HelpMap"):
        ...


    def getFullText(self, forWho: "CommandSender") -> str:
        ...


    def canSee(self, commandSender: "CommandSender") -> bool:
        ...
