"""
Python module generated from Java source file org.bukkit.block.data.type.Stairs

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.block.data import Bisected
from org.bukkit.block.data import Directional
from org.bukkit.block.data import Waterlogged
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class Stairs(Bisected, Directional, Waterlogged):
    """
    'shape' represents the texture and bounding box shape of these stairs.
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


    class Shape(Enum):
        """
        The shape of a stair block - used for constructing corners.
        """

        STRAIGHT = 0
        """
        Regular stair block.
        """
        INNER_LEFT = 1
        """
        Inner corner stair block with higher left side.
        """
        INNER_RIGHT = 2
        """
        Inner corner stair block with higher right side.
        """
        OUTER_LEFT = 3
        """
        Outer corner stair block with higher left side.
        """
        OUTER_RIGHT = 4
        """
        Outer corner stair block with higher right side.
        """
