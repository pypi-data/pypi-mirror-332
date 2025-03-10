"""
Python module generated from Java source file org.bukkit.event.inventory.PrepareInventoryResultEvent

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.event import HandlerList
from org.bukkit.event.inventory import *
from org.bukkit.inventory import InventoryView
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class PrepareInventoryResultEvent(InventoryEvent):
    """
    Called when an item is put in a slot and the result is calculated.
    """

    def __init__(self, inventory: "InventoryView", result: "ItemStack"):
        ...


    def getResult(self) -> "ItemStack":
        """
        Get result item, may be null.

        Returns
        - result item
        """
        ...


    def setResult(self, result: "ItemStack") -> None:
        """
        Set result item, may be null.

        Arguments
        - result: result item
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
