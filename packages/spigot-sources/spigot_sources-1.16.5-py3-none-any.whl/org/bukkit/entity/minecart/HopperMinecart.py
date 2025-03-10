"""
Python module generated from Java source file org.bukkit.entity.minecart.HopperMinecart

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Minecart
from org.bukkit.entity.minecart import *
from org.bukkit.inventory import InventoryHolder
from org.bukkit.loot import Lootable
from typing import Any, Callable, Iterable, Tuple


class HopperMinecart(Minecart, InventoryHolder, Lootable):
    """
    Represents a Minecart with a Hopper inside it
    """

    def isEnabled(self) -> bool:
        """
        Checks whether or not this Minecart will pick up
        items into its inventory.

        Returns
        - True if the Minecart will pick up items
        """
        ...


    def setEnabled(self, enabled: bool) -> None:
        """
        Sets whether this Minecart will pick up items.

        Arguments
        - enabled: new enabled state
        """
        ...
