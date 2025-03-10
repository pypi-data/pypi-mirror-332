"""
Python module generated from Java source file org.bukkit.entity.SizedFireball

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class SizedFireball(Fireball):
    """
    Represents a sized fireball.
    """

    def getDisplayItem(self) -> "ItemStack":
        """
        Gets the display ItemStack.

        Returns
        - display ItemStack
        """
        ...


    def setDisplayItem(self, item: "ItemStack") -> None:
        """
        Sets the display ItemStack for the fireball.

        Arguments
        - item: the ItemStack to display
        """
        ...
