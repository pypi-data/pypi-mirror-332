"""
Python module generated from Java source file org.bukkit.block.BlockFace

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.block import *
from org.bukkit.util import Vector
from typing import Any, Callable, Iterable, Tuple


class BlockFace(Enum):
    """
    Represents the face of a block
    """

    NORTH = (0, 0, -1)
    EAST = (1, 0, 0)
    SOUTH = (0, 0, 1)
    WEST = (-1, 0, 0)
    UP = (0, 1, 0)
    DOWN = (0, -1, 0)
    NORTH_EAST = (NORTH, EAST)
    NORTH_WEST = (NORTH, WEST)
    SOUTH_EAST = (SOUTH, EAST)
    SOUTH_WEST = (SOUTH, WEST)
    WEST_NORTH_WEST = (WEST, NORTH_WEST)
    NORTH_NORTH_WEST = (NORTH, NORTH_WEST)
    NORTH_NORTH_EAST = (NORTH, NORTH_EAST)
    EAST_NORTH_EAST = (EAST, NORTH_EAST)
    EAST_SOUTH_EAST = (EAST, SOUTH_EAST)
    SOUTH_SOUTH_EAST = (SOUTH, SOUTH_EAST)
    SOUTH_SOUTH_WEST = (SOUTH, SOUTH_WEST)
    WEST_SOUTH_WEST = (WEST, SOUTH_WEST)
    SELF = (0, 0, 0)


    def getModX(self) -> int:
        """
        Get the amount of X-coordinates to modify to get the represented block

        Returns
        - Amount of X-coordinates to modify
        """
        ...


    def getModY(self) -> int:
        """
        Get the amount of Y-coordinates to modify to get the represented block

        Returns
        - Amount of Y-coordinates to modify
        """
        ...


    def getModZ(self) -> int:
        """
        Get the amount of Z-coordinates to modify to get the represented block

        Returns
        - Amount of Z-coordinates to modify
        """
        ...


    def getDirection(self) -> "Vector":
        """
        Gets the normal vector corresponding to this block face.

        Returns
        - the normal vector
        """
        ...


    def isCartesian(self) -> bool:
        """
        Returns True if this face is aligned with one of the unit axes in 3D
        Cartesian space (ie NORTH, SOUTH, EAST, WEST, UP, DOWN).

        Returns
        - Cartesian status
        """
        ...


    def getOppositeFace(self) -> "BlockFace":
        ...
