"""
Python module generated from Java source file org.bukkit.inventory.meta.Damageable

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

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


    def hasMaxDamage(self) -> bool:
        """
        Checks to see if this item has a maximum amount of damage.

        Returns
        - True if this has maximum amount of damage
        """
        ...


    def getMaxDamage(self) -> int:
        """
        Gets the maximum amount of damage.
        
        Plugins should check .hasMaxDamage() before calling this method.

        Returns
        - the maximum amount of damage
        """
        ...


    def setMaxDamage(self, maxDamage: "Integer") -> None:
        """
        Sets the maximum amount of damage.

        Arguments
        - maxDamage: maximum amount of damage
        """
        ...


    def clone(self) -> "Damageable":
        ...
