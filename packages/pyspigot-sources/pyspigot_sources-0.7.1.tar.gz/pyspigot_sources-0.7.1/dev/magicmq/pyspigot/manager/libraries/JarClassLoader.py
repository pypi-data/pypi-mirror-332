"""
Python module generated from Java source file dev.magicmq.pyspigot.manager.libraries.JarClassLoader

Java source file obtained from artifact pyspigot version 0.7.1

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.manager.libraries import *
from java.net import MalformedURLException
from java.net import URL
from java.net import URLClassLoader
from java.nio.file import Path
from typing import Any, Callable, Iterable, Tuple


class JarClassLoader(URLClassLoader):
    """
    Utility class for assisting with loading Jar files into the classpath.
    """

    def __init__(self, parentClassLoader: "ClassLoader"):
        """
        Initialize a new JarClassLoader using a parent class loader.

        Arguments
        - parentClassLoader: The parent class loader to use
        """
        ...


    def addJarToClasspath(self, file: "Path") -> None:
        """
        Add a new Jar to the classpath.

        Arguments
        - file: The Jar file to add to the classpath

        Raises
        - MalformedURLException: If the file has an invalid URL
        """
        ...


    def isJarInClassPath(self, file: "Path") -> bool:
        """
        Check if a Jar file is in the classpath.

        Arguments
        - file: The Jar file to check

        Returns
        - True if the Jar file is already in the classpath, False if otherwise
        """
        ...
