"""
Python module generated from Java source file org.bukkit.block.Container

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Nameable
from org.bukkit.block import *
from org.bukkit.inventory import BlockInventoryHolder
from org.bukkit.inventory import Inventory
from typing import Any, Callable, Iterable, Tuple


class Container(TileState, BlockInventoryHolder, Lockable, Nameable):
    """
    Represents a captured state of a container block.
    """

    def getInventory(self) -> "Inventory":
        """
        Gets the inventory of the block represented by this block state.
        
        If the block was changed to a different type in the meantime, the
        returned inventory might no longer be valid.
        
        If this block state is not placed this will return the captured inventory
        snapshot instead.

        Returns
        - the inventory
        """
        ...


    def getSnapshotInventory(self) -> "Inventory":
        """
        Gets the captured inventory snapshot of this container.
        
        The returned inventory is not linked to any block. Any modifications to
        the returned inventory will not be applied to the block represented by
        this block state up until .update(boolean, boolean) has been
        called.

        Returns
        - the captured inventory snapshot
        """
        ...
