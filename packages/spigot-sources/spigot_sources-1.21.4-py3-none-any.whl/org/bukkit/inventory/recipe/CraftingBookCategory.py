"""
Python module generated from Java source file org.bukkit.inventory.recipe.CraftingBookCategory

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.inventory.recipe import *
from typing import Any, Callable, Iterable, Tuple


class CraftingBookCategory(Enum):
    """
    Represents categories within the crafting recipe book.
    """

    BUILDING = 0
    REDSTONE = 1
    EQUIPMENT = 2
    MISC = 3
