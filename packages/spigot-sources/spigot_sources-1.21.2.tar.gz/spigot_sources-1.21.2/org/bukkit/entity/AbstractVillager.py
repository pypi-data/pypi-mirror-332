"""
Python module generated from Java source file org.bukkit.entity.AbstractVillager

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from org.bukkit.inventory import Inventory
from org.bukkit.inventory import InventoryHolder
from org.bukkit.inventory import Merchant
from typing import Any, Callable, Iterable, Tuple


class AbstractVillager(Breedable, NPC, InventoryHolder, Merchant):
    """
    Represents a villager NPC
    """

    def getInventory(self) -> "Inventory":
        """
        Gets this villager's inventory.
        
        Note that this inventory is not the Merchant inventory, rather, it is the
        items that a villager might have collected (from harvesting crops, etc.)
        
        """
        ...
