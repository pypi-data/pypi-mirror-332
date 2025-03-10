"""
Python module generated from Java source file org.bukkit.inventory.BeaconInventory

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.inventory import *
from typing import Any, Callable, Iterable, Tuple


class BeaconInventory(Inventory):
    """
    Interface to the inventory of a Beacon.
    """

    def setItem(self, item: "ItemStack") -> None:
        """
        Set the item powering the beacon.

        Arguments
        - item: The new item
        """
        ...


    def getItem(self) -> "ItemStack":
        """
        Get the item powering the beacon.

        Returns
        - The current item.
        """
        ...
