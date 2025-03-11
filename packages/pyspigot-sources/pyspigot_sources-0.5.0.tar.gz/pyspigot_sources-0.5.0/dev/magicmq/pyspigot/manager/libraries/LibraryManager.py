"""
Python module generated from Java source file dev.magicmq.pyspigot.manager.libraries.LibraryManager

Java source file obtained from artifact pyspigot version 0.5.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot import PySpigot
from dev.magicmq.pyspigot.config import PluginConfig
from dev.magicmq.pyspigot.manager.libraries import *
from enum import Enum
from java.io import File
from java.io import IOException
from java.util import Arrays
from java.util import SortedSet
from java.util.concurrent import Callable
from java.util.concurrent import ExecutorService
from java.util.concurrent import Executors
from me.lucko.jarrelocator import JarRelocator
from typing import Any, Callable, Iterable, Tuple


class LibraryManager:
    """
    A manager class to help with dynamically loading Jar files into the classpath at runtime. Most commonly, scripts will not use this directly and PySpigot will be the primary user of this manager.
    
    Internally, this utilizes the jar-relocator library from lucko to dynamically load Jar files at runtime.

    See
    - me.lucko.jarrelocator.JarRelocator
    """

    def shutdown(self) -> None:
        """
        Closes the class loader for scripts.
        """
        ...


    def reload(self) -> None:
        """
        Attempts to load all libraries that are not currently loaded. Libraries that are already loaded will be unaffected.
        """
        ...


    def loadLibrary(self, libName: str) -> "LoadResult":
        """
        Load a library into the classpath.

        Arguments
        - libName: The name of the Jar file to load into the classpath, including the extension (.jar)

        Returns
        - A LoadResult describing the outcome of the load attempt
        """
        ...


    def getClassLoader(self) -> "JarClassLoader":
        """
        Get the JarClassLoader for loading Jar files into the classpath.

        Returns
        - The JarClassLoader
        """
        ...


    @staticmethod
    def get() -> "LibraryManager":
        """
        Get the singleton instance of this LibraryManager.

        Returns
        - The instance
        """
        ...


    class LoadResult(Enum):
        """
        An enum representing the outcome of an attempt to load a library.
        """

        FAILED_FILE = 0
        """
        The library failed to load because the libs folder does not exist.
        """
        FAILED_LOADED = 1
        """
        The library failed to load because it is already loaded.
        """
        FAILED_ERROR = 2
        """
        The library failed to load because of some unrecoverable error.
        """
        SUCCESS = 3
        """
        The library loaded successfully.
        """
