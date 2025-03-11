"""
Python module generated from Java source file org.bukkit.event.block.CrafterCraftEvent

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.block import *
from org.bukkit.inventory import CraftingRecipe
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class CrafterCraftEvent(BlockEvent, Cancellable):
    """
    Event called when a Crafter is about to craft an item.
    """

    def __init__(self, theBlock: "Block", recipe: "CraftingRecipe", result: "ItemStack"):
        ...


    def getResult(self) -> "ItemStack":
        """
        Gets the result for the craft.

        Returns
        - the result for the craft
        """
        ...


    def setResult(self, result: "ItemStack") -> None:
        """
        Sets the result of the craft.

        Arguments
        - result: the result of the craft
        """
        ...


    def getRecipe(self) -> "CraftingRecipe":
        """
        Gets the recipe that was used to craft this item.

        Returns
        - the recipe that was used to craft this item
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
