"""
Python module generated from Java source file org.bukkit.block.BrewingStand

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import *
from org.bukkit.inventory import BrewerInventory
from typing import Any, Callable, Iterable, Tuple


class BrewingStand(Container):
    """
    Represents a captured state of a brewing stand.
    """

    def getBrewingTime(self) -> int:
        """
        How much time is left in the brewing cycle.

        Returns
        - Brew Time
        """
        ...


    def setBrewingTime(self, brewTime: int) -> None:
        """
        Set the time left before brewing completes.

        Arguments
        - brewTime: Brewing time
        """
        ...


    def getFuelLevel(self) -> int:
        """
        Get the level of current fuel for brewing.

        Returns
        - The fuel level
        """
        ...


    def setFuelLevel(self, level: int) -> None:
        """
        Set the level of current fuel for brewing.

        Arguments
        - level: fuel level
        """
        ...


    def getInventory(self) -> "BrewerInventory":
        ...


    def getSnapshotInventory(self) -> "BrewerInventory":
        ...
