"""
Python module generated from Java source file org.bukkit.block.data.type.Slab

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.block.data import Waterlogged
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class Slab(Waterlogged):
    """
    'type' represents what state the slab is in - either top, bottom, or a double
    slab occupying the full block.
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
        The type of the slab.
        """

        TOP = 0
        """
        The slab occupies the upper y half of the block.
        """
        BOTTOM = 1
        """
        The slab occupies the lower y half of the block.
        """
        DOUBLE = 2
        """
        The slab occupies the entire block.
        """
