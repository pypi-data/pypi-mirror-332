"""
Python module generated from Java source file org.bukkit.inventory.meta.Damageable

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.inventory.meta import *
from typing import Any, Callable, Iterable, Tuple


class Damageable(ItemMeta):
    """
    Represents an item that has durability and can take damage.
    """

    def hasDamage(self) -> bool:
        """
        Checks to see if this item has damage

        Returns
        - True if this has damage
        """
        ...


    def getDamage(self) -> int:
        """
        Gets the damage

        Returns
        - the damage
        """
        ...


    def setDamage(self, damage: int) -> None:
        """
        Sets the damage

        Arguments
        - damage: item damage
        """
        ...


    def clone(self) -> "Damageable":
        ...
