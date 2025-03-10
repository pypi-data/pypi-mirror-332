"""
Python module generated from Java source file org.bukkit.plugin.IllegalPluginAccessException

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.plugin import *
from typing import Any, Callable, Iterable, Tuple


class IllegalPluginAccessException(RuntimeException):
    """
    Thrown when a plugin attempts to interact with the server when it is not
    enabled
    """

    def __init__(self):
        """
        Creates a new instance of `IllegalPluginAccessException`
        without detail message.
        """
        ...


    def __init__(self, msg: str):
        """
        Constructs an instance of `IllegalPluginAccessException`
        with the specified detail message.

        Arguments
        - msg: the detail message.
        """
        ...
