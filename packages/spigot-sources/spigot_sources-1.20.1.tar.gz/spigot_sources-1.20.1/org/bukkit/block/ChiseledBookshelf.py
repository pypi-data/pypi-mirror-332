"""
Python module generated from Java source file org.bukkit.block.ChiseledBookshelf

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import *
from org.bukkit.inventory import BlockInventoryHolder
from org.bukkit.inventory import ChiseledBookshelfInventory
from org.bukkit.util import Vector
from typing import Any, Callable, Iterable, Tuple


class ChiseledBookshelf(TileState, BlockInventoryHolder):
    """
    Represents a captured state of a chiseled bookshelf.
    """

    def getLastInteractedSlot(self) -> int:
        """
        Gets the last interacted inventory slot.

        Returns
        - the last interacted slot
        """
        ...


    def setLastInteractedSlot(self, lastInteractedSlot: int) -> None:
        """
        Sets the last interacted inventory slot.

        Arguments
        - lastInteractedSlot: the new last interacted slot
        """
        ...


    def getInventory(self) -> "ChiseledBookshelfInventory":
        """
        Returns
        - inventory

        See
        - Container.getInventory()
        """
        ...


    def getSnapshotInventory(self) -> "ChiseledBookshelfInventory":
        """
        Returns
        - snapshot inventory

        See
        - Container.getSnapshotInventory()
        """
        ...


    def getSlot(self, position: "Vector") -> int:
        """
        Gets the appropriate slot based on a vector relative to this block.
        Will return -1 if the given vector is not within the bounds of any slot.
        
        The supplied vector should only contain components with values between 0.0
        and 1.0, inclusive.

        Arguments
        - position: a vector relative to this block

        Returns
        - the slot under the given vector or -1
        """
        ...
