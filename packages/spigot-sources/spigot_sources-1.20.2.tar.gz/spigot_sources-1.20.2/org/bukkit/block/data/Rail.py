"""
Python module generated from Java source file org.bukkit.block.data.Rail

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.block.data import *
from typing import Any, Callable, Iterable, Tuple


class Rail(Waterlogged):
    """
    'shape' represents the current layout of a minecart rail.
    
    Some types of rail may not be able to be laid out in all shapes, use
    .getShapes() to get those applicable to this block.
    """

    def getShape(self) -> "Shape":
        """
        Gets the value of the 'shape' property.

        Returns
        - the 'shape' value
        """
        ...


    def setShape(self, shape: "Shape") -> None:
        """
        Sets the value of the 'shape' property.

        Arguments
        - shape: the new 'shape' value
        """
        ...


    def getShapes(self) -> set["Shape"]:
        """
        Gets the shapes which are applicable to this block.

        Returns
        - the allowed 'shape' values
        """
        ...


    class Shape(Enum):
        """
        The different types of shapes a rail block can occupy.
        """

        NORTH_SOUTH = 0
        """
        The rail runs flat along the north/south (Z) axis.
        """
        EAST_WEST = 1
        """
        The rail runs flat along the east/west (X) axis.
        """
        ASCENDING_EAST = 2
        """
        The rail ascends in the east (positive X) direction.
        """
        ASCENDING_WEST = 3
        """
        The rail ascends in the west (negative X) direction.
        """
        ASCENDING_NORTH = 4
        """
        The rail ascends in the north (negative Z) direction.
        """
        ASCENDING_SOUTH = 5
        """
        The rail ascends in the south (positive Z) direction.
        """
        SOUTH_EAST = 6
        """
        The rail forms a curve connecting the south and east faces of the
        block.
        """
        SOUTH_WEST = 7
        """
        The rail forms a curve connecting the south and west faces of the
        block.
        """
        NORTH_WEST = 8
        """
        The rail forms a curve connecting the north and west faces of the
        block.
        """
        NORTH_EAST = 9
        """
        The rail forms a curve connecting the north and east faces of the
        block.
        """
