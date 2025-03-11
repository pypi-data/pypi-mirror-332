"""
Python module generated from Java source file org.bukkit.event.EventException

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.event import *
from typing import Any, Callable, Iterable, Tuple


class EventException(Exception):

    def __init__(self, throwable: "Throwable"):
        """
        Constructs a new EventException based on the given Exception

        Arguments
        - throwable: Exception that triggered this Exception
        """
        ...


    def __init__(self):
        """
        Constructs a new EventException
        """
        ...


    def __init__(self, cause: "Throwable", message: str):
        """
        Constructs a new EventException with the given message

        Arguments
        - cause: The exception that caused this
        - message: The message
        """
        ...


    def __init__(self, message: str):
        """
        Constructs a new EventException with the given message

        Arguments
        - message: The message
        """
        ...


    def getCause(self) -> "Throwable":
        """
        If applicable, returns the Exception that triggered this Exception

        Returns
        - Inner exception, or null if one does not exist
        """
        ...
