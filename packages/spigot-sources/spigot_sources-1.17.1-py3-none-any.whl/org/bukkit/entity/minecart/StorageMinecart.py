"""
Python module generated from Java source file org.bukkit.entity.minecart.StorageMinecart

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Minecart
from org.bukkit.entity.minecart import *
from org.bukkit.inventory import InventoryHolder
from org.bukkit.loot import Lootable
from typing import Any, Callable, Iterable, Tuple


class StorageMinecart(Minecart, InventoryHolder, Lootable):
    """
    Represents a minecart with a chest. These types of Minecart
    minecarts have their own inventory that can be accessed using methods
    from the InventoryHolder interface.
    """


