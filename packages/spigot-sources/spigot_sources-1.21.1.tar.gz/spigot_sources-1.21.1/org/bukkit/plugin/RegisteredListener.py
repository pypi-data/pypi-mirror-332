"""
Python module generated from Java source file org.bukkit.plugin.RegisteredListener

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.event import Cancellable
from org.bukkit.event import Event
from org.bukkit.event import EventException
from org.bukkit.event import EventPriority
from org.bukkit.event import Listener
from org.bukkit.plugin import *
from typing import Any, Callable, Iterable, Tuple


class RegisteredListener:
    """
    Stores relevant information for plugin listeners
    """

    def __init__(self, listener: "Listener", executor: "EventExecutor", priority: "EventPriority", plugin: "Plugin", ignoreCancelled: bool):
        ...


    def getListener(self) -> "Listener":
        """
        Gets the listener for this registration

        Returns
        - Registered Listener
        """
        ...


    def getPlugin(self) -> "Plugin":
        """
        Gets the plugin for this registration

        Returns
        - Registered Plugin
        """
        ...


    def getPriority(self) -> "EventPriority":
        """
        Gets the priority for this registration

        Returns
        - Registered Priority
        """
        ...


    def callEvent(self, event: "Event") -> None:
        """
        Calls the event executor

        Arguments
        - event: The event

        Raises
        - EventException: If an event handler throws an exception.
        """
        ...


    def isIgnoringCancelled(self) -> bool:
        """
        Whether this listener accepts cancelled events

        Returns
        - True when ignoring cancelled events
        """
        ...
