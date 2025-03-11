"""
Python module generated from Java source file dev.magicmq.pyspigot.PluginListener

Java source file obtained from artifact pyspigot version 0.5.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot import *
from dev.magicmq.pyspigot.config import PluginConfig
from dev.magicmq.pyspigot.util import StringUtils
from net.md_5.bungee.api.chat import *
from net.md_5.bungee.api.chat.hover.content import Text
from org.bukkit import Bukkit
from org.bukkit.entity import Player
from org.bukkit.event import EventHandler
from org.bukkit.event import Listener
from org.bukkit.event.player import PlayerJoinEvent
from typing import Any, Callable, Iterable, Tuple


class PluginListener(Listener):
    """
    Main listener of the plugin. Used only for notifying if using an outdated version of the plugin on server join.
    """

    def onJoin(self, event: "PlayerJoinEvent") -> None:
        ...
