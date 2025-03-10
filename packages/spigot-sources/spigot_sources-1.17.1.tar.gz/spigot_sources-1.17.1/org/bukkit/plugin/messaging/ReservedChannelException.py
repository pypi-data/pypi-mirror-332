"""
Python module generated from Java source file org.bukkit.plugin.messaging.ReservedChannelException

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.plugin.messaging import *
from typing import Any, Callable, Iterable, Tuple


class ReservedChannelException(RuntimeException):
    """
    Thrown if a plugin attempts to register for a reserved channel (such as
    "REGISTER")
    """

    def __init__(self):
        ...


    def __init__(self, name: str):
        ...
