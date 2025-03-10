"""
Python module generated from Java source file org.bukkit.event.inventory.InventoryPickupItemEvent

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Item
from org.bukkit.event import Cancellable
from org.bukkit.event import Event
from org.bukkit.event import HandlerList
from org.bukkit.event.inventory import *
from org.bukkit.inventory import Inventory
from typing import Any, Callable, Iterable, Tuple


class InventoryPickupItemEvent(Event, Cancellable):
    """
    Called when a hopper or hopper minecart picks up a dropped item.
    """

    def __init__(self, inventory: "Inventory", item: "Item"):
        ...


    def getInventory(self) -> "Inventory":
        """
        Gets the Inventory that picked up the item

        Returns
        - Inventory
        """
        ...


    def getItem(self) -> "Item":
        """
        Gets the Item entity that was picked up

        Returns
        - Item
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
