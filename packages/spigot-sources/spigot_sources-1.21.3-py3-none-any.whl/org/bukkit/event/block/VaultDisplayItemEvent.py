"""
Python module generated from Java source file org.bukkit.event.block.VaultDisplayItemEvent

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.block import *
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class VaultDisplayItemEvent(BlockEvent, Cancellable):
    """
    Called when a vault in a trial chamber is about to display an item.
    """

    def __init__(self, theBlock: "Block", displayItem: "ItemStack"):
        ...


    def getDisplayItem(self) -> "ItemStack":
        """
        Gets the item that will be displayed inside the vault.

        Returns
        - the item to be displayed
        """
        ...


    def setDisplayItem(self, displayItem: "ItemStack") -> None:
        """
        Sets the item that will be displayed inside the vault.

        Arguments
        - displayItem: the item to be displayed
        """
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancelled: bool) -> None:
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
