"""
Python module generated from Java source file org.bukkit.entity.ThrowableProjectile

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class ThrowableProjectile(Projectile):

    def getItem(self) -> "ItemStack":
        """
        Gets the ItemStack the thrown projectile will display.

        Returns
        - The thrown item display ItemStack
        """
        ...


    def setItem(self, item: "ItemStack") -> None:
        """
        Sets the display ItemStack for the thrown projectile.

        Arguments
        - item: ItemStack set to be displayed
        """
        ...
