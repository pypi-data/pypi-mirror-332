"""
Python module generated from Java source file org.bukkit.inventory.view.LoomView

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.banner import PatternType
from org.bukkit.inventory import InventoryView
from org.bukkit.inventory import LoomInventory
from org.bukkit.inventory.view import *
from typing import Any, Callable, Iterable, Tuple


class LoomView(InventoryView):
    """
    An instance of InventoryView which provides extra methods related to
    loom view data.
    """

    def getTopInventory(self) -> "LoomInventory":
        ...


    def getSelectablePatterns(self) -> list["PatternType"]:
        """
        Gets a list of all selectable to the player.

        Returns
        - A copy of the PatternType's currently selectable by the
        player
        """
        ...


    def getSelectedPatternIndex(self) -> int:
        """
        Gets an index of the selected pattern.

        Returns
        - Index of the selected pattern
        """
        ...
