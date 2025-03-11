"""
Python module generated from Java source file org.bukkit.block.data.type.Bed

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.block.data import Bisected
from org.bukkit.block.data import Directional
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class Bed(Directional):
    """
    Similar to Bisected, 'part' denotes which half of the bed this block
    corresponds to.
    
    'occupied' property is a quick flag to check if a player is currently
    sleeping in this bed block.
    """

    def getPart(self) -> "Part":
        """
        Gets the value of the 'part' property.

        Returns
        - the 'part' value
        """
        ...


    def setPart(self, part: "Part") -> None:
        """
        Sets the value of the 'part' property.

        Arguments
        - part: the new 'part' value
        """
        ...


    def isOccupied(self) -> bool:
        """
        Gets the value of the 'occupied' property.

        Returns
        - the 'occupied' value
        """
        ...


    class Part(Enum):
        """
        Horizontal half of a bed.
        """

        HEAD = 0
        """
        The head is the upper part of the bed containing the pillow.
        """
        FOOT = 1
        """
        The foot is the lower half of the bed.
        """
