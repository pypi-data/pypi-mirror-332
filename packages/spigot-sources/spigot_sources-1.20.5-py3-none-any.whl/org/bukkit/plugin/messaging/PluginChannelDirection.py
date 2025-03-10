"""
Python module generated from Java source file org.bukkit.plugin.messaging.PluginChannelDirection

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.plugin.messaging import *
from typing import Any, Callable, Iterable, Tuple


class PluginChannelDirection(Enum):
    """
    Represents the different directions a plugin channel may go.
    """

    INCOMING = 0
    """
    The plugin channel is being sent to the server from a client.
    """
    OUTGOING = 1
    """
    The plugin channel is being sent to a client from the server.
    """
