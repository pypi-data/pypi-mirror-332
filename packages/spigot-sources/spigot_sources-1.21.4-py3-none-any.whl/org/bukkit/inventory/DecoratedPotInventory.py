"""
Python module generated from Java source file org.bukkit.inventory.DecoratedPotInventory

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import DecoratedPot
from org.bukkit.inventory import *
from typing import Any, Callable, Iterable, Tuple


class DecoratedPotInventory(Inventory):
    """
    Interface to the inventory of a DecoratedPot.
    """

    def setItem(self, item: "ItemStack") -> None:
        """
        Set the item stack in the decorated pot.

        Arguments
        - item: the new item stack
        """
        ...


    def getItem(self) -> "ItemStack":
        """
        Get the item stack in the decorated pot.

        Returns
        - the current item stack
        """
        ...


    def getHolder(self) -> "DecoratedPot":
        ...
