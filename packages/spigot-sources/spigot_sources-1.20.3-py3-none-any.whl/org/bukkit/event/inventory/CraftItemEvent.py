"""
Python module generated from Java source file org.bukkit.event.inventory.CraftItemEvent

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.event.inventory import *
from org.bukkit.event.inventory.InventoryType import SlotType
from org.bukkit.inventory import CraftingInventory
from org.bukkit.inventory import InventoryView
from org.bukkit.inventory import Recipe
from typing import Any, Callable, Iterable, Tuple


class CraftItemEvent(InventoryClickEvent):
    """
    Called when the recipe of an Item is completed inside a crafting matrix.
    """

    def __init__(self, recipe: "Recipe", what: "InventoryView", type: "SlotType", slot: int, click: "ClickType", action: "InventoryAction"):
        ...


    def __init__(self, recipe: "Recipe", what: "InventoryView", type: "SlotType", slot: int, click: "ClickType", action: "InventoryAction", key: int):
        ...


    def getRecipe(self) -> "Recipe":
        """
        Returns
        - A copy of the current recipe on the crafting matrix.
        """
        ...


    def getInventory(self) -> "CraftingInventory":
        ...
