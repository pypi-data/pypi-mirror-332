"""
Python module generated from Java source file dev.magicmq.pyspigot.manager.script.GlobalVariables

Java source file obtained from artifact pyspigot version 0.7.1

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from dev.magicmq.pyspigot.manager.script import *
from typing import Any, Callable, Iterable, Tuple


class GlobalVariables:
    """
    A wrapper class for a HashMap that contains global variables that can be shared across scripts.

    See
    - java.util.HashMap
    """

    def set(self, key: str, value: "Object") -> "Object":
        """
        Set a global variable. Will override an existing global variable with the same name.

        Arguments
        - key: The name of the variable to set
        - value: The value of the variable

        Returns
        - The value that was previously associated with the given key, or null if there was none
        """
        ...


    def set(self, key: str, value: "Object", override: bool) -> "Object":
        """
        Set a global variable, with the option to override an existing global variable with the same name.

        Arguments
        - key: The name of the variable to set
        - value: The value of the variable
        - override: Whether an existing value should be overridden

        Returns
        - If override is True, will return the value that was previously associated with the key, or null if there was none. If override is False, will return the existing value, or null if there was none
        """
        ...


    def remove(self, key: str) -> "Object":
        """
        Remove/delete a global variable.

        Arguments
        - key: The name of the variable to remove

        Returns
        - The value of the variable that was removed, or null if there was none
        """
        ...


    def get(self, key: str) -> "Object":
        """
        Get a global variable

        Arguments
        - key: The name of the variable to get

        Returns
        - The variable, or null if there is no variable associated with the given key
        """
        ...


    def getKeys(self) -> set[str]:
        """
        Get a set of all global variable names.

        Returns
        - An immutable java.util.Set containing the names of all global variables. Will return an empty set if there are no global variables
        """
        ...


    def getValues(self) -> Iterable["Object"]:
        """
        Get a set of all global variable values.

        Returns
        - An immutable java.util.Collection containing the values of all global variables. Will return an empty collection if there are no global variables
        """
        ...


    def getHashMap(self) -> dict[str, "Object"]:
        """
        Get the underlying java.util.HashMap wherein global variables are cached.

        Returns
        - The underlying HashMap, which is mutable
        """
        ...


    def contains(self, key: str) -> bool:
        """
        Check if a global variable exists with the given name.

        Arguments
        - key: The name to check

        Returns
        - True if there is a global variable with the given name, False if there is not
        """
        ...


    def containsValue(self, value: "Object") -> bool:
        """
        Check if a global variable exists with the given value.

        Arguments
        - value: The value to check

        Returns
        - True if there is a global variable with the given value, False if there is not
        """
        ...


    def purge(self) -> None:
        """
        Clear all global variables.
        """
        ...


    @staticmethod
    def get() -> "GlobalVariables":
        ...
