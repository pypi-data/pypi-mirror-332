"""
Python module generated from Java source file org.bukkit.block.DoubleChest

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Location
from org.bukkit import World
from org.bukkit.block import *
from org.bukkit.inventory import DoubleChestInventory
from org.bukkit.inventory import Inventory
from org.bukkit.inventory import InventoryHolder
from typing import Any, Callable, Iterable, Tuple


class DoubleChest(InventoryHolder):
    """
    Represents a double chest.
    """

    def __init__(self, chest: "DoubleChestInventory"):
        ...


    def getInventory(self) -> "Inventory":
        ...


    def getLeftSide(self) -> "InventoryHolder":
        ...


    def getRightSide(self) -> "InventoryHolder":
        ...


    def getLocation(self) -> "Location":
        ...


    def getWorld(self) -> "World":
        ...


    def getX(self) -> float:
        ...


    def getY(self) -> float:
        ...


    def getZ(self) -> float:
        ...
