"""
Python module generated from Java source file dev.magicmq.pyspigot.util.player.CommandSenderAdapter

Java source file obtained from artifact pyspigot-core version 0.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.util.player import *
from net.md_5.bungee.api.chat import BaseComponent
from typing import Any, Callable, Iterable, Tuple


class CommandSenderAdapter:
    """
    A utility class that wraps a platform-specific command sender object.
    """

    def hasPermission(self, permission: str) -> bool:
        """
        Check if the command sender has a permission via a platform-specific implementation.

        Arguments
        - permission: The permission to check

        Returns
        - True if the command sender has the permission, False if it does not
        """
        ...


    def sendMessage(self, message: str) -> None:
        """
        Send a message to the command sender via a platform-specific implementation.

        Arguments
        - message: The message to send
        """
        ...


    def sendMessage(self, message: list["BaseComponent"]) -> None:
        """
        Send a message to the command sender via a platform-specific implementation.

        Arguments
        - message: The message to send
        """
        ...


    def isPlayer(self) -> bool:
        """
        Check if the command sender is a player via a platform-specific implementation.

        Returns
        - True if the command sender is a player, False if it is not
        """
        ...
