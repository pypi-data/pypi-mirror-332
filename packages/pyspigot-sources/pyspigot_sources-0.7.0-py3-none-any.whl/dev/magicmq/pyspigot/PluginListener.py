"""
Python module generated from Java source file dev.magicmq.pyspigot.PluginListener

Java source file obtained from artifact pyspigot version 0.7.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot import *
from dev.magicmq.pyspigot.config import PluginConfig
from dev.magicmq.pyspigot.manager.script import Script
from dev.magicmq.pyspigot.manager.script import ScriptManager
from dev.magicmq.pyspigot.util import StringUtils
from net.md_5.bungee.api import ChatColor
from net.md_5.bungee.api.chat import *
from org.bukkit import Bukkit
from org.bukkit.entity import Player
from org.bukkit.event import EventHandler
from org.bukkit.event import Listener
from org.bukkit.event.player import PlayerJoinEvent
from org.bukkit.event.server import PluginDisableEvent
from typing import Any, Callable, Iterable, Tuple


class PluginListener(Listener):
    """
    Main listener of the plugin. Currently used to listen for plugin disable (to disable scripts that depend on a disabled plugin) and to listen for player join to send PySpigot update messages.
    """

    def onDisable(self, event: "PluginDisableEvent") -> None:
        ...


    def onJoin(self, event: "PlayerJoinEvent") -> None:
        ...
