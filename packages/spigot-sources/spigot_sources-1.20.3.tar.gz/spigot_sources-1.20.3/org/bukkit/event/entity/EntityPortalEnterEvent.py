"""
Python module generated from Java source file org.bukkit.event.entity.EntityPortalEnterEvent

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Location
from org.bukkit.entity import Entity
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class EntityPortalEnterEvent(EntityEvent):
    """
    Called when an entity comes into contact with a portal
    """

    def __init__(self, entity: "Entity", location: "Location"):
        ...


    def getLocation(self) -> "Location":
        """
        Gets the portal block the entity is touching

        Returns
        - The portal block the entity is touching
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
