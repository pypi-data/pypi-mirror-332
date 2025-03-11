"""
Python module generated from Java source file org.bukkit.inventory.meta.EnchantmentStorageMeta

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.enchantments import Enchantment
from org.bukkit.inventory.meta import *
from typing import Any, Callable, Iterable, Tuple


class EnchantmentStorageMeta(ItemMeta):
    """
    EnchantmentMeta is specific to items that can *store* enchantments, as
    opposed to being enchanted. Material.ENCHANTED_BOOK is an example
    of an item with enchantment storage.
    """

    def hasStoredEnchants(self) -> bool:
        """
        Checks for the existence of any stored enchantments.

        Returns
        - True if an enchantment exists on this meta
        """
        ...


    def hasStoredEnchant(self, ench: "Enchantment") -> bool:
        """
        Checks for storage of the specified enchantment.

        Arguments
        - ench: enchantment to check

        Returns
        - True if this enchantment is stored in this meta
        """
        ...


    def getStoredEnchantLevel(self, ench: "Enchantment") -> int:
        """
        Checks for the level of the stored enchantment.

        Arguments
        - ench: enchantment to check

        Returns
        - The level that the specified stored enchantment has, or 0 if
            none
        """
        ...


    def getStoredEnchants(self) -> dict["Enchantment", "Integer"]:
        """
        Gets a copy the stored enchantments in this ItemMeta.

        Returns
        - An immutable copy of the stored enchantments
        """
        ...


    def addStoredEnchant(self, ench: "Enchantment", level: int, ignoreLevelRestriction: bool) -> bool:
        """
        Stores the specified enchantment in this item meta.

        Arguments
        - ench: Enchantment to store
        - level: Level for the enchantment
        - ignoreLevelRestriction: this indicates the enchantment should be
            applied, ignoring the level limit

        Returns
        - True if the item meta changed as a result of this call, False
            otherwise

        Raises
        - IllegalArgumentException: if enchantment is null
        """
        ...


    def removeStoredEnchant(self, ench: "Enchantment") -> bool:
        """
        Remove the specified stored enchantment from this item meta.

        Arguments
        - ench: Enchantment to remove

        Returns
        - True if the item meta changed as a result of this call, False
            otherwise

        Raises
        - IllegalArgumentException: if enchantment is null
        """
        ...


    def hasConflictingStoredEnchant(self, ench: "Enchantment") -> bool:
        """
        Checks if the specified enchantment conflicts with any enchantments in
        this ItemMeta.

        Arguments
        - ench: enchantment to test

        Returns
        - True if the enchantment conflicts, False otherwise
        """
        ...


    def clone(self) -> "EnchantmentStorageMeta":
        ...
