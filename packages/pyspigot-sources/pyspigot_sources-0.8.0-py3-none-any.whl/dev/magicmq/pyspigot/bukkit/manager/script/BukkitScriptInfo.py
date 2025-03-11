"""
Python module generated from Java source file dev.magicmq.pyspigot.bukkit.manager.script.BukkitScriptInfo

Java source file obtained from artifact pyspigot-bukkit version 0.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.bukkit import PySpigot
from dev.magicmq.pyspigot.bukkit.manager.placeholder import PlaceholderManager
from dev.magicmq.pyspigot.bukkit.manager.placeholder import ScriptPlaceholder
from dev.magicmq.pyspigot.bukkit.manager.protocol import ProtocolManager
from dev.magicmq.pyspigot.bukkit.manager.protocol import ScriptPacketListener
from dev.magicmq.pyspigot.bukkit.manager.script import *
from dev.magicmq.pyspigot.manager.script import Script
from dev.magicmq.pyspigot.manager.script import ScriptInfo
from net.md_5.bungee.api import ChatColor
from typing import Any, Callable, Iterable, Tuple


class BukkitScriptInfo(ScriptInfo):
    """
    The Bukkit-specific implementation of the dev.magicmq.pyspigot.manager.script.ScriptInfo class, for printing information related to Bukkit-specific managers.
    """

    def printPlatformManagerInfo(self, script: "Script", appendTo: "StringBuilder") -> None:
        ...
