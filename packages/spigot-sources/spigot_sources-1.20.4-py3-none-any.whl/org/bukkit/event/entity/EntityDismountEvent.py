"""
Python module generated from Java source file org.bukkit.event.entity.EntityDismountEvent

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Entity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class EntityDismountEvent(EntityEvent, Cancellable):
    """
    Called when an entity stops riding another entity.
    """

    def __init__(self, what: "Entity", dismounted: "Entity"):
        ...


    def getDismounted(self) -> "Entity":
        """
        Gets the entity which will no longer be ridden.

        Returns
        - dismounted entity
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
