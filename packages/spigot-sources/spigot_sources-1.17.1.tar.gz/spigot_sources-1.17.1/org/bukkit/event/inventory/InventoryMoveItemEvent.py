"""
Python module generated from Java source file org.bukkit.event.inventory.InventoryMoveItemEvent

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.apache.commons.lang import Validate
from org.bukkit.event import Cancellable
from org.bukkit.event import Event
from org.bukkit.event import HandlerList
from org.bukkit.event.inventory import *
from org.bukkit.inventory import Inventory
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class InventoryMoveItemEvent(Event, Cancellable):
    """
    Called when some entity or block (e.g. hopper) tries to move items directly
    from one inventory to another.
    
    When this event is called, the initiator may already have removed the item
    from the source inventory and is ready to move it into the destination
    inventory.
    
    If this event is cancelled, the items will be returned to the source
    inventory, if needed.
    
    If this event is not cancelled, the initiator will try to put the ItemStack
    into the destination inventory. If this is not possible and the ItemStack
    has not been modified, the source inventory slot will be restored to its
    former state. Otherwise any additional items will be discarded.
    """

    def __init__(self, sourceInventory: "Inventory", itemStack: "ItemStack", destinationInventory: "Inventory", didSourceInitiate: bool):
        ...


    def getSource(self) -> "Inventory":
        """
        Gets the Inventory that the ItemStack is being taken from

        Returns
        - Inventory that the ItemStack is being taken from
        """
        ...


    def getItem(self) -> "ItemStack":
        """
        Gets the ItemStack being moved; if modified, the original item will not
        be removed from the source inventory.

        Returns
        - ItemStack
        """
        ...


    def setItem(self, itemStack: "ItemStack") -> None:
        """
        Sets the ItemStack being moved; if this is different from the original
        ItemStack, the original item will not be removed from the source
        inventory.

        Arguments
        - itemStack: The ItemStack
        """
        ...


    def getDestination(self) -> "Inventory":
        """
        Gets the Inventory that the ItemStack is being put into

        Returns
        - Inventory that the ItemStack is being put into
        """
        ...


    def getInitiator(self) -> "Inventory":
        """
        Gets the Inventory that initiated the transfer. This will always be
        either the destination or source Inventory.

        Returns
        - Inventory that initiated the transfer
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
