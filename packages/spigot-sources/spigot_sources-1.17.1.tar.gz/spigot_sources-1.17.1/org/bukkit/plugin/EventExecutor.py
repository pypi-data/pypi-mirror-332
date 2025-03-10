"""
Python module generated from Java source file org.bukkit.plugin.EventExecutor

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.event import Event
from org.bukkit.event import EventException
from org.bukkit.event import Listener
from org.bukkit.plugin import *
from typing import Any, Callable, Iterable, Tuple


class EventExecutor:
    """
    Interface which defines the class for event call backs to plugins
    """

    def execute(self, listener: "Listener", event: "Event") -> None:
        ...
