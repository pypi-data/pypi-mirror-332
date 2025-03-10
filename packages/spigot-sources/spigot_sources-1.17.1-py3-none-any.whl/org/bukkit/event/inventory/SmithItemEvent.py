"""
Python module generated from Java source file org.bukkit.event.inventory.SmithItemEvent

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.event.inventory import *
from org.bukkit.inventory import InventoryView
from org.bukkit.inventory import SmithingInventory
from typing import Any, Callable, Iterable, Tuple


class SmithItemEvent(InventoryClickEvent):
    """
    Called when the recipe of an Item is completed inside a smithing table.
    """

    def __init__(self, view: "InventoryView", type: "InventoryType.SlotType", slot: int, click: "ClickType", action: "InventoryAction"):
        ...


    def __init__(self, view: "InventoryView", type: "InventoryType.SlotType", slot: int, click: "ClickType", action: "InventoryAction", key: int):
        ...


    def getInventory(self) -> "SmithingInventory":
        ...
