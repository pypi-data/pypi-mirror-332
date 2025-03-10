"""
Python module generated from Java source file org.bukkit.event.server.PluginEvent

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.event.server import *
from org.bukkit.plugin import Plugin
from typing import Any, Callable, Iterable, Tuple


class PluginEvent(ServerEvent):
    """
    Used for plugin enable and disable events
    """

    def __init__(self, plugin: "Plugin"):
        ...


    def getPlugin(self) -> "Plugin":
        """
        Gets the plugin involved in this event

        Returns
        - Plugin for this event
        """
        ...
