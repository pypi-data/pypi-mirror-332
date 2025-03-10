"""
Python module generated from Java source file org.bukkit.plugin.messaging.ChannelNotRegisteredException

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.plugin.messaging import *
from typing import Any, Callable, Iterable, Tuple


class ChannelNotRegisteredException(RuntimeException):
    """
    Thrown if a Plugin attempts to send a message on an unregistered channel.
    """

    def __init__(self):
        ...


    def __init__(self, channel: str):
        ...
