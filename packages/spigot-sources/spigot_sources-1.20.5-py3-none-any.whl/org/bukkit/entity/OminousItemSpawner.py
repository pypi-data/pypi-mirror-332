"""
Python module generated from Java source file org.bukkit.entity.OminousItemSpawner

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import MinecraftExperimental
from org.bukkit.MinecraftExperimental import Requires
from org.bukkit.entity import *
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class OminousItemSpawner(Entity):
    """
    Represents an ominous item spawner.
    """

    def getItem(self) -> "ItemStack":
        """
        Gets the item which will be spawned by this spawner.

        Returns
        - the item
        """
        ...


    def setItem(self, item: "ItemStack") -> None:
        """
        Sets the item which will be spawned by this spawner.

        Arguments
        - item: the item
        """
        ...


    def getSpawnItemAfterTicks(self) -> int:
        """
        Gets the ticks after which this item will be spawned.

        Returns
        - total spawn ticks
        """
        ...


    def setSpawnItemAfterTicks(self, ticks: int) -> None:
        """
        Sets the ticks after which this item will be spawned.

        Arguments
        - ticks: total spawn ticks
        """
        ...
