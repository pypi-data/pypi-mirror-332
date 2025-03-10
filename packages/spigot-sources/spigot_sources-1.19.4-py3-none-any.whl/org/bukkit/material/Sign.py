"""
Python module generated from Java source file org.bukkit.material.Sign

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import *
from typing import Any, Callable, Iterable, Tuple


class Sign(MaterialData, Attachable):
    """
    MaterialData for signs

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
        - type: the raw type id
        - data: the raw data value

        Deprecated
        - Magic value
        """
        ...


    def isWallSign(self) -> bool:
        """
        Check if this sign is attached to a wall

        Returns
        - True if this sign is attached to a wall, False if set on top of
            a block
        """
        ...


    def getAttachedFace(self) -> "BlockFace":
        """
        Gets the face that this block is attached on

        Returns
        - BlockFace attached to
        """
        ...


    def getFacing(self) -> "BlockFace":
        """
        Gets the direction that this sign is currently facing

        Returns
        - BlockFace indicating where this sign is facing
        """
        ...


    def setFacingDirection(self, face: "BlockFace") -> None:
        ...


    def toString(self) -> str:
        ...


    def clone(self) -> "Sign":
        ...
