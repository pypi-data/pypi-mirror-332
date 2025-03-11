"""
Python module generated from Java source file org.bukkit.block.BrushableBlock

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import *
from org.bukkit.inventory import ItemStack
from org.bukkit.loot import Lootable
from typing import Any, Callable, Iterable, Tuple


class BrushableBlock(Lootable, TileState):
    """
    Represents a captured state of suspicious sand or gravel.
    """

    def getItem(self) -> "ItemStack":
        """
        Get the item which will be revealed when the sand is fully brushed away
        and uncovered.

        Returns
        - the item
        """
        ...


    def setItem(self, item: "ItemStack") -> None:
        """
        Sets the item which will be revealed when the sand is fully brushed away
        and uncovered.

        Arguments
        - item: the item
        """
        ...
