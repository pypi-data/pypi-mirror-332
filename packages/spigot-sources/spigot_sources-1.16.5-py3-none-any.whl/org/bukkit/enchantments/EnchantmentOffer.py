"""
Python module generated from Java source file org.bukkit.enchantments.EnchantmentOffer

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.apache.commons.lang import Validate
from org.bukkit.enchantments import *
from typing import Any, Callable, Iterable, Tuple


class EnchantmentOffer:
    """
    A class for the available enchantment offers in the enchantment table.
    """

    def __init__(self, enchantment: "Enchantment", enchantmentLevel: int, cost: int):
        ...


    def getEnchantment(self) -> "Enchantment":
        """
        Get the type of the enchantment.

        Returns
        - type of enchantment
        """
        ...


    def setEnchantment(self, enchantment: "Enchantment") -> None:
        """
        Sets the type of the enchantment.

        Arguments
        - enchantment: type of the enchantment
        """
        ...


    def getEnchantmentLevel(self) -> int:
        """
        Gets the level of the enchantment.

        Returns
        - level of the enchantment
        """
        ...


    def setEnchantmentLevel(self, enchantmentLevel: int) -> None:
        """
        Sets the level of the enchantment.

        Arguments
        - enchantmentLevel: level of the enchantment
        """
        ...


    def getCost(self) -> int:
        """
        Gets the cost (minimum level) which is displayed as a number on the right
        hand side of the enchantment offer.

        Returns
        - cost for this enchantment
        """
        ...


    def setCost(self, cost: int) -> None:
        """
        Sets the cost (minimum level) which is displayed as a number on the right
        hand side of the enchantment offer.

        Arguments
        - cost: cost for this enchantment
        """
        ...
