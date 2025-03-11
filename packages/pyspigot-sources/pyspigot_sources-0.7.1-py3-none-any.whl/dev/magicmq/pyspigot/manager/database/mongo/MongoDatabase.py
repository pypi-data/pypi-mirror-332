"""
Python module generated from Java source file dev.magicmq.pyspigot.manager.database.mongo.MongoDatabase

Java source file obtained from artifact pyspigot version 0.7.1

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.mongodb import BasicDBObject
from com.mongodb import MongoClientSettings
from com.mongodb.client import *
from com.mongodb.client.model import FindOneAndUpdateOptions
from com.mongodb.client.model import ReturnDocument
from com.mongodb.client.model import UpdateOptions
from com.mongodb.client.result import DeleteResult
from com.mongodb.client.result import InsertManyResult
from com.mongodb.client.result import InsertOneResult
from com.mongodb.client.result import UpdateResult
from dev.magicmq.pyspigot.manager.database import Database
from dev.magicmq.pyspigot.manager.database.mongo import *
from dev.magicmq.pyspigot.manager.script import Script
from java.util import Collections
from org.bson import Document
from org.bson.conversions import Bson
from typing import Any, Callable, Iterable, Tuple


class MongoDatabase(Database):
    """
    Represents an open connection to a Mongo Database.
    
    **Note:** Most methods in this class should be called from scripts only!
    """

    def __init__(self, script: "Script", clientSettings: "MongoClientSettings"):
        """
        Arguments
        - script: The script associated with this MongoDatabase
        - clientSettings: The client settings for the MongoDatabase connection
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


    def getMongoClient(self) -> "MongoClient":
        """
        Get the com.mongodb.client.MongoClient associated with this Mongo Database connection.

        Returns
        - The MongoClient
        """
        ...


    def fetchNewUpdateOptions(self) -> "UpdateOptions":
        """
        Fetch a new com.mongodb.client.model.UpdateOptions object for updates
        """
        ...


    def fetchNewFindOneAndUpdateOptions(self) -> "FindOneAndUpdateOptions":
        """
        Fetch a new com.mongodb.client.model.FindOneAndUpdateOptions object for updates
        """
        ...


    def createObject(self) -> "BasicDBObject":
        """
        Create a new empty com.mongodb.BasicDBObject.

        Returns
        - The BasicDBObject
        """
        ...


    def createObject(self, json: str) -> "BasicDBObject":
        """
        Create a new com.mongodb.BasicDBObject out of the provided json.

        Returns
        - The BasicDBObject
        """
        ...


    def createObject(self, key: str, value: "Object") -> "BasicDBObject":
        """
        Create a new com.mongodb.BasicDBObject with the provided key and value.

        Returns
        - The BasicDBObject
        """
        ...


    def createDocument(self) -> "Document":
        """
        Create an empty org.bson.Document.

        Returns
        - The document
        """
        ...


    def createDocument(self, json: str) -> "Document":
        """
        Create a org.bson.Document out of the provided json.

        Arguments
        - json: A JSON representation of the document

        Returns
        - The document
        """
        ...


    def createDocument(self, key: str, value: "Object") -> "Document":
        """
        Create a org.bson.Document with the provided key and value.

        Arguments
        - key: The key
        - value: The value

        Returns
        - The document
        """
        ...


    def getDatabase(self, database: str) -> "com.mongodb.client.MongoDatabase":
        """
        Get a com.mongodb.client.MongoDatabase with the given name.

        Arguments
        - database: The name of the database

        Returns
        - The database
        """
        ...


    def getDatabaseNames(self) -> "MongoIterable"[str]:
        """
        Get all database names.

        Returns
        - An iterable list of type com.mongodb.client.MongoIterable<String> containing all database names
        """
        ...


    def getDatabases(self) -> "MongoIterable"["Document"]:
        """
        Get all databases.

        Returns
        - An iterable list of type com.mongodb.client.MongoIterable<Document> containing all databases
        """
        ...


    def doesDatabaseExist(self, database: str) -> bool:
        """
        Check if a database exists with the given name.

        Arguments
        - database: The name of the database to check

        Returns
        - True if the database exists, False if otherwise
        """
        ...


    def createCollection(self, database: str, collection: str) -> bool:
        """
        Create a collection in the given database

        Arguments
        - database: The name of the database where the collection should be created
        - collection: The name for the collection

        Returns
        - True if the collection was created, False if it already exists in the database
        """
        ...


    def deleteCollection(self, database: str, collection: str) -> bool:
        """
        Delete a collection in the given database

        Arguments
        - database: The name of the database where the collection should be deleted
        - collection: The name of the collection

        Returns
        - True if the collection was deleted, False if it did not exist in the database
        """
        ...


    def getCollection(self, database: str, collection: str) -> "MongoCollection"["Document"]:
        """
        Get a collection from a database.

        Arguments
        - database: The name of the database to fetch from
        - collection: The name of the collection to get

        Returns
        - A com.mongodb.client.MongoCollection<Document> containing org.bson.Document representing the collection
        """
        ...


    def getCollectionNames(self, database: str) -> "ListCollectionNamesIterable":
        """
        Get all collection names within a database.

        Arguments
        - database: The database to get collections names from

        Returns
        - An iterable list of type com.mongodb.client.ListCollectionNamesIterable containing all collection names
        """
        ...


    def getCollections(self, database: str) -> "ListCollectionsIterable"["Document"]:
        """
        Get all collections within a database.

        Arguments
        - database: The database to get collections from

        Returns
        - An iterable list of type com.mongodb.client.ListCollectionsIterable<Document> containing all collections
        """
        ...


    def doesCollectionExist(self, database: str, collection: str) -> bool:
        """
        Check if a collection exists within a database.

        Arguments
        - database: The name of the database to check
        - collection: The name of the collection to check

        Returns
        - True if the collection exists, False if otherwise
        """
        ...


    def createCollectionIndex(self, database: str, collection: str, keys: "Bson") -> str:
        """
        Create a collection with an index of the given keys.

        Arguments
        - database: The name of the database where the collection should be created
        - collection: The name for the collection
        - keys: A org.bson.conversions.Bson object representing the index keys

        Returns
        - 
        """
        ...


    def getDocument(self, database: str, collection: str, filter: "Bson") -> "Document":
        """
        Get a document within a collection that match the given filter.

        Arguments
        - database: The name of the database to fetch from
        - collection: The name of the collection to fetch from
        - filter: A org.bson.conversions.Bson object representing a filter to filter documents within the collection

        Returns
        - The first document within the collection that matched the provided filter
        """
        ...


    def getDocument(self, database: str, collection: str, filter: "Bson", projections: "Bson", sorts: "Bson") -> "Document":
        """
        Get a document within a collection that match the given filter, projections, and sort criteria.

        Arguments
        - database: The name of the database to fetch from
        - collection: The name of the collection to fetch from
        - filter: A org.bson.conversions.Bson object representing a filter to filter documents within the collection
        - projections: The project document
        - sorts: Sort criteria

        Returns
        - The first document within the collection that matched the provided filter, projections, and sort criteria
        """
        ...


    def getDocuments(self, database: str, collection: str) -> "FindIterable"["Document"]:
        """
        Get all documents within a collection.

        Arguments
        - database: The name of the database to fetch from
        - collection: The name of the collection to fetch from

        Returns
        - An iterable list of type com.mongodb.client.FindIterable<Document> containing all documents within the collection
        """
        ...


    def getDocuments(self, database: str, collection: str, filter: "Bson") -> "FindIterable"["Document"]:
        """
        Get all documents within a collection that match the given filter.

        Arguments
        - database: The name of the database to fetch from
        - collection: The name of the collection to fetch from
        - filter: A org.bson.conversions.Bson object representing a filter to filter documents within the collection

        Returns
        - An iterable list of type com.mongodb.client.FindIterable<Document> containing all documents within the collection that matched the provided filter
        """
        ...


    def insertDocument(self, database: str, collection: str, document: "Document") -> "InsertOneResult":
        """
        Insert a document into a collection.

        Arguments
        - database: The database that contains the collection
        - collection: The collection to insert into
        - document: The document to insert

        Returns
        - An com.mongodb.client.result.InsertOneResult representing the outcome of the operation
        """
        ...


    def insertDocuments(self, database: str, collection: str, documents: list["Document"]) -> "InsertManyResult":
        """
        Insert multiple documents into a collection.

        Arguments
        - database: The database that contains the collection
        - collection: The collection to insert into
        - documents: The documents to insert

        Returns
        - An com.mongodb.client.result.InsertManyResult representing the outcome of the operation
        """
        ...


    def updateDocument(self, database: str, collection: str, filter: "Bson", update: "Bson") -> "UpdateResult":
        """
        Update one or more documents within a collection that match the given filter, with the default update options

        Arguments
        - database: The database that contains the collection
        - collection: The collection containing the document
        - filter: A org.bson.conversions.Bson object representing a filter to filter documents within the collection
        - update: The update that should be applied to the first matching document

        Returns
        - An com.mongodb.client.result.UpdateResult representing the outcome of the operation
        """
        ...


    def updateDocument(self, database: str, collection: str, filter: "Bson", update: "Bson", updateOptions: "UpdateOptions") -> "UpdateResult":
        """
        Update one or more documents within a collection that match the given filter, with the provided update options

        Arguments
        - database: The database that contains the collection
        - collection: The collection containing the document
        - filter: A org.bson.conversions.Bson object representing a filter to filter documents within the collection
        - update: The update that that should be applied to the first matching document
        - updateOptions: A com.mongodb.client.model.UpdateOptions object representing the options to apply to the update operation

        Returns
        - An com.mongodb.client.result.UpdateResult representing the outcome of the operation
        """
        ...


    def updateDocument(self, database: str, collection: str, filter: "Bson", updates: list["Bson"]) -> "UpdateResult":
        """
        Update one or more documents within a collection that match the given filter, with the default update options

        Arguments
        - database: The database that contains the collection
        - collection: The collection containing the document
        - filter: A org.bson.conversions.Bson object representing a filter to filter documents within the collection
        - updates: The updates that should be applied to the first matching document

        Returns
        - An com.mongodb.client.result.UpdateResult representing the outcome of the operation
        """
        ...


    def updateDocument(self, database: str, collection: str, filter: "Bson", updates: list["Bson"], updateOptions: "UpdateOptions") -> "UpdateResult":
        """
        Update one or more documents within a collection that match the given filter, with the provided update options

        Arguments
        - database: The database that contains the collection
        - collection: The collection containing the document
        - filter: A org.bson.conversions.Bson object representing a filter to filter documents within the collection
        - updates: The updates that should be applied to the first matching document
        - updateOptions: A com.mongodb.client.model.UpdateOptions object representing the options to apply to the update operation

        Returns
        - An com.mongodb.client.result.UpdateResult representing the outcome of the operation
        """
        ...


    def findAndUpdateDocument(self, database: str, collection: str, filter: "Bson", update: "Bson") -> "Document":
        """
        Update and return a document within a collection that match the given filter, with the default update options

        Arguments
        - database: The database that contains the collection
        - collection: The collection containing the document
        - filter: A org.bson.conversions.Bson object representing a filter to filter documents within the collection
        - update: The update that should be applied to the first matching document

        Returns
        - An com.mongodb.client.result.UpdateResult representing the outcome of the operation
        """
        ...


    def findAndUpdateDocument(self, database: str, collection: str, filter: "Bson", update: "Bson", updateOptions: "FindOneAndUpdateOptions") -> "Document":
        """
        Update and return a document within a collection that match the given filter, with the default update options

        Arguments
        - database: The database that contains the collection
        - collection: The collection containing the document
        - filter: A org.bson.conversions.Bson object representing a filter to filter documents within the collection
        - update: The update that should be applied to the first matching document
        - updateOptions: A com.mongodb.client.model.FindOneAndUpdateOptions object representing the options to apply to the update operation

        Returns
        - The document that was updated
        """
        ...


    def findAndUpdateDocument(self, database: str, collection: str, filter: "Bson", update: list["Bson"]) -> "Document":
        """
        Update and return a document within a collection that match the given filter, with the default update options

        Arguments
        - database: The database that contains the collection
        - collection: The collection containing the document
        - filter: A org.bson.conversions.Bson object representing a filter to filter documents within the collection
        - update: The updates that should be applied to the first matching document

        Returns
        - The document that was updated
        """
        ...


    def findAndUpdateDocument(self, database: str, collection: str, filter: "Bson", update: list["Bson"], updateOptions: "FindOneAndUpdateOptions") -> "Document":
        """
        Update and return a document within a collection that match the given filter, with the default update options

        Arguments
        - database: The database that contains the collection
        - collection: The collection containing the document
        - filter: A org.bson.conversions.Bson object representing a filter to filter documents within the collection
        - update: The updates that should be applied to the first matching document
        - updateOptions: A com.mongodb.client.model.FindOneAndUpdateOptions object representing the options to apply to the update operation

        Returns
        - The document that was updated
        """
        ...


    def updateDocuments(self, database: str, collection: str, filter: "Bson", update: "Bson") -> "UpdateResult":
        """
        Update multiple documents within a collection.

        Arguments
        - database: The database that contains the collection
        - collection: The collection whose documents should be updated
        - filter: A org.bson.conversions.Bson object representing a filter to filter documents within the collection
        - update: The update that should be applied to all matching documents

        Returns
        - An com.mongodb.client.result.UpdateResult representing the outcome of the operation
        """
        ...


    def updateDocuments(self, database: str, collection: str, filter: "Bson", update: "Bson", updateOptions: "UpdateOptions") -> "UpdateResult":
        """
        Update multiple documents within a collection.

        Arguments
        - database: The database that contains the collection
        - collection: The collection whose documents should be updated
        - filter: A org.bson.conversions.Bson object representing a filter to filter documents within the collection
        - update: The update that should be applied to all matching documents
        - updateOptions: A com.mongodb.client.model.UpdateOptions object representing the options to apply to the update operation

        Returns
        - An com.mongodb.client.result.UpdateResult representing the outcome of the operation
        """
        ...


    def updateDocuments(self, database: str, collection: str, filter: "Bson", update: list["Bson"]) -> "UpdateResult":
        """
        Update multiple documents within a collection.

        Arguments
        - database: The database that contains the collection
        - collection: The collection whose documents should be updated
        - filter: A org.bson.conversions.Bson object representing a filter to filter documents within the collection
        - update: The updates that should be applied to all matching documents

        Returns
        - An com.mongodb.client.result.UpdateResult representing the outcome of the operation
        """
        ...


    def updateDocuments(self, database: str, collection: str, filter: "Bson", update: list["Bson"], updateOptions: "UpdateOptions") -> "UpdateResult":
        """
        Update multiple documents within a collection.

        Arguments
        - database: The database that contains the collection
        - collection: The collection whose documents should be updated
        - filter: A org.bson.conversions.Bson object representing a filter to filter documents within the collection
        - update: The updates that should be applied to all matching documents
        - updateOptions: A com.mongodb.client.model.UpdateOptions object representing the options to apply to the update operation

        Returns
        - An com.mongodb.client.result.UpdateResult representing the outcome of the operation
        """
        ...


    def deleteDocument(self, database: str, collection: str, filter: "Bson") -> "DeleteResult":
        """
        Delete a document from a collection matching the provided filter.

        Arguments
        - database: The database that contains the collection
        - collection: The collection that contains the document
        - filter: A org.bson.conversions.Bson object representing a filter to filter documents within the collection

        Returns
        - An com.mongodb.client.result.DeleteResult representing the outcome of the operation
        """
        ...


    def deleteDocuments(self, database: str, collection: str, filter: "Bson") -> "DeleteResult":
        """
        Delete multiple documents from a collection matching the provided filter.

        Arguments
        - database: The database that contains the collection
        - collection: The collection that contains the documents
        - filter: A org.bson.conversions.Bson object representing a filter to filter documents within the collection

        Returns
        - An com.mongodb.client.result.DeleteResult representing the outcome of the operation
        """
        ...


    def toString(self) -> str:
        """
        Prints a representation of this MongoDatabase in string format, including the URI and com.mongodb.client.MongoClient

        Returns
        - A string representation of the MongoDatabase
        """
        ...
