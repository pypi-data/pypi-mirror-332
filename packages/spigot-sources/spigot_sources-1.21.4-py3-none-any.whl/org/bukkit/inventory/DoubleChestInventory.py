"""
Python module generated from Java source file org.bukkit.inventory.DoubleChestInventory

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import DoubleChest
from org.bukkit.inventory import *
from typing import Any, Callable, Iterable, Tuple


class DoubleChestInventory(Inventory):
    """
    Interface to the inventory of a Double Chest.
    """

    def getLeftSide(self) -> "Inventory":
        """
        Get the left half of this double chest.

        Returns
        - The left side inventory
        """
        ...


    def getRightSide(self) -> "Inventory":
        """
        Get the right side of this double chest.

        Returns
        - The right side inventory
        """
        ...


    def getHolder(self) -> "DoubleChest":
        ...
