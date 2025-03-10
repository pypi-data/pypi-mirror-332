"""
Python module generated from Java source file org.bukkit.block.data.type.Jigsaw

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.block.data import BlockData
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class Jigsaw(BlockData):
    """
    'orientation' is the direction the block is facing.
    """

    def getOrientation(self) -> "Orientation":
        """
        Gets the value of the 'orientation' property.

        Returns
        - the 'orientation' value
        """
        ...


    def setOrientation(self, orientation: "Orientation") -> None:
        """
        Sets the value of the 'orientation' property.

        Arguments
        - orientation: the new 'orientation' value
        """
        ...


    class Orientation(Enum):
        """
        The directions the Jigsaw can be oriented.
        """

        DOWN_EAST = 0
        DOWN_NORTH = 1
        DOWN_SOUTH = 2
        DOWN_WEST = 3
        UP_EAST = 4
        UP_NORTH = 5
        UP_SOUTH = 6
        UP_WEST = 7
        WEST_UP = 8
        EAST_UP = 9
        NORTH_UP = 10
        SOUTH_UP = 11
