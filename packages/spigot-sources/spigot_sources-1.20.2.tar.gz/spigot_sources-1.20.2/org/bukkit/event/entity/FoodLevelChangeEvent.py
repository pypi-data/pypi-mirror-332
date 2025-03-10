"""
Python module generated from Java source file org.bukkit.event.entity.FoodLevelChangeEvent

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import HumanEntity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class FoodLevelChangeEvent(EntityEvent, Cancellable):
    """
    Called when a human entity's food level changes
    """

    def __init__(self, what: "HumanEntity", level: int):
        ...


    def __init__(self, what: "HumanEntity", level: int, item: "ItemStack"):
        ...


    def getEntity(self) -> "HumanEntity":
        ...


    def getItem(self) -> "ItemStack":
        """
        Gets the item that triggered this event, if any.

        Returns
        - an ItemStack for the item being consumed
        """
        ...


    def getFoodLevel(self) -> int:
        """
        Gets the resultant food level that the entity involved in this event
        should be set to.
        
        Where 20 is a full food bar and 0 is an empty one.

        Returns
        - The resultant food level
        """
        ...


    def setFoodLevel(self, level: int) -> None:
        """
        Sets the resultant food level that the entity involved in this event
        should be set to

        Arguments
        - level: the resultant food level that the entity involved in this
            event should be set to
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
