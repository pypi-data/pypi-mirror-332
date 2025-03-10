"""
Python module generated from Java source file org.bukkit.inventory.CreativeCategory

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.inventory import *
from typing import Any, Callable, Iterable, Tuple


class CreativeCategory(Enum):
    """
    Represents a category in the creative inventory.
    """

    BUILDING_BLOCKS = 0
    """
    An assortment of building blocks including dirt, bricks, planks, ores
    slabs, etc.
    """
    DECORATIONS = 1
    """
    Blocks and items typically used for decorative purposes including
    candles, saplings, flora, fauna, fences, walls, carpets, etc.
    """
    REDSTONE = 2
    """
    Blocks used and associated with redstone contraptions including buttons,
    levers, pressure plates, redstone components, pistons, etc.
    """
    TRANSPORTATION = 3
    """
    Items pertaining to transportation including minecarts, rails, boats,
    elytra, etc.
    """
    MISC = 4
    """
    Miscellaneous items and blocks that do not fit into other categories
    including gems, dyes, spawn eggs, discs, banner patterns, etc.
    """
    FOOD = 5
    """
    Food items consumable by the player including meats, berries, edible
    drops from creatures, etc.
    """
    TOOLS = 6
    """
    Equipment items meant for general utility including pickaxes, axes, hoes,
    flint and steel, and useful enchantment books for said tools.
    """
    COMBAT = 7
    """
    Equipment items meant for combat including armor, swords, bows, tipped
    arrows, and useful enchantment books for said equipment.
    """
    BREWING = 8
    """
    All items related to brewing and potions including all types of potions,
    their variants, and ingredients to brew them.
    """
