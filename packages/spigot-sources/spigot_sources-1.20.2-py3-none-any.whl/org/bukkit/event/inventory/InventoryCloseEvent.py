"""
Python module generated from Java source file org.bukkit.event.inventory.InventoryCloseEvent

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import HumanEntity
from org.bukkit.event import HandlerList
from org.bukkit.event.inventory import *
from org.bukkit.inventory import InventoryView
from typing import Any, Callable, Iterable, Tuple


class InventoryCloseEvent(InventoryEvent):
    """
    Represents a player related inventory event
    """

    def __init__(self, transaction: "InventoryView"):
        ...


    def getPlayer(self) -> "HumanEntity":
        """
        Returns the player involved in this event

        Returns
        - Player who is involved in this event
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
