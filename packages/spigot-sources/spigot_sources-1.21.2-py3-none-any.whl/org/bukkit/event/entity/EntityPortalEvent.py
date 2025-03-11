"""
Python module generated from Java source file org.bukkit.event.entity.EntityPortalEvent

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

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


    def __init__(self, entity: "Entity", from: "Location", to: "Location", searchRadius: int, canCreatePortal: bool, creationRadius: int):
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


    def getCanCreatePortal(self) -> bool:
        """
        Returns whether the server will attempt to create a destination portal or
        not.

        Returns
        - whether there should create be a destination portal created
        """
        ...


    def setCanCreatePortal(self, canCreatePortal: bool) -> None:
        """
        Sets whether the server should attempt to create a destination portal or
        not.

        Arguments
        - canCreatePortal: Sets whether there should be a destination portal
        created
        """
        ...


    def setCreationRadius(self, creationRadius: int) -> None:
        """
        Sets the maximum radius the world is searched for a free space from the
        given location.
        
        If enough free space is found then the portal will be created there, if
        not it will force create with air-space at the target location.
        
        Does not apply to end portal target platforms which will always appear at
        the target location.

        Arguments
        - creationRadius: the radius in which to create a portal from the
        location
        """
        ...


    def getCreationRadius(self) -> int:
        """
        Gets the maximum radius the world is searched for a free space from the
        given location.
        
        If enough free space is found then the portal will be created there, if
        not it will force create with air-space at the target location.
        
        Does not apply to end portal target platforms which will always appear at
        the target location.

        Returns
        - the currently set creation radius
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
