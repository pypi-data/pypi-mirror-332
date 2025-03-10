"""
Python module generated from Java source file org.bukkit.block.ShulkerBox

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import DyeColor
from org.bukkit.block import *
from org.bukkit.loot import Lootable
from typing import Any, Callable, Iterable, Tuple


class ShulkerBox(Container, Lootable, Lidded):
    """
    Represents a captured state of a ShulkerBox.
    """

    def getColor(self) -> "DyeColor":
        """
        Get the DyeColor corresponding to this ShulkerBox

        Returns
        - the DyeColor of this ShulkerBox, or null if default
        """
        ...
