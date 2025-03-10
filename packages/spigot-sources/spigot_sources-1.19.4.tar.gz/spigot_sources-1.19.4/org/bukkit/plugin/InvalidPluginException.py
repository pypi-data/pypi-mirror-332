"""
Python module generated from Java source file org.bukkit.plugin.InvalidPluginException

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.plugin import *
from typing import Any, Callable, Iterable, Tuple


class InvalidPluginException(Exception):
    """
    Thrown when attempting to load an invalid Plugin file
    """

    def __init__(self, cause: "Throwable"):
        """
        Constructs a new InvalidPluginException based on the given Exception

        Arguments
        - cause: Exception that triggered this Exception
        """
        ...


    def __init__(self):
        """
        Constructs a new InvalidPluginException
        """
        ...


    def __init__(self, message: str, cause: "Throwable"):
        """
        Constructs a new InvalidPluginException with the specified detail
        message and cause.

        Arguments
        - message: the detail message (which is saved for later retrieval
            by the getMessage() method).
        - cause: the cause (which is saved for later retrieval by the
            getCause() method). (A null value is permitted, and indicates that
            the cause is nonexistent or unknown.)
        """
        ...


    def __init__(self, message: str):
        """
        Constructs a new InvalidPluginException with the specified detail
        message

        Arguments
        - message: TThe detail message is saved for later retrieval by the
            getMessage() method.
        """
        ...
