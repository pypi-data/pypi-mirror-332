"""
Python module generated from Java source file org.bukkit.event.hanging.HangingEvent

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Hanging
from org.bukkit.event import Event
from org.bukkit.event.hanging import *
from typing import Any, Callable, Iterable, Tuple


class HangingEvent(Event):
    """
    Represents a hanging entity-related event.
    """

    def getEntity(self) -> "Hanging":
        """
        Gets the hanging entity involved in this event.

        Returns
        - the hanging entity
        """
        ...
