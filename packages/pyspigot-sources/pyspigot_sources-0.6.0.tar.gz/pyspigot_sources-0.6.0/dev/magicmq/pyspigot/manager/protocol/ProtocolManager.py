"""
Python module generated from Java source file dev.magicmq.pyspigot.manager.protocol.ProtocolManager

Java source file obtained from artifact pyspigot version 0.6.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.comphenix.protocol import PacketType
from com.comphenix.protocol import ProtocolLibrary
from com.comphenix.protocol.events import ListenerPriority
from com.comphenix.protocol.events import PacketContainer
from dev.magicmq.pyspigot.manager.protocol import *
from dev.magicmq.pyspigot.manager.script import Script
from dev.magicmq.pyspigot.util import ScriptUtils
from org.bukkit import Location
from org.bukkit.entity import Entity
from org.bukkit.entity import Player
from org.python.core import PyFunction
from typing import Any, Callable, Iterable, Tuple


class ProtocolManager:
    """
    Manager to interface with ProtocolLib's ProtocolManager. Primarily used by scripts to register and unregister packet listeners.
    
    Do not call this manager if ProtocolLib is not loaded and enabled on the server! It will not work.

    See
    - com.comphenix.protocol.ProtocolManager
    """

    def getProtocolManager(self) -> "com.comphenix.protocol.ProtocolManager":
        """
        Get the current ProtocolLib ProtocolManager.

        Returns
        - The com.comphenix.protocol.ProtocolManager
        """
        ...


    def async(self) -> "AsyncProtocolManager":
        """
        Get the async protocol manager for working with asynchronous listeners.

        Returns
        - The AsyncProtocolManager
        """
        ...


    def registerPacketListener(self, function: Callable, type: "PacketType") -> "ScriptPacketListener":
        """
        Register a new packet listener with default priority.
        
        This method will automatically register a PacketReceivingListener or a PacketSendingListener, depending on if the PacketType is for the server or client, respectively.
        
        **Note:** This should be called from scripts only!

        Arguments
        - function: The function that should be called when the packet event occurs
        - type: The packet type to listen for

        Returns
        - A ScriptPacketListener representing the packet listener that was registered
        """
        ...


    def registerPacketListener(self, function: Callable, type: "PacketType", priority: "ListenerPriority") -> "ScriptPacketListener":
        """
        Register a new packet listener.
        
        This method will automatically register a PacketReceivingListener or a PacketSendingListener, depending on if the PacketType is for the server or client, respectively.
        
        **Note:** This should be called from scripts only!

        Arguments
        - function: The function that should be called when the packet event occurs
        - type: The packet type to listen for
        - priority: The priority of the packet listener relative to other packet listeners

        Returns
        - A ScriptPacketListener representing the packet listener that was registered
        """
        ...


    def unregisterPacketListener(self, listener: "ScriptPacketListener") -> None:
        """
        Unregister a packet listener.
        
        **Note:** This should be called from scripts only!

        Arguments
        - listener: The packet listener to unregister
        """
        ...


    def unregisterPacketListeners(self, script: "Script") -> None:
        """
        Unregister all normal packet listeners belonging to a script, excluding asynchronous packet listeners.
        
        Use AsyncProtocolManager.unregisterAsyncPacketListeners(Script) to unregister asynchronous packet listeners.

        Arguments
        - script: The script whose normal packet listeners should be unregistered
        """
        ...


    def getPacketListeners(self, script: "Script") -> list["ScriptPacketListener"]:
        """
        Get all normal packet listeners associated with a script, excluding asynchronous packet listeners.
        
        Use AsyncProtocolManager.getAsyncPacketListeners(Script) to get a script's asynchronous packet listeners.

        Arguments
        - script: The script to get normal packet listeners from

        Returns
        - A List of ScriptPacketListener containing all normal packet listeners associated with this script. Will return null if there are no normal packet listeners associated with the script
        """
        ...


    def getPacketListener(self, script: "Script", packetType: "PacketType") -> "ScriptPacketListener":
        """
        Get the normal packet listener for a particular packet type associated with a script.
        
        Use AsyncProtocolManager.getAsyncPacketListener(Script, PacketType) to get a script's asynchronous packet listener of a specific packet type.

        Arguments
        - script: The script
        - packetType: The packet type

        Returns
        - The ScriptPacketListener associated with the script and packet type, null if there is none
        """
        ...


    def createPacket(self, type: "PacketType") -> "PacketContainer":
        """
        Create a new packet with the given type. This method will assign sensible default values to all fields within the packet where a non-null value is required.
        
        This method is the preferred way to create a packet that will later be sent or broadcasted.
        
        **Note:** This should be called from scripts only!

        Arguments
        - type: The type of packet to create

        Returns
        - A com.comphenix.protocol.events.PacketContainer representing the packet that was created.
        """
        ...


    def sendServerPacket(self, player: "Player", packet: "PacketContainer") -> None:
        """
        Send a packet to a player.
        
        **Note:** This should be called from scripts only!

        Arguments
        - player: The player to send the packet to
        - packet: The packet to send
        """
        ...


    def broadcastServerPacket(self, packet: "PacketContainer") -> None:
        """
        Broadcast a packet to the entire server. The packet will be sent to all online players.
        
        **Note:** This should be called from scripts only!

        Arguments
        - packet: The packet to broadcast
        """
        ...


    def broadcastServerPacket(self, packet: "PacketContainer", entity: "Entity") -> None:
        """
        Broadcast a packet to players receiving information about a particular entity. Will also broadcast the packet to the entity, if the entity is a tracker.
        
        **Note:** This should be called from scripts only!

        Arguments
        - packet: The packet to broadcast
        - entity: The entity whose trackers will be informed

        See
        - ProtocolManager.broadcastServerPacket(PacketContainer, Entity, boolean)
        """
        ...


    def broadcastServerPacket(self, packet: "PacketContainer", entity: "Entity", includeTracker: bool) -> None:
        """
        Broadcast a packet to players receiving information about a particular entity.
        
        Usually, this would be every player in the same world within an observable distance. If the entity is a player, it will be included only if `includeTracker` is set to `True`.
        
        **Note:** This should be called from scripts only!

        Arguments
        - packet: The packet to broadcast
        - entity: The entity whose trackers will be informed
        - includeTracker: Whether to also transmit the packet to the entity, if it is a tracker
        """
        ...


    def broadcastServerPacket(self, packet: "PacketContainer", origin: "Location", maxObserverDistance: int) -> None:
        """
        Broadcast a packet to all players within a given max observer distance from an origin location (center point).
        
        **Note:** This should be called from scripts only!

        Arguments
        - packet: The packet to broadcast
        - origin: The origin location (center point) to consider when calculating distance to each observer
        - maxObserverDistance: The maximum distance from origin wherein packets will be broadcasted
        """
        ...


    def broadcastServerPacket(self, packet: "PacketContainer", targetPlayers: Iterable["Player"]) -> None:
        """
        Broadcast a packet to a specified list of players.
        
        **Note:** This should be called from scripts only!

        Arguments
        - packet: The packet to broadcast
        - targetPlayers: The list of players to which the packet should be broadcasted
        """
        ...


    @staticmethod
    def get() -> "ProtocolManager":
        """
        Get the singleton instance of this ProtocolManager.

        Returns
        - The instance
        """
        ...
