"""
Python module generated from Java source file org.bukkit.event.entity.VillagerReplenishTradeEvent

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import AbstractVillager
from org.bukkit.entity import Villager
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from org.bukkit.inventory import MerchantRecipe
from typing import Any, Callable, Iterable, Tuple


class VillagerReplenishTradeEvent(EntityEvent, Cancellable):
    """
    Called when a Villager is about to restock one of its trades.
    
    If this event passes, the villager will reset the
    MerchantRecipe.getUses() uses of the affected .getRecipe()
    MerchantRecipe to `0`.
    """

    def __init__(self, what: "AbstractVillager", recipe: "MerchantRecipe"):
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
        Get the bonus uses added.

        Returns
        - the extra uses added

        Deprecated
        - MC 1.14 has changed how villagers restock their trades. Use
        MerchantRecipe.getUses().
        """
        ...


    def setBonus(self, bonus: int) -> None:
        """
        Set the bonus uses added.

        Arguments
        - bonus: the extra uses added

        Deprecated
        - MC 1.14 has changed how villagers restock their trades. This
        has no effect anymore.
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
