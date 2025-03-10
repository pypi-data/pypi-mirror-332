"""
Python module generated from Java source file org.bukkit.inventory.ItemFlag

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.inventory import *
from typing import Any, Callable, Iterable, Tuple


class ItemFlag(Enum):
    """
    A ItemFlag can hide some Attributes from ItemStacks
    """

    HIDE_ENCHANTS = 0
    """
    Setting to show/hide enchants
    """
    HIDE_ATTRIBUTES = 1
    """
    Setting to show/hide Attributes like Damage
    """
    HIDE_UNBREAKABLE = 2
    """
    Setting to show/hide the unbreakable State
    """
    HIDE_DESTROYS = 3
    """
    Setting to show/hide what the ItemStack can break/destroy
    """
    HIDE_PLACED_ON = 4
    """
    Setting to show/hide where this ItemStack can be build/placed on
    """
    HIDE_ADDITIONAL_TOOLTIP = 5
    """
    Setting to show/hide potion effects, book and firework information, map
    tooltips, patterns of banners, and enchantments of enchanted books.
    """
    HIDE_DYE = 6
    """
    Setting to show/hide dyes from colored leather armor.
    """
    HIDE_ARMOR_TRIM = 7
    """
    Setting to show/hide armor trim from leather armor.
    """
