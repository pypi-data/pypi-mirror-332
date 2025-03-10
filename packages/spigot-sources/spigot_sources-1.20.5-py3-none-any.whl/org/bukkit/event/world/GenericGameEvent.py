"""
Python module generated from Java source file org.bukkit.event.world.GenericGameEvent

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from org.bukkit import GameEvent
from org.bukkit import Location
from org.bukkit.entity import Entity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.world import *
from typing import Any, Callable, Iterable, Tuple


class GenericGameEvent(WorldEvent, Cancellable):
    """
    Represents a generic Mojang game event.
    
    Specific Bukkit events should be used where possible, this event is mainly
    used internally by Sculk sensors.
    """

    def __init__(self, event: "GameEvent", location: "Location", entity: "Entity", radius: int, isAsync: bool):
        ...


    def getEvent(self) -> "GameEvent":
        """
        Get the underlying event.

        Returns
        - the event
        """
        ...


    def getLocation(self) -> "Location":
        """
        Get the location where the event occurred.

        Returns
        - event location
        """
        ...


    def getEntity(self) -> "Entity":
        """
        Get the entity which triggered this event, if present.

        Returns
        - triggering entity or null
        """
        ...


    def getRadius(self) -> int:
        """
        Get the block radius to which this event will be broadcast.

        Returns
        - broadcast radius
        """
        ...


    def setRadius(self, radius: int) -> None:
        """
        Set the radius to which the event should be broadcast.

        Arguments
        - radius: radius, must be greater than or equal to 0
        """
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def isCancelled(self) -> bool:
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
