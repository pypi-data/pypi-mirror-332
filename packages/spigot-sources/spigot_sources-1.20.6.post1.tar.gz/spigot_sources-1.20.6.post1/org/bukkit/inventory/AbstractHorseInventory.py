"""
Python module generated from Java source file org.bukkit.inventory.AbstractHorseInventory

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import AbstractHorse
from org.bukkit.inventory import *
from typing import Any, Callable, Iterable, Tuple


class AbstractHorseInventory(Inventory):
    """
    An interface to the inventory of an AbstractHorse.
    """

    def getSaddle(self) -> "ItemStack":
        """
        Gets the item in the horse's saddle slot.

        Returns
        - the saddle item
        """
        ...


    def setSaddle(self, stack: "ItemStack") -> None:
        """
        Sets the item in the horse's saddle slot.

        Arguments
        - stack: the new item
        """
        ...
