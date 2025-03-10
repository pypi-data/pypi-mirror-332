"""
Python module generated from Java source file org.bukkit.plugin.messaging.MessageTooLargeException

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.plugin.messaging import *
from typing import Any, Callable, Iterable, Tuple


class MessageTooLargeException(RuntimeException):
    """
    Thrown if a Plugin Message is sent that is too large to be sent.
    """

    def __init__(self):
        ...


    def __init__(self, message: list[int]):
        ...


    def __init__(self, length: int):
        ...


    def __init__(self, msg: str):
        ...
