"""
Python module generated from Java source file org.bukkit.event.entity.EntityDropItemEvent

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Entity
from org.bukkit.entity import Item
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class EntityDropItemEvent(EntityEvent, Cancellable):
    """
    Thrown when an entity creates an item drop.
    """

    def __init__(self, entity: "Entity", drop: "Item"):
        ...


    def getItemDrop(self) -> "Item":
        """
        Gets the Item created by the entity

        Returns
        - Item created by the entity
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
