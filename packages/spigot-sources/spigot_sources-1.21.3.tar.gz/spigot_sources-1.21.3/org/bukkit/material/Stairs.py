"""
Python module generated from Java source file org.bukkit.material.Stairs

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import *
from typing import Any, Callable, Iterable, Tuple


class Stairs(MaterialData, Directional):
    """
    Represents stairs.

    Deprecated
    - all usage of MaterialData is deprecated and subject to removal.
    Use org.bukkit.block.data.BlockData.
    """

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


    def getAscendingDirection(self) -> "BlockFace":
        """
        Returns
        - the direction the stairs ascend towards
        """
        ...


    def getDescendingDirection(self) -> "BlockFace":
        """
        Returns
        - the direction the stairs descend towards
        """
        ...


    def setFacingDirection(self, face: "BlockFace") -> None:
        """
        Set the direction the stair part of the block is facing
        """
        ...


    def getFacing(self) -> "BlockFace":
        """
        Returns
        - the direction the stair part of the block is facing
        """
        ...


    def isInverted(self) -> bool:
        """
        Test if step is inverted

        Returns
        - True if inverted (top half), False if normal (bottom half)
        """
        ...


    def setInverted(self, inv: bool) -> None:
        """
        Set step inverted state

        Arguments
        - inv: - True if step is inverted (top half), False if step is
            normal (bottom half)
        """
        ...


    def toString(self) -> str:
        ...


    def clone(self) -> "Stairs":
        ...
