"""
Python module generated from Java source file org.bukkit.event.inventory.InventoryCreativeEvent

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.event.inventory import *
from org.bukkit.event.inventory.InventoryType import SlotType
from org.bukkit.inventory import InventoryView
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class InventoryCreativeEvent(InventoryClickEvent):
    """
    This event is called when a player in creative mode puts down or picks up
    an item in their inventory / hotbar and when they drop items from their
    Inventory while in creative mode.
    """

    def __init__(self, what: "InventoryView", type: "SlotType", slot: int, newItem: "ItemStack"):
        ...


    def getCursor(self) -> "ItemStack":
        ...


    def setCursor(self, item: "ItemStack") -> None:
        ...
