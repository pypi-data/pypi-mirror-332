"""
Python module generated from Java source file org.bukkit.inventory.meta.BundleMeta

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import MinecraftExperimental
from org.bukkit.inventory import ItemStack
from org.bukkit.inventory.meta import *
from typing import Any, Callable, Iterable, Tuple


class BundleMeta(ItemMeta):

    def hasItems(self) -> bool:
        """
        Returns whether the item has any items.

        Returns
        - whether items are present
        """
        ...


    def getItems(self) -> list["ItemStack"]:
        """
        Returns an immutable list of the items stored in this item.

        Returns
        - items
        """
        ...


    def setItems(self, items: list["ItemStack"]) -> None:
        """
        Sets the items stored in this item.
        
        Removes all items when given null.

        Arguments
        - items: the items to set
        """
        ...


    def addItem(self, item: "ItemStack") -> None:
        """
        Adds an item to this item.

        Arguments
        - item: item to add
        """
        ...
