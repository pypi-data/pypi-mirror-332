"""
Python module generated from Java source file org.bukkit.event.entity.EntityEvent

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Entity
from org.bukkit.entity import EntityType
from org.bukkit.event import Event
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class EntityEvent(Event):
    """
    Represents an Entity-related event
    """

    def __init__(self, what: "Entity"):
        ...


    def getEntity(self) -> "Entity":
        """
        Returns the Entity involved in this event

        Returns
        - Entity who is involved in this event
        """
        ...


    def getEntityType(self) -> "EntityType":
        """
        Gets the EntityType of the Entity involved in this event.

        Returns
        - EntityType of the Entity involved in this event
        """
        ...
