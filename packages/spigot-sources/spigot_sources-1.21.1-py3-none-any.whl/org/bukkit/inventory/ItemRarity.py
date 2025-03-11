"""
Python module generated from Java source file org.bukkit.inventory.ItemRarity

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.inventory import *
from typing import Any, Callable, Iterable, Tuple


class ItemRarity(Enum):
    """
    A item's rarity determines the default color of its name. This enum is
    ordered from least rare to most rare.
    """

    COMMON = 0
    """
    White item name.
    """
    UNCOMMON = 1
    """
    Yellow item name.
    """
    RARE = 2
    """
    Aqua item name.
    """
    EPIC = 3
    """
    Light purple item name.
    """
