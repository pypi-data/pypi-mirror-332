"""
Python module generated from Java source file org.bukkit.event.inventory.InventoryOpenEvent

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import HumanEntity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.inventory import *
from org.bukkit.inventory import InventoryView
from typing import Any, Callable, Iterable, Tuple


class InventoryOpenEvent(InventoryEvent, Cancellable):
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


    def isCancelled(self) -> bool:
        """
        Gets the cancellation state of this event. A cancelled event will not
        be executed in the server, but will still pass to other plugins.
        
        If an inventory open event is cancelled, the inventory screen will not
        show.

        Returns
        - True if this event is cancelled
        """
        ...


    def setCancelled(self, cancel: bool) -> None:
        """
        Sets the cancellation state of this event. A cancelled event will not
        be executed in the server, but will still pass to other plugins.
        
        If an inventory open event is cancelled, the inventory screen will not
        show.

        Arguments
        - cancel: True if you wish to cancel this event
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
