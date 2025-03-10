"""
Python module generated from Java source file org.bukkit.event.block.CampfireStartEvent

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.event import HandlerList
from org.bukkit.event.block import *
from org.bukkit.inventory import CampfireRecipe
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class CampfireStartEvent(InventoryBlockStartEvent):
    """
    Called when a Campfire starts to cook.
    """

    def __init__(self, furnace: "Block", source: "ItemStack", recipe: "CampfireRecipe"):
        ...


    def getRecipe(self) -> "CampfireRecipe":
        """
        Gets the CampfireRecipe associated with this event.

        Returns
        - the CampfireRecipe being cooked
        """
        ...


    def getTotalCookTime(self) -> int:
        """
        Gets the total cook time associated with this event.

        Returns
        - the total cook time
        """
        ...


    def setTotalCookTime(self, cookTime: int) -> None:
        """
        Sets the total cook time for this event.

        Arguments
        - cookTime: the new total cook time
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
