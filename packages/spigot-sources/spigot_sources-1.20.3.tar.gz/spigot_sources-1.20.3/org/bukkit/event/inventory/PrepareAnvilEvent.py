"""
Python module generated from Java source file org.bukkit.event.inventory.PrepareAnvilEvent

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.event import HandlerList
from org.bukkit.event.inventory import *
from org.bukkit.inventory import AnvilInventory
from org.bukkit.inventory import InventoryView
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class PrepareAnvilEvent(PrepareInventoryResultEvent):
    """
    Called when an item is put in a slot for repair by an anvil.
    """

    def __init__(self, inventory: "InventoryView", result: "ItemStack"):
        ...


    def getInventory(self) -> "AnvilInventory":
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
