"""
Python module generated from Java source file org.bukkit.material.types.MushroomBlockTexture

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import Maps
from enum import Enum
from org.bukkit.block import BlockFace
from org.bukkit.material.types import *
from typing import Any, Callable, Iterable, Tuple


class MushroomBlockTexture(Enum):
    """
    Represents the different textured blocks of mushroom.
    """

    ALL_PORES = (0, None)
    """
    Pores on all faces.
    """
    CAP_NORTH_WEST = (1, BlockFace.NORTH_WEST)
    """
    Cap texture on the top, north and west faces, pores on remaining sides.
    """
    CAP_NORTH = (2, BlockFace.NORTH)
    """
    Cap texture on the top and north faces, pores on remaining sides.
    """
    CAP_NORTH_EAST = (3, BlockFace.NORTH_EAST)
    """
    Cap texture on the top, north and east faces, pores on remaining sides.
    """
    CAP_WEST = (4, BlockFace.WEST)
    """
    Cap texture on the top and west faces, pores on remaining sides.
    """
    CAP_TOP = (5, BlockFace.UP)
    """
    Cap texture on the top face, pores on remaining sides.
    """
    CAP_EAST = (6, BlockFace.EAST)
    """
    Cap texture on the top and east faces, pores on remaining sides.
    """
    CAP_SOUTH_WEST = (7, BlockFace.SOUTH_WEST)
    """
    Cap texture on the top, south and west faces, pores on remaining sides.
    """
    CAP_SOUTH = (8, BlockFace.SOUTH)
    """
    Cap texture on the top and south faces, pores on remaining sides.
    """
    CAP_SOUTH_EAST = (9, BlockFace.SOUTH_EAST)
    """
    Cap texture on the top, south and east faces, pores on remaining sides.
    """
    STEM_SIDES = (10, None)
    """
    Stem texture on the north, east, south and west faces, pores on top and
    bottom.
    """
    ALL_CAP = (14, BlockFace.SELF)
    """
    Cap texture on all faces.
    """
    ALL_STEM = (15, None)
    """
    Stem texture on all faces.
    """


    def getData(self) -> int:
        """
        Gets the associated data value representing this mushroom block face.

        Returns
        - A byte containing the data value of this mushroom block face

        Deprecated
        - Magic value
        """
        ...


    def getCapFace(self) -> "BlockFace":
        """
        Gets the face that has cap texture.

        Returns
        - The cap face
        """
        ...


    @staticmethod
    def getByData(data: int) -> "MushroomBlockTexture":
        """
        Gets the MushroomBlockType with the given data value.

        Arguments
        - data: Data value to fetch

        Returns
        - The MushroomBlockTexture representing the given value, or
        null if it doesn't exist

        Deprecated
        - Magic value
        """
        ...


    @staticmethod
    def getCapByFace(face: "BlockFace") -> "MushroomBlockTexture":
        """
        Gets the MushroomBlockType with cap texture on the given block face.

        Arguments
        - face: the required block face with cap texture

        Returns
        - The MushroomBlockTexture representing the given block
        face, or null if it doesn't exist

        See
        - BlockFace
        """
        ...
