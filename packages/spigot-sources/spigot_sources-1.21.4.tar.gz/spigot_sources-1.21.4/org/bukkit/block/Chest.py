"""
Python module generated from Java source file org.bukkit.block.Chest

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import *
from org.bukkit.inventory import Inventory
from org.bukkit.loot import Lootable
from typing import Any, Callable, Iterable, Tuple


class Chest(Container, Lootable, Lidded):
    """
    Represents a captured state of a chest.
    """

    def getBlockInventory(self) -> "Inventory":
        """
        Gets the inventory of the chest block represented by this block state.
        
        If the chest is a double chest, it returns just the portion of the
        inventory linked to the half of the chest corresponding to this block state.
        
        If the block was changed to a different type in the meantime, the
        returned inventory might no longer be valid.
        
        If this block state is not placed this will return the captured
        inventory snapshot instead.

        Returns
        - the inventory
        """
        ...
