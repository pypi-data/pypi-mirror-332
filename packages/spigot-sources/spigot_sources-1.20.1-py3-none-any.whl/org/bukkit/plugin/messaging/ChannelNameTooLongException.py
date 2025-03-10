"""
Python module generated from Java source file org.bukkit.plugin.messaging.ChannelNameTooLongException

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.plugin.messaging import *
from typing import Any, Callable, Iterable, Tuple


class ChannelNameTooLongException(RuntimeException):
    """
    Thrown if a Plugin Channel is too long.
    """

    def __init__(self):
        ...


    def __init__(self, channel: str):
        ...
