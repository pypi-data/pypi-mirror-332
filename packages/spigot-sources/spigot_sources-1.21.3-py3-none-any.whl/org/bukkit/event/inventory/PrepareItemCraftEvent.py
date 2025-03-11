"""
Python module generated from Java source file org.bukkit.event.inventory.PrepareItemCraftEvent

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.event import HandlerList
from org.bukkit.event.inventory import *
from org.bukkit.inventory import CraftingInventory
from org.bukkit.inventory import InventoryView
from org.bukkit.inventory import Recipe
from typing import Any, Callable, Iterable, Tuple


class PrepareItemCraftEvent(InventoryEvent):

    def __init__(self, what: "CraftingInventory", view: "InventoryView", isRepair: bool):
        ...


    def getRecipe(self) -> "Recipe":
        """
        Get the recipe that has been formed. If this event was triggered by a
        tool repair, this will be a temporary shapeless recipe representing the
        repair.

        Returns
        - The recipe being crafted.
        """
        ...


    def getInventory(self) -> "CraftingInventory":
        """
        Returns
        - The crafting inventory on which the recipe was formed.
        """
        ...


    def isRepair(self) -> bool:
        """
        Check if this event was triggered by a tool repair operation rather
        than a crafting recipe.

        Returns
        - True if this is a repair.
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
