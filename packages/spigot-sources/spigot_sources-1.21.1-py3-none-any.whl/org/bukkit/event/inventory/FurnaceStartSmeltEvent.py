"""
Python module generated from Java source file org.bukkit.event.inventory.FurnaceStartSmeltEvent

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.event import HandlerList
from org.bukkit.event.block import InventoryBlockStartEvent
from org.bukkit.event.inventory import *
from org.bukkit.inventory import CookingRecipe
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class FurnaceStartSmeltEvent(InventoryBlockStartEvent):
    """
    Called when a Furnace starts smelting.
    """

    def __init__(self, furnace: "Block", source: "ItemStack", recipe: "CookingRecipe"[Any]):
        ...


    def getRecipe(self) -> "CookingRecipe"[Any]:
        """
        Gets the FurnaceRecipe associated with this event

        Returns
        - the FurnaceRecipe being cooked
        """
        ...


    def getTotalCookTime(self) -> int:
        """
        Gets the total cook time associated with this event

        Returns
        - the total cook time
        """
        ...


    def setTotalCookTime(self, cookTime: int) -> None:
        """
        Sets the total cook time for this event

        Arguments
        - cookTime: the new total cook time
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
