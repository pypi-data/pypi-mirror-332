"""
Python module generated from Java source file org.bukkit.block.Campfire

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import *
from org.bukkit.inventory import Inventory
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class Campfire(TileState):
    """
    Represents a captured state of a campfire.
    """

    def getSize(self) -> int:
        """
        Returns
        - The size of the inventory

        See
        - Inventory.getSize()
        """
        ...


    def getItem(self, index: int) -> "ItemStack":
        """
        Arguments
        - index: The index of the Slot's ItemStack to return

        Returns
        - The ItemStack in the slot

        See
        - Inventory.getItem(int)
        """
        ...


    def setItem(self, index: int, item: "ItemStack") -> None:
        """
        Arguments
        - index: The index where to put the ItemStack
        - item: The ItemStack to set

        See
        - Inventory.setItem(int, org.bukkit.inventory.ItemStack)
        """
        ...


    def getCookTime(self, index: int) -> int:
        """
        Get cook time.
        
        This is the amount of time the item has been cooking for.

        Arguments
        - index: item slot index

        Returns
        - Cook time
        """
        ...


    def setCookTime(self, index: int, cookTime: int) -> None:
        """
        Set cook time.
        
        This is the amount of time the item has been cooking for.

        Arguments
        - index: item slot index
        - cookTime: Cook time
        """
        ...


    def getCookTimeTotal(self, index: int) -> int:
        """
        Get cook time total.
        
        This is the amount of time the item is required to cook for.

        Arguments
        - index: item slot index

        Returns
        - Cook time total
        """
        ...


    def setCookTimeTotal(self, index: int, cookTimeTotal: int) -> None:
        """
        Set cook time.
        
        This is the amount of time the item is required to cook for.

        Arguments
        - index: item slot index
        - cookTimeTotal: Cook time total
        """
        ...
