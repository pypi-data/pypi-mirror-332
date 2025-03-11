"""
Python module generated from Java source file dev.magicmq.pyspigot.manager.protocol.AsyncProtocolManager

Java source file obtained from artifact pyspigot version 0.6.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.comphenix.protocol import AsynchronousManager
from com.comphenix.protocol import PacketType
from com.comphenix.protocol import ProtocolLibrary
from com.comphenix.protocol.async import AsyncListenerHandler
from com.comphenix.protocol.events import ListenerPriority
from dev.magicmq.pyspigot.manager.protocol import *
from dev.magicmq.pyspigot.manager.script import Script
from dev.magicmq.pyspigot.util import ScriptUtils
from org.python.core import PyFunction
from typing import Any, Callable, Iterable, Tuple


class AsyncProtocolManager:
    """
    Manager to interface with ProtocolLib's AsynchronousManager. Primarily used by scripts to register and unregister asynchronous packet listeners.

    See
    - com.comphenix.protocol.AsynchronousManager
    """

    def getAsynchronousManager(self) -> "AsynchronousManager":
        """
        Get the current ProtocolLib AsynchronousManager.

        Returns
        - The com.comphenix.protocol.AsynchronousManager
        """
        ...


    def registerAsyncPacketListener(self, function: Callable, type: "PacketType") -> "ScriptPacketListener":
        """
        Register a new asynchronous packet listener with default priority.
        
        This method will automatically register a PacketReceivingListener or a PacketSendingListener, depending on if the PacketType is for the server or client, respectively.
        
        **Note:** This should be called from scripts only!

        Arguments
        - function: The function that should be called when the packet event occurs
        - type: The packet type to listen for

        Returns
        - A ScriptPacketListener representing the asynchronous packet listener that was registered
        """
        ...


    def registerAsyncPacketListener(self, function: Callable, type: "PacketType", priority: "ListenerPriority") -> "ScriptPacketListener":
        """
        Register a new asynchronous packet listener.
        
        This method will automatically register a PacketReceivingListener or a PacketSendingListener, depending on if the PacketType is for the server or client, respectively.
        
        **Note:** This should be called from scripts only!

        Arguments
        - function: The function that should be called when the packet event occurs
        - type: The packet type to listen for
        - priority: The priority of the asynchronous packet listener relative to other packet listeners

        Returns
        - A ScriptPacketListener representing the asynchronous packet listener that was registered
        """
        ...


    def registerTimeoutPacketListener(self, function: Callable, type: "PacketType") -> "ScriptPacketListener":
        """
        Register a new asynchronous timeout packet listener with default priority.
        
        This method will automatically register a PacketReceivingListener or a PacketSendingListener, depending on if the PacketType is for the server or client, respectively.
        
        **Note:** This should be called from scripts only!

        Arguments
        - function: The function that should be called when the packet event occurs
        - type: The packet type to listen for

        Returns
        - A ScriptPacketListener representing the asynchronous timeout packet listener that was registered
        """
        ...


    def registerTimeoutPacketListener(self, function: Callable, type: "PacketType", priority: "ListenerPriority") -> "ScriptPacketListener":
        """
        Register a new asynchronous timeout packet listener.
        
        This method will automatically register a PacketReceivingListener or a PacketSendingListener, depending on if the PacketType is for the server or client, respectively.
        
        **Note:** This should be called from scripts only!

        Arguments
        - function: The function that should be called when the packet event occurs
        - type: The packet type to listen for
        - priority: The priority of the asynchronous timeout packet listener relative to other asynchronous timeout packet listeners

        Returns
        - A ScriptPacketListener representing the asynchronous timeout packet listener that was registered
        """
        ...


    def unregisterAsyncPacketListener(self, listener: "ScriptPacketListener") -> None:
        """
        Unregister an asynchronous packet listener.
        
        **Note:** This should be called from scripts only!

        Arguments
        - listener: The asynchronous packet listener to unregister
        """
        ...


    def unregisterAsyncPacketListeners(self, script: "Script") -> None:
        """
        Unregister all asynchronous packet listeners belonging to a script.

        Arguments
        - script: The script whose asynchronous packet listeners should be unregistered
        """
        ...


    def getAsyncPacketListeners(self, script: "Script") -> list["ScriptPacketListener"]:
        """
        Get all asynchronous packet listeners associated with a script

        Arguments
        - script: The script to get asynchronous packet listeners from

        Returns
        - A List of ScriptPacketListener containing all asynchronous packet listeners associated with this script. Will return null if there are no asynchronous packet listeners associated with the script
        """
        ...


    def getAsyncPacketListener(self, script: "Script", packetType: "PacketType") -> "ScriptPacketListener":
        """
        Get the asynchronous packet listener for a particular packet type associated with a script

        Arguments
        - script: The script
        - packetType: The packet type

        Returns
        - The ScriptPacketListener associated with the script and packet type, null if there is none
        """
        ...
