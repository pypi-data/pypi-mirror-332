"""
Python module generated from Java source file org.bukkit.inventory.AnvilInventory

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.inventory import *
from org.bukkit.inventory.view import AnvilView
from typing import Any, Callable, Iterable, Tuple


class AnvilInventory(Inventory):
    """
    Interface to the inventory of an Anvil.
    """

    def getRenameText(self) -> str:
        """
        Get the name to be applied to the repaired item. An empty string denotes
        the default item name.

        Returns
        - the rename text

        Deprecated
        - use AnvilView.getRenameText().
        """
        ...


    def getRepairCostAmount(self) -> int:
        """
        Get the item cost (in amount) to complete the current repair.

        Returns
        - the amount

        Deprecated
        - use AnvilView.getRepairItemCountCost().
        """
        ...


    def setRepairCostAmount(self, amount: int) -> None:
        """
        Set the item cost (in amount) to complete the current repair.

        Arguments
        - amount: the amount

        Deprecated
        - use AnvilView.setRepairItemCountCost(int).
        """
        ...


    def getRepairCost(self) -> int:
        """
        Get the experience cost (in levels) to complete the current repair.

        Returns
        - the experience cost

        Deprecated
        - use AnvilView.getRepairCost().
        """
        ...


    def setRepairCost(self, levels: int) -> None:
        """
        Set the experience cost (in levels) to complete the current repair.

        Arguments
        - levels: the experience cost

        Deprecated
        - use AnvilView.setRepairCost(int).
        """
        ...


    def getMaximumRepairCost(self) -> int:
        """
        Get the maximum experience cost (in levels) to be allowed by the current
        repair. If the result of .getRepairCost() exceeds the returned
        value, the repair result will be air to due being "too expensive".
        
        By default, this level is set to 40. Players in creative mode ignore the
        maximum repair cost.

        Returns
        - the maximum experience cost

        Deprecated
        - use AnvilView.getMaximumRepairCost().
        """
        ...


    def setMaximumRepairCost(self, levels: int) -> None:
        """
        Set the maximum experience cost (in levels) to be allowed by the current
        repair. The default value set by vanilla Minecraft is 40.

        Arguments
        - levels: the maximum experience cost

        Deprecated
        - use AnvilView.setMaximumRepairCost(int).
        """
        ...
