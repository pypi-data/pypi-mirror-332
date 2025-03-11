"""
Python module generated from Java source file org.bukkit.inventory.view.EnchantmentView

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.enchantments import EnchantmentOffer
from org.bukkit.inventory import EnchantingInventory
from org.bukkit.inventory import InventoryView
from org.bukkit.inventory.view import *
from typing import Any, Callable, Iterable, Tuple


class EnchantmentView(InventoryView):
    """
    An instance of InventoryView which provides extra methods related to
    enchantment table view data.
    """

    def getTopInventory(self) -> "EnchantingInventory":
        ...


    def getEnchantmentSeed(self) -> int:
        """
        Gets the random enchantment seed used in this view

        Returns
        - The random seed used
        """
        ...


    def getOffers(self) -> list["EnchantmentOffer"]:
        """
        Gets the offers of this EnchantmentView

        Returns
        - The enchantment offers that are provided
        """
        ...


    def setOffers(self, offers: list["EnchantmentOffer"]) -> None:
        """
        Sets the offers to provide to the player.

        Arguments
        - offers: The offers to provide

        Raises
        - IllegalArgumentException: if the array length isn't 3
        """
        ...
