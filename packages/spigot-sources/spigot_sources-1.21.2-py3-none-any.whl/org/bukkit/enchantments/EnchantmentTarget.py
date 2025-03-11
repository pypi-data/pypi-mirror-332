"""
Python module generated from Java source file org.bukkit.enchantments.EnchantmentTarget

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit import Material
from org.bukkit.enchantments import *
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class EnchantmentTarget(Enum):
    """
    Represents the applicable target for a Enchantment
    """

    ALL = 0
    """
    Allows the Enchantment to be placed on all items

    Deprecated
    - this target no longer exists in Vanilla
    """
    ARMOR = 1
    """
    Allows the Enchantment to be placed on armor
    """
    ARMOR_FEET = 2
    """
    Allows the Enchantment to be placed on feet slot armor
    """
    ARMOR_LEGS = 3
    """
    Allows the Enchantment to be placed on leg slot armor
    """
    ARMOR_TORSO = 4
    """
    Allows the Enchantment to be placed on torso slot armor
    """
    ARMOR_HEAD = 5
    """
    Allows the Enchantment to be placed on head slot armor
    """
    WEAPON = 6
    """
    Allows the Enchantment to be placed on weapons (swords)
    """
    TOOL = 7
    """
    Allows the Enchantment to be placed on tools (spades, pickaxe, axes)
    """
    BOW = 8
    """
    Allows the Enchantment to be placed on bows.
    """
    FISHING_ROD = 9
    """
    Allows the Enchantment to be placed on fishing rods.
    """
    BREAKABLE = 10
    """
    Allows the enchantment to be placed on items with durability.
    """
    WEARABLE = 11
    """
    Allows the enchantment to be placed on wearable items.
    """
    TRIDENT = 12
    """
    Allow the Enchantment to be placed on tridents.
    """
    CROSSBOW = 13
    """
    Allow the Enchantment to be placed on crossbows.
    """
    VANISHABLE = 14
    """
    Allow the Enchantment to be placed on vanishing items.
    """


    def includes(self, item: "Material") -> bool:
        """
        Check whether this target includes the specified item.

        Arguments
        - item: The item to check

        Returns
        - True if the target includes the item
        """
        ...


    def includes(self, item: "ItemStack") -> bool:
        """
        Check whether this target includes the specified item.

        Arguments
        - item: The item to check

        Returns
        - True if the target includes the item
        """
        ...
