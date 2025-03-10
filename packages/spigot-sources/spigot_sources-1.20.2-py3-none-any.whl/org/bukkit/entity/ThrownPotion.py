"""
Python module generated from Java source file org.bukkit.entity.ThrownPotion

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from org.bukkit.inventory import ItemStack
from org.bukkit.potion import PotionEffect
from typing import Any, Callable, Iterable, Tuple


class ThrownPotion(ThrowableProjectile):
    """
    Represents a thrown potion bottle
    """

    def getEffects(self) -> Iterable["PotionEffect"]:
        """
        Returns the effects that are applied by this potion.

        Returns
        - The potion effects
        """
        ...


    def getItem(self) -> "ItemStack":
        """
        Returns a copy of the ItemStack for this thrown potion.
        
        Altering this copy will not alter the thrown potion directly. If you want
        to alter the thrown potion, you must use the .setItem(ItemStack) setItemStack method.

        Returns
        - A copy of the ItemStack for this thrown potion.
        """
        ...


    def setItem(self, item: "ItemStack") -> None:
        """
        Set the ItemStack for this thrown potion.
        
        The ItemStack must be of type org.bukkit.Material.SPLASH_POTION
        or org.bukkit.Material.LINGERING_POTION, otherwise an exception
        is thrown.

        Arguments
        - item: New ItemStack
        """
        ...
