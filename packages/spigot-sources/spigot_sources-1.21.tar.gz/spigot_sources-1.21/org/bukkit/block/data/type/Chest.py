"""
Python module generated from Java source file org.bukkit.block.data.type.Chest

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.block.data import Directional
from org.bukkit.block.data import Waterlogged
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class Chest(Directional, Waterlogged):
    """
    'type' represents which part of a double chest this block is, or if it is a
    single chest.
    """

    def getType(self) -> "Type":
        """
        Gets the value of the 'type' property.

        Returns
        - the 'type' value
        """
        ...


    def setType(self, type: "Type") -> None:
        """
        Sets the value of the 'type' property.

        Arguments
        - type: the new 'type' value
        """
        ...


    class Type(Enum):
        """
        Type of this chest block.
        
        NB: Left and right are relative to the chest itself, i.e opposite to what
        a player placing the appropriate block would see.
        """

        SINGLE = 0
        """
        The chest is not linked to any others and contains only one 27 slot
        inventory.
        """
        LEFT = 1
        """
        The chest is the left hand side of a double chest and shares a 54
        block inventory with the chest to its right.
        """
        RIGHT = 2
        """
        The chest is the right hand side of a double chest and shares a 54
        block inventory with the chest to its left.
        """
