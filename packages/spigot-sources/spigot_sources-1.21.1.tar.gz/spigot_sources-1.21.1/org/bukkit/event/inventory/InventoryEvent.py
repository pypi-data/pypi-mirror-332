"""
Python module generated from Java source file org.bukkit.event.inventory.InventoryEvent

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import HumanEntity
from org.bukkit.event import Event
from org.bukkit.event import HandlerList
from org.bukkit.event.inventory import *
from org.bukkit.inventory import Inventory
from org.bukkit.inventory import InventoryView
from typing import Any, Callable, Iterable, Tuple


class InventoryEvent(Event):
    """
    Represents a player related inventory event
    """

    def __init__(self, transaction: "InventoryView"):
        ...


    def getInventory(self) -> "Inventory":
        """
        Gets the primary Inventory involved in this transaction

        Returns
        - The upper inventory.
        """
        ...


    def getViewers(self) -> list["HumanEntity"]:
        """
        Gets the list of players viewing the primary (upper) inventory involved
        in this event

        Returns
        - A list of people viewing.
        """
        ...


    def getView(self) -> "InventoryView":
        """
        Gets the view object itself

        Returns
        - InventoryView
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
