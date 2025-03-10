"""
Python module generated from Java source file org.bukkit.event.entity.EntityTransformEvent

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from java.util import Collections
from org.bukkit.entity import Entity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class EntityTransformEvent(EntityEvent, Cancellable):
    """
    Called when an entity is about to be replaced by another entity.
    """

    def __init__(self, original: "Entity", convertedList: list["Entity"], transformReason: "TransformReason"):
        ...


    def getTransformedEntity(self) -> "Entity":
        """
        Gets the entity that the original entity was transformed to.
        
        This returns the first entity in the transformed entity list.

        Returns
        - The transformed entity.

        See
        - .getTransformedEntities()
        """
        ...


    def getTransformedEntities(self) -> list["Entity"]:
        """
        Gets the entities that the original entity was transformed to.

        Returns
        - The transformed entities.
        """
        ...


    def getTransformReason(self) -> "TransformReason":
        """
        Gets the reason for the conversion that has occurred.

        Returns
        - The reason for conversion that has occurred.
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


    class TransformReason(Enum):

        CURED = 0
        """
        When a zombie gets cured and a villager is spawned.
        """
        FROZEN = 1
        """
        When an entity is shaking in Powder Snow and a new entity spawns.
        """
        INFECTION = 2
        """
        When a villager gets infected and a zombie villager spawns.
        """
        DROWNED = 3
        """
        When an entity drowns in water and a new entity spawns.
        """
        SHEARED = 4
        """
        When a mooshroom (or MUSHROOM_COW) is sheared and a cow spawns.
        """
        LIGHTNING = 5
        """
        When lightning strikes a entity.
        """
        SPLIT = 6
        """
        When a slime splits into multiple smaller slimes.
        """
        PIGLIN_ZOMBIFIED = 7
        """
        When a piglin converts to a zombified piglin.
        """
        METAMORPHOSIS = 8
        """
        When a tadpole converts to a frog
        """
        UNKNOWN = 9
        """
        When reason is unknown.
        """
