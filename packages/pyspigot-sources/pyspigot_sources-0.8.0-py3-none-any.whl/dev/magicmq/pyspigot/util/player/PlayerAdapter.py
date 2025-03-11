"""
Python module generated from Java source file dev.magicmq.pyspigot.util.player.PlayerAdapter

Java source file obtained from artifact pyspigot-core version 0.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.util.player import *
from net.md_5.bungee.api.chat import BaseComponent
from typing import Any, Callable, Iterable, Tuple


class PlayerAdapter:
    """
    A utility class that wraps a platform-specific player object.
    """

    def hasPermission(self, permission: str) -> bool:
        """
        Check if the player has a permission via a platform-specific implementation.

        Arguments
        - permission: The permission to check

        Returns
        - True if the player has the permission, False if they do not
        """
        ...


    def sendMessage(self, message: list["BaseComponent"]) -> None:
        """
        Send a message to the player via a platform-specific implementation.

        Arguments
        - message: The message to send
        """
        ...
