"""
Python module generated from Java source file dev.magicmq.pyspigot.manager.listener.ListenerManager

Java source file obtained from artifact pyspigot version 0.5.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot import PySpigot
from dev.magicmq.pyspigot.manager.listener import *
from dev.magicmq.pyspigot.manager.script import Script
from dev.magicmq.pyspigot.util import ScriptUtils
from java.lang.reflect import InvocationTargetException
from java.lang.reflect import Method
from org.bukkit import Bukkit
from org.bukkit.event import Event
from org.bukkit.event import EventPriority
from org.bukkit.event import HandlerList
from org.python.core import PyFunction
from typing import Any, Callable, Iterable, Tuple


class ListenerManager:
    """
    Manager to interface with Bukkit's event framework. Primarily used by scripts to register and unregister event listeners.
    """

    def registerListener(self, function: Callable, eventClass: type["Event"]) -> "ScriptEventListener":
        """
        Register a new event listener with default priority.
        
        **Note:** This should be called from scripts only!

        Arguments
        - function: The function that should be called when the event occurs
        - eventClass: The type of event to listen to

        Returns
        - The ScriptEventListener that was registered
        """
        ...


    def registerListener(self, function: Callable, eventClass: type["Event"], priority: "EventPriority") -> "ScriptEventListener":
        """
        Register a new event listener.
        
        **Note:** This should be called from scripts only!

        Arguments
        - function: The function that should be called when the event occurs
        - eventClass: The type of event to listen to
        - priority: The priority of the event relative to other listeners

        Returns
        - The ScriptEventListener that was registered
        """
        ...


    def registerListener(self, function: Callable, eventClass: type["Event"], ignoreCancelled: bool) -> "ScriptEventListener":
        """
        Register a new event listener with default priority.
        
        **Note:** This should be called from scripts only!

        Arguments
        - function: The function that should be called when the event occurs
        - eventClass: The type of event to listen to
        - ignoreCancelled: If True, the event listener will not be called if the event has been previously cancelled by another listener.

        Returns
        - The ScriptEventListener that was registered
        """
        ...


    def registerListener(self, function: Callable, eventClass: type["Event"], priority: "EventPriority", ignoreCancelled: bool) -> "ScriptEventListener":
        """
        Register a new event listener.
        
        **Note:** This should be called from scripts only!

        Arguments
        - function: The function that should be called when the event occurs
        - eventClass: The type of event to listen to
        - priority: The priority of the event relative to other listeners
        - ignoreCancelled: If True, the event listener will not be called if the event has been previously cancelled by another listener.

        Returns
        - The ScriptEventListener that was registered
        """
        ...


    def unregisterListener(self, listener: "ScriptEventListener") -> None:
        """
        Unregister an event listener.
        
        **Note:** This should be called from scripts only!

        Arguments
        - listener: The listener to unregister
        """
        ...


    def getListeners(self, script: "Script") -> list["ScriptEventListener"]:
        """
        Get all event listeners associated with a script

        Arguments
        - script: The script to get event listeners from

        Returns
        - An immutable List of ScriptEventListener containing all events associated with the script. Will return null if there are no event listeners associated with the script
        """
        ...


    def getEventListener(self, script: "Script", eventClass: type["Event"]) -> "ScriptEventListener":
        """
        Get the event listener for a particular event associated with a script

        Arguments
        - script: The script
        - eventClass: The event

        Returns
        - The ScriptEventListener associated with the script and event, null if there is none
        """
        ...


    def unregisterListeners(self, script: "Script") -> None:
        """
        Unregister all event listeners belonging to a script.

        Arguments
        - script: The script whose event listeners should be unregistered
        """
        ...


    @staticmethod
    def get() -> "ListenerManager":
        """
        Get the singleton instance of this ListenerManager.

        Returns
        - The instance
        """
        ...
