"""
Python module generated from Java source file org.bukkit.inventory.ChiseledBookshelfInventory

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import MinecraftExperimental
from org.bukkit.block import ChiseledBookshelf
from org.bukkit.inventory import *
from typing import Any, Callable, Iterable, Tuple


class ChiseledBookshelfInventory(Inventory):
    """
    Interface to the inventory of a chiseled bookshelf.
    """

    def getHolder(self) -> "ChiseledBookshelf":
        ...
