"""
Python module generated from Java source file org.bukkit.event.entity.VillagerReplenishTradeEvent

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

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


class VillagerReplenishTradeEvent(EntityEvent, Cancellable):
    """
    Called when a villager's trade's maximum uses is increased, due to a player's
    trade.

    See
    - MerchantRecipe.getMaxUses()
    """

    def __init__(self, what: "AbstractVillager", recipe: "MerchantRecipe", bonus: int):
        ...


    def getRecipe(self) -> "MerchantRecipe":
        """
        Get the recipe to replenish.

        Returns
        - the replenished recipe
        """
        ...


    def setRecipe(self, recipe: "MerchantRecipe") -> None:
        """
        Set the recipe to replenish.

        Arguments
        - recipe: the replenished recipe
        """
        ...


    def getBonus(self) -> int:
        """
        Get the bonus uses added. The maximum uses of the recipe will be
        increased by this number.

        Returns
        - the extra uses added
        """
        ...


    def setBonus(self, bonus: int) -> None:
        """
        Set the bonus uses added.

        Arguments
        - bonus: the extra uses added

        See
        - VillagerReplenishTradeEvent.getBonus()
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
