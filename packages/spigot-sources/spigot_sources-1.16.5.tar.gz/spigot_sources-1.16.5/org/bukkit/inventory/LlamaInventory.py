"""
Python module generated from Java source file org.bukkit.inventory.LlamaInventory

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Llama
from org.bukkit.inventory import *
from typing import Any, Callable, Iterable, Tuple


class LlamaInventory(AbstractHorseInventory):
    """
    An interface to the inventory of a Llama.
    """

    def getDecor(self) -> "ItemStack":
        """
        Gets the item in the llama's decor slot.

        Returns
        - the decor item
        """
        ...


    def setDecor(self, stack: "ItemStack") -> None:
        """
        Sets the item in the llama's decor slot.

        Arguments
        - stack: the new item
        """
        ...
