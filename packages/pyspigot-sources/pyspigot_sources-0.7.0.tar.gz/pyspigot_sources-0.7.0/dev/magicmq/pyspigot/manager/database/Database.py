"""
Python module generated from Java source file dev.magicmq.pyspigot.manager.database.Database

Java source file obtained from artifact pyspigot version 0.7.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.manager.database import *
from dev.magicmq.pyspigot.manager.script import Script
from typing import Any, Callable, Iterable, Tuple


class Database:
    """
    Represents a database to which a script is connected and can read/write.
    """

    def __init__(self, script: "Script"):
        """
        Arguments
        - script: The script associated with this database connection
        """
        ...


    def open(self) -> bool:
        """
        Opens a connection to the database.

        Returns
        - True if opening the connection to the database was successful, False if otherwise
        """
        ...


    def close(self) -> bool:
        """
        Closes a connection to the database.

        Returns
        - True if closing the connection to the database was successful, False if otherwise
        """
        ...


    def getScript(self) -> "Script":
        """
        Get the script associated with this database connection.

        Returns
        - The script associated with this database connection
        """
        ...


    def getDatabaseId(self) -> int:
        """
        Get the ID of this database connection.

        Returns
        - The ID
        """
        ...


    def toString(self) -> str:
        """
        Prints a representation of this Database in string format.

        Returns
        - A string representation of this Database
        """
        ...
