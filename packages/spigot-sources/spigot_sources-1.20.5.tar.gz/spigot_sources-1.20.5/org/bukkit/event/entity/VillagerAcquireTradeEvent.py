"""
Python module generated from Java source file org.bukkit.event.entity.VillagerAcquireTradeEvent

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import AbstractVillager
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from org.bukkit.inventory import MerchantRecipe
from typing import Any, Callable, Iterable, Tuple


class VillagerAcquireTradeEvent(EntityEvent, Cancellable):
    """
    Called whenever a villager acquires a new trade.
    """

    def __init__(self, what: "AbstractVillager", recipe: "MerchantRecipe"):
        ...


    def getRecipe(self) -> "MerchantRecipe":
        """
        Get the recipe to be acquired.

        Returns
        - the new recipe
        """
        ...


    def setRecipe(self, recipe: "MerchantRecipe") -> None:
        """
        Set the recipe to be acquired.

        Arguments
        - recipe: the new recipe
        """
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getEntity(self) -> "AbstractVillager":
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
