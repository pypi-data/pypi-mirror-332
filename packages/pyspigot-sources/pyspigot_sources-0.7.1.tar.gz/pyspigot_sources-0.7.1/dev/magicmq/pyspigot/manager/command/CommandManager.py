"""
Python module generated from Java source file dev.magicmq.pyspigot.manager.command.CommandManager

Java source file obtained from artifact pyspigot version 0.7.1

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot import PySpigot
from dev.magicmq.pyspigot.manager.command import *
from dev.magicmq.pyspigot.manager.script import Script
from dev.magicmq.pyspigot.util import ReflectionUtils
from dev.magicmq.pyspigot.util import ScriptUtils
from java.lang.reflect import Field
from java.lang.reflect import InvocationTargetException
from java.lang.reflect import Method
from org.bukkit import Bukkit
from org.bukkit.command import Command
from org.bukkit.command import SimpleCommandMap
from org.python.core import PyFunction
from typing import Any, Callable, Iterable, Tuple


class CommandManager:
    """
    Manager to interface with Bukkit's command framework. Primarily used by scripts to register and unregister commands.
    """

    def registerCommand(self, commandFunction: Callable, name: str) -> "ScriptCommand":
        """
        Register a new command.
        
        **Note:** This should be called from scripts only!

        Arguments
        - commandFunction: The command function that should be called when the command is executed
        - name: The name of the command to register

        Returns
        - A ScriptCommand representing the command that was registered
        """
        ...


    def registerCommand(self, commandFunction: Callable, tabFunction: Callable, name: str) -> "ScriptCommand":
        """
        Register a new command.
        
        **Note:** This should be called from scripts only!

        Arguments
        - commandFunction: The command function that should be called when the command is executed
        - tabFunction: The tab function that should be called for tab completion of the command
        - name: The name of the command to register

        Returns
        - A ScriptCommand representing the command that was registered
        """
        ...


    def registerCommand(self, commandFunction: Callable, name: str, description: str, usage: str) -> "ScriptCommand":
        """
        Register a new command.
        
        **Note:** This should be called from scripts only!

        Arguments
        - commandFunction: The command function that should be called when the command is executed
        - name: The name of the command to register
        - description: The description of the command
        - usage: The usage message for the command

        Returns
        - A ScriptCommand representing the command that was registered
        """
        ...


    def registerCommand(self, commandFunction: Callable, tabFunction: Callable, name: str, description: str, usage: str) -> "ScriptCommand":
        """
        Register a new command.
        
        **Note:** This should be called from scripts only!

        Arguments
        - commandFunction: The command function that should be called when the command is executed
        - tabFunction: The tab function that should be called for tab completion of the command
        - name: The name of the command to register
        - description: The description of the command
        - usage: The usage message for the command

        Returns
        - A ScriptCommand representing the command that was registered
        """
        ...


    def registerCommand(self, commandFunction: Callable, name: str, description: str, usage: str, aliases: list[str]) -> "ScriptCommand":
        """
        Register a new command.
        
        **Note:** This should be called from scripts only!

        Arguments
        - commandFunction: The command function that should be called when the command is executed
        - name: The name of the command to register
        - description: The description of the command
        - usage: The usage message for the command
        - aliases: A List of String containing all the aliases for this command

        Returns
        - A ScriptCommand representing the command that was registered
        """
        ...


    def registerCommand(self, commandFunction: Callable, tabFunction: Callable, name: str, description: str, usage: str, aliases: list[str]) -> "ScriptCommand":
        """
        Register a new command.
        
        **Note:** This should be called from scripts only!

        Arguments
        - commandFunction: The command function that should be called when the command is executed
        - tabFunction: The tab function that should be called for tab completion of the command
        - name: The name of the command to register
        - description: The description of the command
        - usage: The usage message for the command
        - aliases: A List of String containing all the aliases for this command

        Returns
        - A ScriptCommand representing the command that was registered
        """
        ...


    def registerCommand(self, commandFunction: Callable, tabFunction: Callable, name: str, description: str, usage: str, aliases: list[str], permission: str, permissionMessage: str) -> "ScriptCommand":
        """
        Register a new command.
        
        **Note:** This should be called from scripts only!

        Arguments
        - commandFunction: The command function that should be called when the command is executed
        - tabFunction: The tab function that should be called for tab completion of the command. Can be null
        - name: The name of the command to register
        - description: The description of the command. Use an empty string for no description
        - usage: The usage message for the command
        - aliases: A List of String containing all the aliases for this command. Use an empty list for no aliases
        - permission: The required permission node to use this command. Can be null
        - permissionMessage: The message do display if there is insufficient permission to run the command. Can be null

        Returns
        - A ScriptCommand representing the command that was registered
        """
        ...


    def unregisterCommand(self, command: "ScriptCommand") -> None:
        """
        Unregister a script's command.
        
        **Note:** This should be called from scripts only!

        Arguments
        - command: The command to be unregistered
        """
        ...


    def unregisterCommands(self, script: "Script") -> None:
        """
        Unregister all commands belonging to a particular script.

        Arguments
        - script: The script from which all commands should be unregistered
        """
        ...


    def getCommand(self, script: "Script", name: str) -> "ScriptCommand":
        """
        Get a command associated with a particular script by the command name

        Arguments
        - script: The script
        - name: The name of the command

        Returns
        - The command with this name and associated with the script, or null if none was found
        """
        ...


    def getCommands(self, script: "Script") -> list["ScriptCommand"]:
        """
        Get an immutable list containing all commands belonging to a particular script.

        Arguments
        - script: The script to get commands from

        Returns
        - An immutable list containing all commands belonging to the script. Will return null if no commands belong to the script
        """
        ...


    @staticmethod
    def get() -> "CommandManager":
        """
        Get the singleton instance of this CommandManager

        Returns
        - The instance
        """
        ...
