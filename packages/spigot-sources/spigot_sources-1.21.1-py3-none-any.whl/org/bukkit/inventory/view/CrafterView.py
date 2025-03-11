"""
Python module generated from Java source file org.bukkit.inventory.view.CrafterView

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.inventory import CrafterInventory
from org.bukkit.inventory import InventoryView
from org.bukkit.inventory.view import *
from typing import Any, Callable, Iterable, Tuple


class CrafterView(InventoryView):
    """
    An instance of InventoryView which provides extra methods related to
    crafter view data.
    """

    def getTopInventory(self) -> "CrafterInventory":
        ...


    def isSlotDisabled(self, slot: int) -> bool:
        """
        Checks if the given crafter slot is disabled.

        Arguments
        - slot: the slot to check

        Returns
        - True if the slot is disabled otherwise False
        """
        ...


    def isPowered(self) -> bool:
        """
        Checks whether or not this crafter view is powered.

        Returns
        - True if the crafter is powered
        """
        ...


    def setSlotDisabled(self, slot: int, disabled: bool) -> None:
        """
        Sets the status of the crafter slot.

        Arguments
        - slot: the slot to set the status of
        - disabled: True if the slot should be disabled otherwise False
        """
        ...
