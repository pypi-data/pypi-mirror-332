"""
Python module generated from Java source file org.bukkit.configuration.InvalidConfigurationException

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.configuration import *
from typing import Any, Callable, Iterable, Tuple


class InvalidConfigurationException(Exception):
    """
    Exception thrown when attempting to load an invalid Configuration
    """

    def __init__(self):
        """
        Creates a new instance of InvalidConfigurationException without a
        message or cause.
        """
        ...


    def __init__(self, msg: str):
        """
        Constructs an instance of InvalidConfigurationException with the
        specified message.

        Arguments
        - msg: The details of the exception.
        """
        ...


    def __init__(self, cause: "Throwable"):
        """
        Constructs an instance of InvalidConfigurationException with the
        specified cause.

        Arguments
        - cause: The cause of the exception.
        """
        ...


    def __init__(self, msg: str, cause: "Throwable"):
        """
        Constructs an instance of InvalidConfigurationException with the
        specified message and cause.

        Arguments
        - cause: The cause of the exception.
        - msg: The details of the exception.
        """
        ...
