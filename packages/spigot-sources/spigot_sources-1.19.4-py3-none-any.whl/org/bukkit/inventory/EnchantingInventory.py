"""
Python module generated from Java source file org.bukkit.inventory.EnchantingInventory

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.inventory import *
from typing import Any, Callable, Iterable, Tuple


class EnchantingInventory(Inventory):
    """
    Interface to the inventory of an Enchantment Table.
    """

    def setItem(self, item: "ItemStack") -> None:
        """
        Set the item being enchanted.

        Arguments
        - item: The new item
        """
        ...


    def getItem(self) -> "ItemStack":
        """
        Get the item being enchanted.

        Returns
        - The current item.
        """
        ...


    def setSecondary(self, item: "ItemStack") -> None:
        """
        Set the secondary item being used for the enchant.

        Arguments
        - item: The new item
        """
        ...


    def getSecondary(self) -> "ItemStack":
        """
        Get the secondary item being used for the enchant.

        Returns
        - The second item
        """
        ...
