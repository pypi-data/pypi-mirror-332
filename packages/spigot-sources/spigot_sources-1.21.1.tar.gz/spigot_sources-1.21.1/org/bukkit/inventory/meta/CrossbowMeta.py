"""
Python module generated from Java source file org.bukkit.inventory.meta.CrossbowMeta

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.inventory import ItemStack
from org.bukkit.inventory.meta import *
from typing import Any, Callable, Iterable, Tuple


class CrossbowMeta(ItemMeta):

    def hasChargedProjectiles(self) -> bool:
        """
        Returns whether the item has any charged projectiles.

        Returns
        - whether charged projectiles are present
        """
        ...


    def getChargedProjectiles(self) -> list["ItemStack"]:
        """
        Returns an immutable list of the projectiles charged on this item.

        Returns
        - charged projectiles
        """
        ...


    def setChargedProjectiles(self, projectiles: list["ItemStack"]) -> None:
        """
        Sets the projectiles charged on this item.
        
        Removes all projectiles when given null.

        Arguments
        - projectiles: the projectiles to set

        Raises
        - IllegalArgumentException: if one of the projectiles is not an
        arrow or firework rocket
        """
        ...


    def addChargedProjectile(self, item: "ItemStack") -> None:
        """
        Adds a charged projectile to this item.

        Arguments
        - item: projectile

        Raises
        - IllegalArgumentException: if the projectile is not an arrow or
        firework rocket
        """
        ...
