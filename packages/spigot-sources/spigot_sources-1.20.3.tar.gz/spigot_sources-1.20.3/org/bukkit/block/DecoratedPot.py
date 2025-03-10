"""
Python module generated from Java source file org.bukkit.block.DecoratedPot

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit import Material
from org.bukkit import Tag
from org.bukkit.block import *
from typing import Any, Callable, Iterable, Tuple


class DecoratedPot(TileState):
    """
    Represents a captured state of a decorated pot.
    """

    def setSherd(self, side: "Side", sherd: "Material") -> None:
        """
        Set the sherd on the provided side.

        Arguments
        - side: the side to set
        - sherd: the sherd, or null to set a blank side.

        Raises
        - IllegalArgumentException: if the sherd is not either
        tagged by Tag.ITEMS_DECORATED_POT_SHERDS, Material.BRICK,
        or `null`
        """
        ...


    def getSherd(self, side: "Side") -> "Material":
        """
        Get the sherd on the provided side.

        Arguments
        - side: the side to get

        Returns
        - the sherd on the side or Material.BRICK if it's blank
        """
        ...


    def getSherds(self) -> dict["Side", "Material"]:
        """
        Gets a Map of all sides on this decorated pot and the sherds on them.
        If a side does not have a specific sherd on it, Material.BRICK
        will be the value of that side.

        Returns
        - the sherds
        """
        ...


    def getShards(self) -> list["Material"]:
        """
        Gets the sherds on this decorated pot. For faces without a specific sherd,
        Material.BRICK is used in its place.

        Returns
        - the sherds

        Deprecated
        - in favor of .getSherds()
        """
        ...


    class Side(Enum):
        """
        A side on a decorated pot. Sides are relative to the facing state of a
        org.bukkit.block.data.type.DecoratedPot.
        """

        BACK = 0
        LEFT = 1
        RIGHT = 2
        FRONT = 3
