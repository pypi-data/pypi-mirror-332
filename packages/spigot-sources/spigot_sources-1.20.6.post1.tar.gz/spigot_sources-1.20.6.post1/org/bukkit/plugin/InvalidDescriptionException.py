"""
Python module generated from Java source file org.bukkit.plugin.InvalidDescriptionException

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.plugin import *
from typing import Any, Callable, Iterable, Tuple


class InvalidDescriptionException(Exception):
    """
    Thrown when attempting to load an invalid PluginDescriptionFile
    """

    def __init__(self, cause: "Throwable", message: str):
        """
        Constructs a new InvalidDescriptionException based on the given
        Exception

        Arguments
        - message: Brief message explaining the cause of the exception
        - cause: Exception that triggered this Exception
        """
        ...


    def __init__(self, cause: "Throwable"):
        """
        Constructs a new InvalidDescriptionException based on the given
        Exception

        Arguments
        - cause: Exception that triggered this Exception
        """
        ...


    def __init__(self, message: str):
        """
        Constructs a new InvalidDescriptionException with the given message

        Arguments
        - message: Brief message explaining the cause of the exception
        """
        ...


    def __init__(self):
        """
        Constructs a new InvalidDescriptionException
        """
        ...
