"""
Python module generated from Java source file org.bukkit.inventory.HorseInventory

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.inventory import *
from typing import Any, Callable, Iterable, Tuple


class HorseInventory(AbstractHorseInventory):
    """
    An interface to the inventory of a Horse.
    """

    def getArmor(self) -> "ItemStack":
        """
        Gets the item in the horse's armor slot.

        Returns
        - the armor item
        """
        ...


    def setArmor(self, stack: "ItemStack") -> None:
        """
        Sets the item in the horse's armor slot.

        Arguments
        - stack: the new item
        """
        ...
