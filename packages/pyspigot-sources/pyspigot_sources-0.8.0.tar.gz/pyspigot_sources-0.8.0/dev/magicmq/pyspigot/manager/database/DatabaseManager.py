"""
Python module generated from Java source file dev.magicmq.pyspigot.manager.database.DatabaseManager

Java source file obtained from artifact pyspigot-core version 0.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.mongodb import ConnectionString
from com.mongodb import MongoClientSettings
from com.zaxxer.hikari import HikariConfig
from dev.magicmq.pyspigot.manager.database import *
from dev.magicmq.pyspigot.manager.database.mongo import MongoDatabase
from dev.magicmq.pyspigot.manager.database.sql import SqlDatabase
from dev.magicmq.pyspigot.manager.script import Script
from dev.magicmq.pyspigot.util import ScriptUtils
from typing import Any, Callable, Iterable, Tuple


class DatabaseManager:
    """
    Manager that allows connection to and interact with a variety of database types. Primarily used by scripts to interact with external databases, such as SQL and MongoDB.
    """

    def newHikariConfig(self) -> "HikariConfig":
        """
        Get a new com.zaxxer.hikari.HikariConfig for specifying configuration options.
        
        **Note:** This should be called from scripts only!

        Returns
        - A new HikariConfig
        """
        ...


    def connectSql(self, host: str, port: str, database: str, username: str, password: str) -> "SqlDatabase":
        """
        Open a new connection with an SQL database, using the default configuration options.
        
        **Note:** This should be called from scripts only!

        Arguments
        - host: The host URL or IP of the SQL database
        - port: The port of the SQL database
        - database: The name of the SQL database
        - username: The username of the SQL database
        - password: The password of the SQL database

        Returns
        - An SqlDatabase object representing an open connection to the database
        """
        ...


    def connectSql(self, host: str, port: str, database: str, username: str, password: str, hikariConfig: "HikariConfig") -> "SqlDatabase":
        """
        Open a new connection with an SQL database, using the specified configuration options.
        
        **Note:** This should be called from scripts only!

        Arguments
        - host: The host URL or IP of the SQL database
        - port: The port of the SQL database
        - database: The name of the SQL database
        - username: The username of the SQL database
        - password: The password of the SQL database
        - hikariConfig: A com.zaxxer.hikari.HikariConfig object representing the configuration options for the connection

        Returns
        - An SqlDatabase object representing an open connection to the database
        """
        ...


    def connectSql(self, uri: str) -> "SqlDatabase":
        """
        Open a new connection with an SQL database, using the provided connection URI.
        
        **Note:** This should be called from scripts only!

        Arguments
        - uri: The connection string to define the connection, including options

        Returns
        - An SqlDatabase object representing an open connection to the database
        """
        ...


    def connectSql(self, uri: str, hikariConfig: "HikariConfig") -> "SqlDatabase":
        """
        Open a new connection with an SQL database, using the provided connection URI and configuration options.
        
        **Note:** This should be called from scripts only!

        Arguments
        - uri: The connection string to define the connection, including options
        - hikariConfig: A com.zaxxer.hikari.HikariConfig object representing the configuration options for the connection

        Returns
        - An SqlDatabase object representing an open connection to the database
        """
        ...


    def connectSql(self, hikariConfig: "HikariConfig") -> "SqlDatabase":
        """
        Open a new connection with an SQL database, using the provided configuration.
        
        **Note:** This should be called from scripts only!

        Arguments
        - hikariConfig: The configuration for the connection

        Returns
        - An SqlDatabase object representing an open connection to the database
        """
        ...


    def newMongoClientSettings(self) -> "MongoClientSettings.Builder":
        """
        Get a new com.mongodb.MongoClientSettings.Builder for specifying client settings.
        
        **Note:** This should be called from scripts only!

        Returns
        - A new MongoClientSettings builder
        """
        ...


    def connectMongo(self, host: str, port: str, username: str, password: str) -> "MongoDatabase":
        """
        Open a new connection with a Mongo database, using the default client settings.
        
        **Note:** This should be called from scripts only!

        Arguments
        - host: The host URL or IP of the Mongo database
        - port: The port of the Mongo database
        - username: The username of the Mongo database
        - password: The password of the Mongo database

        Returns
        - An MongoDatabase object representing an open connection to the database
        """
        ...


    def connectMongo(self, host: str, port: str, username: str, password: str, clientSettings: "MongoClientSettings") -> "MongoDatabase":
        """
        Open a new connection with a Mongo database, using the provided client settings.
        
        **Note:** This should be called from scripts only!

        Arguments
        - host: The host URL or IP of the Mongo database
        - port: The port of the Mongo database
        - username: The username of the Mongo database
        - password: The password of the Mongo database
        - clientSettings: A com.mongodb.MongoClientSettings object representing the client settings for the connection

        Returns
        - An MongoDatabase object representing an open connection to the database
        """
        ...


    def connectMongo(self, uri: str) -> "MongoDatabase":
        """
        Open a new connection with a Mongo database, using the provided connection string URI.
        
        **Note:** This should be called from scripts only!

        Arguments
        - uri: The connection string to define the connection, including options

        Returns
        - An MongoDatabase object representing an open connection to the database
        """
        ...


    def connectMongo(self, uri: str, clientSettings: "MongoClientSettings") -> "MongoDatabase":
        """
        Open a new connection with a Mongo database, using the provided connection string URI and client settings.
        
        **Note:** This should be called from scripts only!

        Arguments
        - uri: The connection string to define the connection, including options
        - clientSettings: A com.mongodb.MongoClientSettings object representing the client settings for the connection

        Returns
        - An MongoDatabase object representing an open connection to the database
        """
        ...


    def connectMongo(self, clientSettings: "MongoClientSettings") -> "MongoDatabase":
        """
        Open a new connection with a Mongo database, using the provided client settings.
        
        **Note:** This should be called from scripts only!

        Arguments
        - clientSettings: The client settings for the connection

        Returns
        - An MongoDatabase object representing an open connection to the database
        """
        ...


    def disconnect(self, connection: "Database") -> bool:
        """
        Disconnect from the provided database connection. Should be called when no longer using the database connection.
        
        **Note:** This should be called from scripts only!

        Arguments
        - connection: The database connection to disconnect from

        Returns
        - True if the disconnection was successful, False if otherwise
        """
        ...


    def disconnectAll(self, script: "Script") -> bool:
        """
        Disconnect from all database connections belonging to a certain script.

        Arguments
        - script: The script whose database connections should be disconnected

        Returns
        - True if all disconnections were successful, False if one or more connections were not closed successfully or if the script had no database connections to close
        """
        ...


    def getConnections(self, script: "Script") -> list["Database"]:
        """
        Get all database connnections belonging to a script.

        Arguments
        - script: The script to get database connections from

        Returns
        - An immutable List of Database containing all database connections associated with the script. Will return null if there are no open database connections associated with the script
        """
        ...


    def getConnections(self, script: "Script", type: "DatabaseType") -> list["Database"]:
        """
        Get all database connnections belonging to a script of the given type.

        Arguments
        - script: The script to get database connections from
        - type: The type of database connection to filter by

        Returns
        - An immutable List of Database containing all database connections of the given type associated with the script. Will return null if there are no open database connections of the given type associated with the script
        """
        ...


    @staticmethod
    def get() -> "DatabaseManager":
        """
        Get the singleton instance of this DatabaseManager.

        Returns
        - The instance
        """
        ...
