"""
Python module generated from Java source file org.bukkit.plugin.UnknownDependencyException

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.plugin import *
from typing import Any, Callable, Iterable, Tuple


class UnknownDependencyException(RuntimeException):
    """
    Thrown when attempting to load an invalid Plugin file
    """

    def __init__(self, throwable: "Throwable"):
        """
        Constructs a new UnknownDependencyException based on the given
        Exception

        Arguments
        - throwable: Exception that triggered this Exception
        """
        ...


    def __init__(self, message: str):
        """
        Constructs a new UnknownDependencyException with the given message

        Arguments
        - message: Brief message explaining the cause of the exception
        """
        ...


    def __init__(self, throwable: "Throwable", message: str):
        """
        Constructs a new UnknownDependencyException based on the given
        Exception

        Arguments
        - message: Brief message explaining the cause of the exception
        - throwable: Exception that triggered this Exception
        """
        ...


    def __init__(self):
        """
        Constructs a new UnknownDependencyException
        """
        ...
