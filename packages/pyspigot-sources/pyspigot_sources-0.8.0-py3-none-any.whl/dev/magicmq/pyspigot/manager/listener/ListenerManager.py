"""
Python module generated from Java source file dev.magicmq.pyspigot.manager.listener.ListenerManager

Java source file obtained from artifact pyspigot-core version 0.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.manager.listener import *
from dev.magicmq.pyspigot.manager.script import Script
from org.python.core import PyFunction
from typing import Any, Callable, Iterable, Tuple


class ListenerManager:
    """
    Abstract manager to interface with a server-specific event framework. Primarily used by scripts to register and unregister event listeners.
    
    Type `<T>`: The platform-specific Listener class
    
    Type `<S>`: The platform-specific Event class
    
    Type `<U>`: The platform-specific EventPriority class
    """

    def registerListener(self, function: Callable, eventClass: type["S"]) -> "T":
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


    def registerListener(self, function: Callable, eventClass: type["S"], priority: "U") -> "T":
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


    def registerListener(self, function: Callable, eventClass: type["S"], ignoreCancelled: bool) -> "T":
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


    def registerListener(self, function: Callable, eventClass: type["S"], priority: "U", ignoreCancelled: bool) -> "T":
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


    def unregisterListener(self, listener: "T") -> None:
        """
        Unregister an event listener.
        
        **Note:** This should be called from scripts only!

        Arguments
        - listener: The listener to unregister
        """
        ...


    def unregisterListeners(self, script: "Script") -> None:
        """
        Unregister all event listeners belonging to a script.

        Arguments
        - script: The script whose event listeners should be unregistered
        """
        ...


    def getListener(self, script: "Script", eventClass: type["S"]) -> "T":
        """
        Get the event listener for a particular event associated with a script

        Arguments
        - script: The script
        - eventClass: The event

        Returns
        - The listener associated with the script and event, or null if there is none
        """
        ...


    def getListeners(self, script: "Script") -> list["T"]:
        """
        Get all event listeners associated with a script

        Arguments
        - script: The script to get event listeners from

        Returns
        - An immutable List of listeners containing all event listeners associated with the script. Will return null if there are no event listeners associated with the script
        """
        ...


    @staticmethod
    def get() -> "ListenerManager"[Any, Any, Any]:
        """
        Get the singleton instance of this ListenerManager.

        Returns
        - The instance
        """
        ...
