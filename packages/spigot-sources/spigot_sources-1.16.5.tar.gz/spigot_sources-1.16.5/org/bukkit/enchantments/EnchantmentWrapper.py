"""
Python module generated from Java source file org.bukkit.enchantments.EnchantmentWrapper

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import NamespacedKey
from org.bukkit.enchantments import *
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class EnchantmentWrapper(Enchantment):
    """
    A simple wrapper for ease of selecting Enchantments
    """

    def __init__(self, name: str):
        ...


    def getEnchantment(self) -> "Enchantment":
        """
        Gets the enchantment bound to this wrapper

        Returns
        - Enchantment
        """
        ...


    def getMaxLevel(self) -> int:
        ...


    def getStartLevel(self) -> int:
        ...


    def getItemTarget(self) -> "EnchantmentTarget":
        ...


    def canEnchantItem(self, item: "ItemStack") -> bool:
        ...


    def getName(self) -> str:
        ...


    def isTreasure(self) -> bool:
        ...


    def isCursed(self) -> bool:
        ...


    def conflictsWith(self, other: "Enchantment") -> bool:
        ...
