"""
Python module generated from Java source file org.bukkit.material.Bed

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import *
from typing import Any, Callable, Iterable, Tuple


class Bed(MaterialData, Directional):
    """
    Represents a bed.

    Deprecated
    - all usage of MaterialData is deprecated and subject to removal.
    Use org.bukkit.block.data.BlockData.
    """

    def __init__(self):
        """
        Default constructor for a bed.
        """
        ...


    def __init__(self, direction: "BlockFace"):
        """
        Instantiate a bed facing in a particular direction.

        Arguments
        - direction: the direction the bed's head is facing
        """
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


    def isHeadOfBed(self) -> bool:
        """
        Determine if this block represents the head of the bed

        Returns
        - True if this is the head of the bed, False if it is the foot
        """
        ...


    def setHeadOfBed(self, isHeadOfBed: bool) -> None:
        """
        Configure this to be either the head or the foot of the bed

        Arguments
        - isHeadOfBed: True to make it the head.
        """
        ...


    def setFacingDirection(self, face: "BlockFace") -> None:
        """
        Set which direction the head of the bed is facing. Note that this will
        only affect one of the two blocks the bed is made of.
        """
        ...


    def getFacing(self) -> "BlockFace":
        """
        Get the direction that this bed's head is facing toward

        Returns
        - the direction the head of the bed is facing
        """
        ...


    def toString(self) -> str:
        ...


    def clone(self) -> "Bed":
        ...
