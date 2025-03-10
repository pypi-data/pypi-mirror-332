"""
Python module generated from Java source file org.bukkit.event.entity.EntityPortalEvent

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Location
from org.bukkit.entity import Entity
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class EntityPortalEvent(EntityTeleportEvent):
    """
    Called when a non-player entity is about to teleport because it is in
    contact with a portal.
    
    For players see org.bukkit.event.player.PlayerPortalEvent
    """

    def __init__(self, entity: "Entity", from: "Location", to: "Location"):
        ...


    def __init__(self, entity: "Entity", from: "Location", to: "Location", searchRadius: int):
        ...


    def setSearchRadius(self, searchRadius: int) -> None:
        """
        Set the Block radius to search in for available portals.

        Arguments
        - searchRadius: the radius in which to search for a portal from the
        location
        """
        ...


    def getSearchRadius(self) -> int:
        """
        Gets the search radius value for finding an available portal.

        Returns
        - the currently set search radius
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
