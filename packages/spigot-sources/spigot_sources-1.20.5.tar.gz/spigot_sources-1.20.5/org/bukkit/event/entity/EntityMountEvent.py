"""
Python module generated from Java source file org.bukkit.event.entity.EntityMountEvent

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Entity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class EntityMountEvent(EntityEvent, Cancellable):
    """
    Called when an entity attempts to ride another entity.
    """

    def __init__(self, what: "Entity", mount: "Entity"):
        ...


    def getMount(self) -> "Entity":
        """
        Gets the entity which will be ridden.

        Returns
        - mounted entity
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
