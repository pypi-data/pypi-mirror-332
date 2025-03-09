"""
Python module generated from Java source file org.bukkit.inventory.LecternInventory

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Lectern
from org.bukkit.inventory import *
from typing import Any, Callable, Iterable, Tuple


class LecternInventory(Inventory):
    """
    Interface to the inventory of a Lectern.
    """

    def getHolder(self) -> "Lectern":
        ...
