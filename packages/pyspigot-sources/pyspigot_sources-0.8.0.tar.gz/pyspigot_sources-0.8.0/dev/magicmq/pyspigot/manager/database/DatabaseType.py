"""
Python module generated from Java source file dev.magicmq.pyspigot.manager.database.DatabaseType

Java source file obtained from artifact pyspigot-core version 0.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.manager.database import *
from dev.magicmq.pyspigot.manager.database.mongo import MongoDatabase
from dev.magicmq.pyspigot.manager.database.sql import SqlDatabase
from enum import Enum
from typing import Any, Callable, Iterable, Tuple


class DatabaseType(Enum):
    """
    Utility enum to represent different database types available for scripts to use.
    """

    SQL = (SqlDatabase, /*Host, port, database, user, password*/
    "jdbc:mysql://%s:%s/%s?user=%s&password=%s")
    """
    An SQL database type.
    """
    MONGO_DB = (MongoDatabase, /*User, password, host, port*/
    "mongodb://%s:%s@%s:%s")
    """
    A MongoDB database type.
    """
    MONGO_DB_NO_AUTH = (MongoDatabase, "mongodb://%s:%s")
    """
    A MongoDB database type without authentication.
    """


    def getDbClass(self) -> type["Database"]:
        """
        Get the class that pertains to the database type. Will be a subclass of Database

        Returns
        - The class associated with the database type
        """
        ...


    def getUri(self) -> str:
        """
        Get the URI scheme associated with the database type.

        Returns
        - The URI scheme associated with the database type
        """
        ...
