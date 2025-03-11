"""
Python module generated from Java source file dev.magicmq.pyspigot.manager.database.sql.SqlDatabase

Java source file obtained from artifact pyspigot-core version 0.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.zaxxer.hikari import HikariConfig
from com.zaxxer.hikari import HikariDataSource
from dev.magicmq.pyspigot.manager.database import Database
from dev.magicmq.pyspigot.manager.database.sql import *
from dev.magicmq.pyspigot.manager.script import Script
from typing import Any, Callable, Iterable, Tuple


class SqlDatabase(Database):
    """
    Represents an open connection to an SQL database.
    """

    def __init__(self, script: "Script", hikariConfig: "HikariConfig"):
        """
        Arguments
        - script: The script associated with this SQLDatabase
        - hikariConfig: The configuration options for the SQLDatabase connection
        """
        ...


    def open(self) -> bool:
        """

        """
        ...


    def close(self) -> bool:
        """

        """
        ...


    def getHikariDataSource(self) -> "HikariDataSource":
        """
        Get the underlying com.zaxxer.hikari.HikariDataSource associated with this SQLDatabase.

        Returns
        - The underlying HikariDataSource
        """
        ...


    def select(self, sql: str) -> dict[str, list["Object"]]:
        """
        Select from the SQL database.
        
        **Note:** This should be called from scripts only!

        Arguments
        - sql: The select statement

        Returns
        - A java.util.Map containing the data returned from the selection. Functionally identical to a python dict, where keys are column names and values are column data, with preserved order

        Raises
        - SQLException: If there was an exception when selecting from the database
        """
        ...


    def select(self, sql: str, values: list["Object"]) -> dict[str, list["Object"]]:
        """
        Select from the SQL database with the provided values that should be inserted into the select statement.
        
        **Note:** This should be called from scripts only!

        Arguments
        - sql: The select statement
        - values: The values that should be inserted into the select statement

        Returns
        - A java.util.Map containing the data returned from the selection. Functionally identical to a python dict, where keys are column names and values are column data, with preserved order

        Raises
        - SQLException: If there was an exception when selecting from the database
        """
        ...


    def update(self, sql: str) -> int:
        """
        Update the SQL database.
        
        **Note:** This should be called from scripts only!

        Arguments
        - sql: The update statement

        Returns
        - The number of rows that were affected by the update statement

        Raises
        - SQLException: If there was an exception when updating the database
        """
        ...


    def update(self, sql: str, values: list["Object"]) -> int:
        """
        Update the SQL database with the provided values that should be inserted into the update statement.
        
        **Note:** This should be called from scripts only!

        Arguments
        - sql: The update statement
        - values: The values that should be inserted into the update statement

        Returns
        - The number of rows that were affected by the update statement

        Raises
        - SQLException: If there was an exception when updating the database
        """
        ...


    def toString(self) -> str:
        """
        Prints a representation of this SqlDatabase in string format, including the ID, URI, and com.zaxxer.hikari.HikariDataSource

        Returns
        - A string representation of the SqlDatabase
        """
        ...
