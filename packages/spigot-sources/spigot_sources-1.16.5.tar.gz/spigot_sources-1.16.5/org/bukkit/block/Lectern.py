"""
Python module generated from Java source file org.bukkit.block.Lectern

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import *
from org.bukkit.inventory import BlockInventoryHolder
from org.bukkit.inventory import Inventory
from typing import Any, Callable, Iterable, Tuple


class Lectern(TileState, BlockInventoryHolder):
    """
    Represents a captured state of a lectern.
    """

    def getPage(self) -> int:
        """
        Get the current lectern page.

        Returns
        - current page
        """
        ...


    def setPage(self, page: int) -> None:
        """
        Set the current lectern page.
        
        If the page is greater than the number of pages of the book currently in
        the inventory, then behavior is undefined.

        Arguments
        - page: new page
        """
        ...


    def getInventory(self) -> "Inventory":
        """
        Returns
        - inventory

        See
        - Container.getInventory()
        """
        ...


    def getSnapshotInventory(self) -> "Inventory":
        """
        Returns
        - snapshot inventory

        See
        - Container.getSnapshotInventory()
        """
        ...
