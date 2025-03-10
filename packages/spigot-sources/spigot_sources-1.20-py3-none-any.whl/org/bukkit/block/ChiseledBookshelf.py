"""
Python module generated from Java source file org.bukkit.block.ChiseledBookshelf

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import *
from org.bukkit.inventory import BlockInventoryHolder
from org.bukkit.inventory import ChiseledBookshelfInventory
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
