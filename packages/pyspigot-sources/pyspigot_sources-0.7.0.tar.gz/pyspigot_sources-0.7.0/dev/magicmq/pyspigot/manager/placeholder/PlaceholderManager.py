"""
Python module generated from Java source file dev.magicmq.pyspigot.manager.placeholder.PlaceholderManager

Java source file obtained from artifact pyspigot version 0.7.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.manager.placeholder import *
from dev.magicmq.pyspigot.manager.script import Script
from dev.magicmq.pyspigot.util import ScriptUtils
from org.python.core import PyFunction
from typing import Any, Callable, Iterable, Tuple


class PlaceholderManager:
    """
    Manager to interface with PlaceholderAPI. Primarily used by scripts to register and unregister placeholder expansions.
    
    Do not call this manager if PlaceholderAPI is not loaded and enabled on the server! It will not work.
    """

    def registerPlaceholder(self, placeholderFunction: Callable) -> "ScriptPlaceholder":
        """
        Register a new script placeholder expansion.
        
        **Note:** This should be called from scripts only!

        Arguments
        - placeholderFunction: The function that should be called when the placeholder is used

        Returns
        - A ScriptPlaceholder representing the placeholder expansion that was registered
        """
        ...


    def registerPlaceholder(self, placeholderFunction: Callable, author: str, version: str) -> "ScriptPlaceholder":
        """
        Register a new script placeholder expansion.
        
        **Note:** This should be called from scripts only!

        Arguments
        - placeholderFunction: The function that should be called when the placeholder is used
        - author: The author of the placeholder
        - version: The version of the placeholder

        Returns
        - A ScriptPlaceholder representing the placeholder expansion that was registered
        """
        ...


    def unregisterPlaceholder(self, placeholder: "ScriptPlaceholder") -> None:
        """
        Unregister a script placeholder expansion.
        
        **Note:** This should be called from scripts only!

        Arguments
        - placeholder: The placeholder expansion to unregister
        """
        ...


    def unregisterPlaceholder(self, script: "Script") -> bool:
        """
        Unregister a script's placeholder expansion.
        
        Similar to .unregisterPlaceholder(ScriptPlaceholder), except this method can be called from outside a script to unregister a script's placeholder expansion (for example when the script is unloaded and stopped).

        Arguments
        - script: The script whose placeholder should be unregistered

        Returns
        - True if a placeholder was unregistered, False if the script did not have a placeholder registered previously
        """
        ...


    def getPlaceholder(self, script: "Script") -> "ScriptPlaceholder":
        """
        Get a script's placeholder expansion.

        Arguments
        - script: The script to get the placeholder expansion from

        Returns
        - The script's placeholder expansion, null if the script does not have a placeholder expansion registered
        """
        ...


    @staticmethod
    def get() -> "PlaceholderManager":
        """
        Get the singleton instance of this PlaceholderManager.

        Returns
        - The instance
        """
        ...
