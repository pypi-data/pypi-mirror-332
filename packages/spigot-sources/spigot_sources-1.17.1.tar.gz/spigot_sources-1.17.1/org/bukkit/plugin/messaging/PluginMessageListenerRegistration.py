"""
Python module generated from Java source file org.bukkit.plugin.messaging.PluginMessageListenerRegistration

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.plugin import Plugin
from org.bukkit.plugin.messaging import *
from typing import Any, Callable, Iterable, Tuple


class PluginMessageListenerRegistration:
    """
    Contains information about a Plugins registration to a plugin
    channel.
    """

    def __init__(self, messenger: "Messenger", plugin: "Plugin", channel: str, listener: "PluginMessageListener"):
        ...


    def getChannel(self) -> str:
        """
        Gets the plugin channel that this registration is about.

        Returns
        - Plugin channel.
        """
        ...


    def getListener(self) -> "PluginMessageListener":
        """
        Gets the registered listener described by this registration.

        Returns
        - Registered listener.
        """
        ...


    def getPlugin(self) -> "Plugin":
        """
        Gets the plugin that this registration is for.

        Returns
        - Registered plugin.
        """
        ...


    def isValid(self) -> bool:
        """
        Checks if this registration is still valid.

        Returns
        - True if this registration is still valid, otherwise False.
        """
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...
