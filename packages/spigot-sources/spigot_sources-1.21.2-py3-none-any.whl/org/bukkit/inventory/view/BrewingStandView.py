"""
Python module generated from Java source file org.bukkit.inventory.view.BrewingStandView

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.inventory import BrewerInventory
from org.bukkit.inventory import InventoryView
from org.bukkit.inventory.view import *
from typing import Any, Callable, Iterable, Tuple


class BrewingStandView(InventoryView):
    """
    An instance of InventoryView which provides extra methods related to
    brewing stand view data.
    """

    def getTopInventory(self) -> "BrewerInventory":
        ...


    def getFuelLevel(self) -> int:
        """
        Gets the fuel level of this brewing stand.
        
        The default maximum fuel level in minecraft is 20.

        Returns
        - The amount of fuel level left
        """
        ...


    def getBrewingTicks(self) -> int:
        """
        Gets the amount of brewing ticks left.

        Returns
        - The amount of ticks left for the brewing task
        """
        ...


    def setFuelLevel(self, level: int) -> None:
        """
        Sets the fuel level left.

        Arguments
        - level: the level of the fuel, which is no less than 0

        Raises
        - IllegalArgumentException: if the level is less than 0
        """
        ...


    def setBrewingTicks(self, ticks: int) -> None:
        """
        Sets the brewing ticks left.

        Arguments
        - ticks: the ticks left, which is no less than 0

        Raises
        - IllegalArgumentException: if the ticks are less than 0
        """
        ...
