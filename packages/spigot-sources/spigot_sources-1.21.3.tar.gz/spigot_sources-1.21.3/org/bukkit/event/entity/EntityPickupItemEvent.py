"""
Python module generated from Java source file org.bukkit.event.entity.EntityPickupItemEvent

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Item
from org.bukkit.entity import LivingEntity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class EntityPickupItemEvent(EntityEvent, Cancellable):
    """
    Thrown when a entity picks an item up from the ground
    """

    def __init__(self, entity: "LivingEntity", item: "Item", remaining: int):
        ...


    def getEntity(self) -> "LivingEntity":
        ...


    def getItem(self) -> "Item":
        """
        Gets the Item picked up by the entity.

        Returns
        - Item
        """
        ...


    def getRemaining(self) -> int:
        """
        Gets the amount remaining on the ground, if any

        Returns
        - amount remaining on the ground
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
