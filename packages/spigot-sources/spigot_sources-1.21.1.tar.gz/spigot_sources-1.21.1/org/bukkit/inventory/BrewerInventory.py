"""
Python module generated from Java source file org.bukkit.inventory.BrewerInventory

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.block import BrewingStand
from org.bukkit.inventory import *
from typing import Any, Callable, Iterable, Tuple


class BrewerInventory(Inventory):
    """
    Interface to the inventory of a Brewing Stand.
    """

    def getIngredient(self) -> "ItemStack":
        """
        Get the current ingredient for brewing.

        Returns
        - The ingredient.
        """
        ...


    def setIngredient(self, ingredient: "ItemStack") -> None:
        """
        Set the current ingredient for brewing.

        Arguments
        - ingredient: The ingredient
        """
        ...


    def getFuel(self) -> "ItemStack":
        """
        Get the current fuel for brewing.

        Returns
        - The fuel
        """
        ...


    def setFuel(self, fuel: "ItemStack") -> None:
        """
        Set the current fuel for brewing. Generally only
        Material.BLAZE_POWDER will be of use.

        Arguments
        - fuel: The fuel
        """
        ...


    def getHolder(self) -> "BrewingStand":
        ...
