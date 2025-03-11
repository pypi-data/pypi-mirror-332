"""
Python module generated from Java source file org.bukkit.inventory.view.AnvilView

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.inventory import AnvilInventory
from org.bukkit.inventory import InventoryView
from org.bukkit.inventory.view import *
from typing import Any, Callable, Iterable, Tuple


class AnvilView(InventoryView):
    """
    An instance of InventoryView which provides extra methods related to
    anvil view data.
    """

    def getTopInventory(self) -> "AnvilInventory":
        ...


    def getRenameText(self) -> str:
        """
        Gets the rename text specified within the anvil's text field.

        Returns
        - The text within the anvil's text field if an item is present
        otherwise null
        """
        ...


    def getRepairItemCountCost(self) -> int:
        """
        Gets the amount of items needed to repair.

        Returns
        - The amount of materials required to repair the item
        """
        ...


    def getRepairCost(self) -> int:
        """
        Gets the experience cost needed to repair.

        Returns
        - The repair cost in experience
        """
        ...


    def getMaximumRepairCost(self) -> int:
        """
        Gets the maximum repair cost needed to repair.

        Returns
        - The maximum repair cost in experience
        """
        ...


    def setRepairItemCountCost(self, amount: int) -> None:
        """
        Sets the amount of repair materials required to repair the item.

        Arguments
        - amount: the amount of repair materials
        """
        ...


    def setRepairCost(self, cost: int) -> None:
        """
        Sets the repair cost in experience.

        Arguments
        - cost: the experience cost to repair
        """
        ...


    def setMaximumRepairCost(self, levels: int) -> None:
        """
        Sets maximum repair cost in experience.

        Arguments
        - levels: the levels to set
        """
        ...
