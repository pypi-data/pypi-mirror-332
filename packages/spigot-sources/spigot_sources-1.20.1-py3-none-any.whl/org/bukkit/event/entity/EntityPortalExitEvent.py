"""
Python module generated from Java source file org.bukkit.event.entity.EntityPortalExitEvent

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Location
from org.bukkit.entity import Entity
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from org.bukkit.util import Vector
from typing import Any, Callable, Iterable, Tuple


class EntityPortalExitEvent(EntityTeleportEvent):
    """
    Called before an entity exits a portal.
    
    This event allows you to modify the velocity of the entity after they have
    successfully exited the portal.
    """

    def __init__(self, entity: "Entity", from: "Location", to: "Location", before: "Vector", after: "Vector"):
        ...


    def getBefore(self) -> "Vector":
        """
        Gets a copy of the velocity that the entity has before entering the
        portal.

        Returns
        - velocity of entity before entering the portal
        """
        ...


    def getAfter(self) -> "Vector":
        """
        Gets a copy of the velocity that the entity will have after exiting the
        portal.

        Returns
        - velocity of entity after exiting the portal
        """
        ...


    def setAfter(self, after: "Vector") -> None:
        """
        Sets the velocity that the entity will have after exiting the portal.

        Arguments
        - after: the velocity after exiting the portal
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
