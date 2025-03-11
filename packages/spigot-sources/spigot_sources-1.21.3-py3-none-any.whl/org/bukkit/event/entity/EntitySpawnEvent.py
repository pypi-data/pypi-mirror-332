"""
Python module generated from Java source file org.bukkit.event.entity.EntitySpawnEvent

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

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


class EntitySpawnEvent(EntityEvent, Cancellable):
    """
    Called when an entity is spawned into a world.
    
    If an Entity Spawn event is cancelled, the entity will not spawn.
    """

    def __init__(self, spawnee: "Entity"):
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getLocation(self) -> "Location":
        """
        Gets the location at which the entity is spawning.

        Returns
        - The location at which the entity is spawning
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
