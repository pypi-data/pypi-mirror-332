"""
Python module generated from Java source file org.bukkit.event.hanging.HangingBreakEvent

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.entity import Hanging
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.hanging import *
from typing import Any, Callable, Iterable, Tuple


class HangingBreakEvent(HangingEvent, Cancellable):
    """
    Triggered when a hanging entity is removed
    """

    def __init__(self, hanging: "Hanging", cause: "HangingBreakEvent.RemoveCause"):
        ...


    def getCause(self) -> "HangingBreakEvent.RemoveCause":
        """
        Gets the cause for the hanging entity's removal

        Returns
        - the RemoveCause for the hanging entity's removal
        """
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...


    class RemoveCause(Enum):
        """
        An enum to specify the cause of the removal
        """

        ENTITY = 0
        """
        Removed by an entity
        """
        EXPLOSION = 1
        """
        Removed by an explosion
        """
        OBSTRUCTION = 2
        """
        Removed by placing a block on it
        """
        PHYSICS = 3
        """
        Removed by destroying the block behind it, etc
        """
        DEFAULT = 4
        """
        Removed by an uncategorised cause
        """
