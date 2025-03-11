"""
Python module generated from Java source file org.bukkit.block.Furnace

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import *
from org.bukkit.inventory import CookingRecipe
from org.bukkit.inventory import FurnaceInventory
from typing import Any, Callable, Iterable, Tuple


class Furnace(Container):
    """
    Represents a captured state of a furnace.
    """

    def getBurnTime(self) -> int:
        """
        Get burn time.

        Returns
        - Burn time
        """
        ...


    def setBurnTime(self, burnTime: int) -> None:
        """
        Set burn time.
        
        A burn time greater than 0 will cause this block to be lit, whilst a time
        less than 0 will extinguish it.

        Arguments
        - burnTime: Burn time
        """
        ...


    def getCookTime(self) -> int:
        """
        Get cook time.
        
        This is the amount of time the item has been cooking for.

        Returns
        - Cook time
        """
        ...


    def setCookTime(self, cookTime: int) -> None:
        """
        Set cook time.
        
        This is the amount of time the item has been cooking for.

        Arguments
        - cookTime: Cook time
        """
        ...


    def getCookTimeTotal(self) -> int:
        """
        Get cook time total.
        
        This is the amount of time the item is required to cook for.

        Returns
        - Cook time total
        """
        ...


    def setCookTimeTotal(self, cookTimeTotal: int) -> None:
        """
        Set cook time.
        
        This is the amount of time the item is required to cook for.

        Arguments
        - cookTimeTotal: Cook time total
        """
        ...


    def getRecipesUsed(self) -> dict["CookingRecipe"[Any], "Integer"]:
        """
        Get the recipes used in this furnace.
        
        **Note:** These recipes used are reset when the result item is
        manually taken from the furnace.

        Returns
        - An immutable map with the recipes used and the times used
        """
        ...


    def getInventory(self) -> "FurnaceInventory":
        ...


    def getSnapshotInventory(self) -> "FurnaceInventory":
        ...
