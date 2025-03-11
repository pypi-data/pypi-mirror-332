"""
Python module generated from Java source file org.bukkit.event.inventory.PrepareSmithingEvent

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.event import HandlerList
from org.bukkit.event.inventory import *
from org.bukkit.inventory import InventoryView
from org.bukkit.inventory import ItemStack
from org.bukkit.inventory import SmithingInventory
from typing import Any, Callable, Iterable, Tuple


class PrepareSmithingEvent(PrepareInventoryResultEvent):
    """
    Called when an item is put in a slot for upgrade by a Smithing Table.
    """

    def __init__(self, inventory: "InventoryView", result: "ItemStack"):
        ...


    def getInventory(self) -> "SmithingInventory":
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
