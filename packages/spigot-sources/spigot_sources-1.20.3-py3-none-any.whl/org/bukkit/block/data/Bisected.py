"""
Python module generated from Java source file org.bukkit.block.data.Bisected

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.block.data import *
from typing import Any, Callable, Iterable, Tuple


class Bisected(BlockData):
    """
    'half' denotes which half of a two block tall material this block is.
    
    In game it may be referred to as either (top, bottom) or (upper, lower).
    """

    def getHalf(self) -> "Half":
        """
        Gets the value of the 'half' property.

        Returns
        - the 'half' value
        """
        ...


    def setHalf(self, half: "Half") -> None:
        """
        Sets the value of the 'half' property.

        Arguments
        - half: the new 'half' value
        """
        ...


    class Half(Enum):
        """
        The half of a vertically bisected block.
        """

        TOP = 0
        """
        The top half of the block, normally with the higher y coordinate.
        """
        BOTTOM = 1
        """
        The bottom half of the block, normally with the lower y coordinate.
        """
