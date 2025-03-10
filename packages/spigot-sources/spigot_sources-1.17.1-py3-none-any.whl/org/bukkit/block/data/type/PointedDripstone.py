"""
Python module generated from Java source file org.bukkit.block.data.type.PointedDripstone

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.block import BlockFace
from org.bukkit.block.data import Waterlogged
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class PointedDripstone(Waterlogged):
    """
    'thickness' represents the dripstone thickness.
    
    'vertical_direction' represents the dripstone orientation.
    
    Some blocks may not be able to face in all directions, use
    .getVerticalDirections() to get all possible directions for this
    block.
    """

    def getVerticalDirection(self) -> "BlockFace":
        """
        Gets the value of the 'vertical_direction' property.

        Returns
        - the 'vertical_direction' value
        """
        ...


    def setVerticalDirection(self, direction: "BlockFace") -> None:
        """
        Sets the value of the 'vertical_direction' property.

        Arguments
        - direction: the new 'vertical_direction' value
        """
        ...


    def getVerticalDirections(self) -> set["BlockFace"]:
        """
        Gets the faces which are applicable to this block.

        Returns
        - the allowed 'vertical_direction' values
        """
        ...


    def getThickness(self) -> "Thickness":
        """
        Gets the value of the 'thickness' property.

        Returns
        - the 'thickness' value
        """
        ...


    def setThickness(self, thickness: "Thickness") -> None:
        """
        Sets the value of the 'thickness' property.

        Arguments
        - thickness: the new 'thickness' value
        """
        ...


    class Thickness(Enum):
        """
        Represents the thickness of the dripstone, corresponding to its position
        within a multi-block dripstone formation.
        """

        TIP_MERGE = 0
        """
        Extended tip.
        """
        TIP = 1
        """
        Just the tip.
        """
        FRUSTUM = 2
        """
        Top section.
        """
        MIDDLE = 3
        """
        Middle section.
        """
        BASE = 4
        """
        Base.
        """
