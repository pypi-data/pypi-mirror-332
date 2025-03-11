"""
Python module generated from Java source file org.bukkit.block.Crafter

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import *
from org.bukkit.loot import Lootable
from typing import Any, Callable, Iterable, Tuple


class Crafter(Container, Lootable):
    """
    Represents a captured state of a crafter.
    """

    def getCraftingTicks(self) -> int:
        """
        Gets the number of ticks which this block will remain in the crafting
        state for.

        Returns
        - number of ticks remaining

        See
        - org.bukkit.block.data.type.Crafter.isCrafting()
        """
        ...


    def setCraftingTicks(self, ticks: int) -> None:
        """
        Sets the number of ticks which this block will remain in the crafting
        state for.

        Arguments
        - ticks: number of ticks remaining

        See
        - org.bukkit.block.data.type.Crafter.isCrafting()
        """
        ...


    def isSlotDisabled(self, slot: int) -> bool:
        """
        Gets whether the slot at the specified index is disabled and will not
        have items placed in it.

        Arguments
        - slot: slot index

        Returns
        - disabled status
        """
        ...


    def setSlotDisabled(self, slot: int, disabled: bool) -> None:
        """
        Sets whether the slot at the specified index is disabled and will not
        have items placed in it.

        Arguments
        - slot: slot index
        - disabled: disabled status
        """
        ...


    def isTriggered(self) -> bool:
        """
        Gets whether this Crafter is powered.

        Returns
        - powered status
        """
        ...


    def setTriggered(self, triggered: bool) -> None:
        """
        Sets whether this Crafter is powered.

        Arguments
        - triggered: powered status
        """
        ...
