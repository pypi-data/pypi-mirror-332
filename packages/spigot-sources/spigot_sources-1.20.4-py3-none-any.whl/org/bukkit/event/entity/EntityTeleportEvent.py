"""
Python module generated from Java source file org.bukkit.event.entity.EntityTeleportEvent

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Location
from org.bukkit.entity import Entity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class EntityTeleportEvent(EntityEvent, Cancellable):
    """
    Thrown when a non-player entity is teleported from one location to another.
    
    This may be as a result of natural causes (Enderman, Shulker), pathfinding
    (Wolf), or commands (/teleport).
    """

    def __init__(self, what: "Entity", from: "Location", to: "Location"):
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getFrom(self) -> "Location":
        """
        Gets the location that this entity moved from

        Returns
        - Location this entity moved from
        """
        ...


    def setFrom(self, from: "Location") -> None:
        """
        Sets the location that this entity moved from

        Arguments
        - from: New location this entity moved from
        """
        ...


    def getTo(self) -> "Location":
        """
        Gets the location that this entity moved to

        Returns
        - Location the entity moved to
        """
        ...


    def setTo(self, to: "Location") -> None:
        """
        Sets the location that this entity moved to

        Arguments
        - to: New Location this entity moved to
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
