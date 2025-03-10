"""
Python module generated from Java source file org.bukkit.command.CommandException

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.command import *
from typing import Any, Callable, Iterable, Tuple


class CommandException(RuntimeException):
    """
    Thrown when an unhandled exception occurs during the execution of a Command
    """

    def __init__(self):
        """
        Creates a new instance of `CommandException` without detail
        message.
        """
        ...


    def __init__(self, msg: str):
        """
        Constructs an instance of `CommandException` with the
        specified detail message.

        Arguments
        - msg: the detail message.
        """
        ...


    def __init__(self, msg: str, cause: "Throwable"):
        ...
