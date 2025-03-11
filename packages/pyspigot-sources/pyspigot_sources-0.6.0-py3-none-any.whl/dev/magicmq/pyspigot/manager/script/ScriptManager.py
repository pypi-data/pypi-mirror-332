"""
Python module generated from Java source file dev.magicmq.pyspigot.manager.script.ScriptManager

Java source file obtained from artifact pyspigot version 0.6.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot import PySpigot
from dev.magicmq.pyspigot.config import PluginConfig
from dev.magicmq.pyspigot.event import ScriptExceptionEvent
from dev.magicmq.pyspigot.event import ScriptLoadEvent
from dev.magicmq.pyspigot.event import ScriptUnloadEvent
from dev.magicmq.pyspigot.manager.command import CommandManager
from dev.magicmq.pyspigot.manager.listener import ListenerManager
from dev.magicmq.pyspigot.manager.placeholder import PlaceholderManager
from dev.magicmq.pyspigot.manager.protocol import ProtocolManager
from dev.magicmq.pyspigot.manager.script import *
from dev.magicmq.pyspigot.manager.task import TaskManager
from dev.magicmq.pyspigot.util import ScriptSorter
from java.io import File
from java.io import FileInputStream
from java.io import FileNotFoundException
from java.io import IOException
from java.util import *
from java.util.stream import Collectors
from org.bukkit import Bukkit
from org.bukkit.scheduler import BukkitTask
from org.python.core import *
from typing import Any, Callable, Iterable, Tuple


class ScriptManager:
    """
    Master manager class for PySpigot. Contains all logic to load, unload, and reload scripts.
    
    Internally, utilizes Jython's org.python.util.PythonInterpreter to run scripts.

    See
    - Script
    """

    def shutdown(self) -> None:
        """
        Called on plugin unload or server shutdown. Gracefully stops and unloads all loaded and running scripts.
        """
        ...


    def loadScripts(self) -> None:
        """
        Loads and runs all scripts contained within the scripts folder. Called on plugin load (I.E. during server start).
        """
        ...


    def getScriptOptions(self, name: str) -> "ScriptOptions":
        """
        Get the ScriptOptions for a particular script.

        Arguments
        - name: The name of the script to fetch options for. Name should contain the file extension (.py)

        Returns
        - A ScriptOptions object representing the options beloinging to the specified script

        Raises
        - FileNotFoundException: If a script file was not found in the scripts folder with the given name
        """
        ...


    def loadScript(self, name: str) -> "RunResult":
        """
        Load a script with the given name.

        Arguments
        - name: The file name of the script to load. Name should contain the file extension (.py)

        Returns
        - A RunResult describing the outcome of the load operation

        Raises
        - FileNotFoundException: If a script file was not found in the scripts folder with the given name
        - IOException: If there was another IOException related to loading the script file
        """
        ...


    def loadScript(self, script: "Script") -> "RunResult":
        """
        Load the given script.

        Arguments
        - script: The script that should be loaded

        Returns
        - A RunResult describing the outcome of the load operation

        Raises
        - IOException: If there was an IOException related to loading the script file
        """
        ...


    def unloadScripts(self) -> None:
        """
        Unload all currently loaded scripts.
        """
        ...


    def unloadScript(self, name: str) -> bool:
        """
        Unload a script with the given name.

        Arguments
        - name: The name of the script to unload. Name should contain the script file extension (.py)

        Returns
        - True if the script was successfully unloaded, False if otherwise
        """
        ...


    def unloadScript(self, script: "Script", error: bool) -> bool:
        """
        Unload a given script.

        Arguments
        - script: The script to unload
        - error: If the script unload was due to an error, pass True. Otherwise, pass False. This value will be passed on to ScriptUnloadEvent

        Returns
        - True if the script was successfully unloaded, False if otherwise
        """
        ...


    def handleScriptException(self, script: "Script", exception: "PyException", message: str) -> None:
        """
        Handles script errors/exceptions, particularly for script logging purposes. Will also attempt to get the traceback of the org.python.core.PyException that was thrown and print it (if it exists).
        
        **Note:** This method will always run synchronously. If it is called from an asynchronous context, it will run inside a synchronous task.

        Arguments
        - script: The script that threw the error
        - exception: The PyException that was thrown
        - message: The message associated with the exception
        """
        ...


    def isScriptRunning(self, name: str) -> bool:
        """
        Check if a script with the given name is currently loaded.

        Arguments
        - name: The name of the script to check. Name should contain the script file extension (.py)

        Returns
        - True if the script is running, False if otherwise
        """
        ...


    def getScript(self, name: str) -> "Script":
        """
        Get a Script object for a loaded and running script

        Arguments
        - name: The name of the script to get. Name should contain the script file extension (.py)

        Returns
        - The Script object for the script, null if no script is loaded and running with the given name
        """
        ...


    def getLoadedScripts(self) -> set["Script"]:
        """
        Get all loaded scripts.

        Returns
        - An immutable set containing all loaded and running scripts
        """
        ...


    def getLoadedScriptNames(self) -> set[str]:
        """
        Get the names of all loaded scripts.

        Returns
        - An immutable list containing the names of all loaded and running scripts
        """
        ...


    def getAllScriptNames(self) -> "SortedSet"[str]:
        """
        Get a set of all script files in the scripts folder.

        Returns
        - An immutable java.util.SortedSet of Strings containing all script files, sorted in alphabetical order
        """
        ...


    @staticmethod
    def get() -> "ScriptManager":
        """
        Get the singleton instance of this ScriptManager.

        Returns
        - The instance
        """
        ...
