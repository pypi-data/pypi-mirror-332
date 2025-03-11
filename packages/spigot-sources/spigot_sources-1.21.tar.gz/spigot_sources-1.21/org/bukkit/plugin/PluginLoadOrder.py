"""
Python module generated from Java source file org.bukkit.plugin.PluginLoadOrder

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.plugin import *
from typing import Any, Callable, Iterable, Tuple


class PluginLoadOrder(Enum):
    """
    Represents the order in which a plugin should be initialized and enabled
    """

    STARTUP = 0
    """
    Indicates that the plugin will be loaded at startup
    """
    POSTWORLD = 1
    """
    Indicates that the plugin will be loaded after the first/default world
    was created
    """
