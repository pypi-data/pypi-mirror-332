"""
Python module generated from Java source file dev.magicmq.pyspigot.manager.protocol.PacketSendingListener

Java source file obtained from artifact pyspigot version 0.7.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.comphenix.protocol import PacketType
from com.comphenix.protocol.events import ListenerPriority
from com.comphenix.protocol.events import PacketEvent
from dev.magicmq.pyspigot.manager.protocol import *
from dev.magicmq.pyspigot.manager.script import Script
from org.python.core import PyFunction
from typing import Any, Callable, Iterable, Tuple


class PacketSendingListener(ScriptPacketListener):
    """
    A listener that listens for packets sent by the server to the client.

    See
    - ScriptPacketListener
    """

    def __init__(self, script: "Script", function: Callable, packetType: "PacketType", listenerPriority: "ListenerPriority", listenerType: "ListenerType"):
        """
        Arguments
        - script: The script associated with this packet listener
        - function: The function to be called when the packet is sent
        - packetType: The packet type to listen for
        - listenerPriority: The com.comphenix.protocol.events.ListenerPriority of this listener
        - listenerType: The ListenerType of this listener
        """
        ...


    def onPacketSending(self, event: "PacketEvent") -> None:
        """

        """
        ...
