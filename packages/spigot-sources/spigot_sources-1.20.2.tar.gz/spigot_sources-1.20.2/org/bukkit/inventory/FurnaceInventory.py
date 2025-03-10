"""
Python module generated from Java source file org.bukkit.inventory.FurnaceInventory

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Furnace
from org.bukkit.inventory import *
from typing import Any, Callable, Iterable, Tuple


class FurnaceInventory(Inventory):
    """
    Interface to the inventory of a Furnace.
    """

    def getResult(self) -> "ItemStack":
        """
        Get the current item in the result slot.

        Returns
        - The item
        """
        ...


    def getFuel(self) -> "ItemStack":
        """
        Get the current fuel.

        Returns
        - The item
        """
        ...


    def getSmelting(self) -> "ItemStack":
        """
        Get the item currently smelting.

        Returns
        - The item
        """
        ...


    def setFuel(self, stack: "ItemStack") -> None:
        """
        Set the current fuel.

        Arguments
        - stack: The item
        """
        ...


    def setResult(self, stack: "ItemStack") -> None:
        """
        Set the current item in the result slot.

        Arguments
        - stack: The item
        """
        ...


    def setSmelting(self, stack: "ItemStack") -> None:
        """
        Set the item currently smelting.

        Arguments
        - stack: The item
        """
        ...


    def getHolder(self) -> "Furnace":
        ...
