"""
Python module generated from Java source file org.bukkit.event.block.BlockDispenseEvent

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.block import *
from org.bukkit.inventory import ItemStack
from org.bukkit.util import Vector
from typing import Any, Callable, Iterable, Tuple


class BlockDispenseEvent(BlockEvent, Cancellable):
    """
    Called when an item is dispensed from a block.
    
    If a Block Dispense event is cancelled, the block will not dispense the
    item.
    """

    def __init__(self, block: "Block", dispensed: "ItemStack", velocity: "Vector"):
        ...


    def getItem(self) -> "ItemStack":
        """
        Gets the item that is being dispensed. Modifying the returned item will
        have no effect, you must use .setItem(org.bukkit.inventory.ItemStack) instead.

        Returns
        - An ItemStack for the item being dispensed
        """
        ...


    def setItem(self, item: "ItemStack") -> None:
        """
        Sets the item being dispensed.

        Arguments
        - item: the item being dispensed
        """
        ...


    def getVelocity(self) -> "Vector":
        """
        Gets the velocity in meters per tick.
        
        Note: Modifying the returned Vector will not change the velocity, you
        must use .setVelocity(org.bukkit.util.Vector) instead.

        Returns
        - A Vector for the dispensed item's velocity
        """
        ...


    def setVelocity(self, vel: "Vector") -> None:
        """
        Sets the velocity of the item being dispensed in meters per tick.

        Arguments
        - vel: the velocity of the item being dispensed
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
