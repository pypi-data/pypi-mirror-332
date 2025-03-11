"""
Python module generated from Java source file dev.magicmq.pyspigot.bukkit.util.player.BukkitPlayer

Java source file obtained from artifact pyspigot-bukkit version 0.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.bukkit.util.player import *
from dev.magicmq.pyspigot.util.player import PlayerAdapter
from net.md_5.bungee.api.chat import BaseComponent
from org.bukkit.entity import Player
from typing import Any, Callable, Iterable, Tuple


class BukkitPlayer(PlayerAdapter):
    """
    A wrapper for the Bukkit org.bukkit.entity.Player class.
    """

    def __init__(self, player: "Player"):
        """
        Arguments
        - player: The Bukkit Player
        """
        ...


    def hasPermission(self, permission: str) -> bool:
        ...


    def sendMessage(self, message: list["BaseComponent"]) -> None:
        ...
