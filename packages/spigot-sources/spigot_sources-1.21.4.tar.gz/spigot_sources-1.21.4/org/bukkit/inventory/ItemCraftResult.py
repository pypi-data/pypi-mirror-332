"""
Python module generated from Java source file org.bukkit.inventory.ItemCraftResult

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.inventory import *
from typing import Any, Callable, Iterable, Tuple


class ItemCraftResult:
    """
    Container class containing the results of a Crafting event.
    
    This class makes no guarantees about the nature or mutability of the returned
    values.
    """

    def getResult(self) -> "ItemStack":
        """
        The resulting ItemStack that was crafted.

        Returns
        - ItemStack that was crafted.
        """
        ...


    def getResultingMatrix(self) -> list["ItemStack"]:
        """
        Gets the resulting matrix from the crafting operation.

        Returns
        - resulting matrix
        """
        ...


    def getOverflowItems(self) -> list["ItemStack"]:
        """
        Gets the overflowed items for items that don't fit back into the crafting
        matrix.

        Returns
        - overflow items
        """
        ...
