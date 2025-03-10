"""
Python module generated from Java source file org.bukkit.material.Lever

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import *
from typing import Any, Callable, Iterable, Tuple


class Lever(SimpleAttachableMaterialData, Redstone):
    """
    Represents a lever

    Deprecated
    - all usage of MaterialData is deprecated and subject to removal.
    Use org.bukkit.block.data.BlockData.
    """

    def __init__(self):
        ...


    def __init__(self, type: "Material"):
        ...


    def __init__(self, type: "Material", data: int):
        """
        Arguments
        - type: the type
        - data: the raw data value

        Deprecated
        - Magic value
        """
        ...


    def isPowered(self) -> bool:
        """
        Gets the current state of this Material, indicating if it's powered or
        unpowered

        Returns
        - True if powered, otherwise False
        """
        ...


    def setPowered(self, isPowered: bool) -> None:
        """
        Set this lever to be powered or not.

        Arguments
        - isPowered: whether the lever should be powered or not
        """
        ...


    def getAttachedFace(self) -> "BlockFace":
        """
        Gets the face that this block is attached on

        Returns
        - BlockFace attached to
        """
        ...


    def setFacingDirection(self, face: "BlockFace") -> None:
        """
        Sets the direction this lever is pointing in
        """
        ...


    def toString(self) -> str:
        ...


    def clone(self) -> "Lever":
        ...
