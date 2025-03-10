"""
Python module generated from Java source file org.bukkit.block.Dropper

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import *
from org.bukkit.loot import Lootable
from typing import Any, Callable, Iterable, Tuple


class Dropper(Container, Lootable):
    """
    Represents a captured state of a dropper.
    """

    def drop(self) -> None:
        """
        Tries to drop a randomly selected item from the dropper's inventory,
        following the normal behavior of a dropper.
        
        Normal behavior of a dropper is as follows:
        
        If the block that the dropper is facing is an InventoryHolder,
        the randomly selected ItemStack is placed within that
        Inventory in the first slot that's available, starting with 0 and
        counting up.  If the inventory is full, nothing happens.
        
        If the block that the dropper is facing is not an InventoryHolder,
        the randomly selected ItemStack is dropped on
        the ground in the form of an org.bukkit.entity.Item Item.
        
        If the block represented by this state is no longer a dropper, this will
        do nothing.

        Raises
        - IllegalStateException: if this block state is not placed
        """
        ...
