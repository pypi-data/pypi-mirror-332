"""
Python module generated from Java source file org.bukkit.entity.ItemDisplay

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.entity import *
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class ItemDisplay(Display):
    """
    Represents an item display entity.
    """

    def getItemStack(self) -> "ItemStack":
        """
        Gets the displayed item stack.

        Returns
        - the displayed item stack
        """
        ...


    def setItemStack(self, item: "ItemStack") -> None:
        """
        Sets the displayed item stack.

        Arguments
        - item: the new item stack
        """
        ...


    def getItemDisplayTransform(self) -> "ItemDisplayTransform":
        """
        Gets the item display transform for this entity.
        
        Defaults to ItemDisplayTransform.FIXED.

        Returns
        - item display transform
        """
        ...


    def setItemDisplayTransform(self, display: "ItemDisplayTransform") -> None:
        """
        Sets the item display transform for this entity.
        
        Defaults to ItemDisplayTransform.FIXED.

        Arguments
        - display: new display
        """
        ...


    class ItemDisplayTransform(Enum):
        """
        Represents the item model transform to be applied to the displayed item.
        """

        NONE = 0
        THIRDPERSON_LEFTHAND = 1
        THIRDPERSON_RIGHTHAND = 2
        FIRSTPERSON_LEFTHAND = 3
        FIRSTPERSON_RIGHTHAND = 4
        HEAD = 5
        GUI = 6
        GROUND = 7
        FIXED = 8
