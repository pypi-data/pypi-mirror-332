"""
Python module generated from Java source file org.bukkit.material.Comparator

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import *
from typing import Any, Callable, Iterable, Tuple


class Comparator(MaterialData, Directional, Redstone):
    """
    Represents a comparator in the on or off state, in normal or subtraction mode and facing in a specific direction.

    See
    - Material.LEGACY_REDSTONE_COMPARATOR_ON

    Deprecated
    - all usage of MaterialData is deprecated and subject to removal.
    Use org.bukkit.block.data.BlockData.
    """

    def __init__(self):
        """
        Constructs a comparator switched off, with the default mode (normal) and facing the default direction (north).
        """
        ...


    def __init__(self, facingDirection: "BlockFace"):
        """
        Constructs a comparator switched off, with the default mode (normal) and facing the specified direction.

        Arguments
        - facingDirection: the direction the comparator is facing

        See
        - BlockFace
        """
        ...


    def __init__(self, facingDirection: "BlockFace", isSubtraction: bool):
        """
        Constructs a comparator switched off, with the specified mode and facing the specified direction.

        Arguments
        - facingDirection: the direction the comparator is facing
        - isSubtraction: True if the comparator is in subtraction mode, False for normal comparator operation

        See
        - BlockFace
        """
        ...


    def __init__(self, facingDirection: "BlockFace", isSubtraction: bool, state: bool):
        """
        Constructs a comparator switched on or off, with the specified mode and facing the specified direction.

        Arguments
        - facingDirection: the direction the comparator is facing
        - isSubtraction: True if the comparator is in subtraction mode, False for normal comparator operation
        - state: True if the comparator is in the on state

        See
        - BlockFace
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


    def setSubtractionMode(self, isSubtraction: bool) -> None:
        """
        Sets whether the comparator is in subtraction mode.

        Arguments
        - isSubtraction: True if the comparator is in subtraction mode, False for normal comparator operation
        """
        ...


    def isSubtractionMode(self) -> bool:
        """
        Checks whether the comparator is in subtraction mode

        Returns
        - True if the comparator is in subtraction mode, False if normal comparator operation
        """
        ...


    def setFacingDirection(self, face: "BlockFace") -> None:
        """
        Sets the direction this comparator is facing

        Arguments
        - face: The direction to set this comparator to

        See
        - BlockFace
        """
        ...


    def getFacing(self) -> "BlockFace":
        """
        Gets the direction this comparator is facing

        Returns
        - The direction this comparator is facing

        See
        - BlockFace
        """
        ...


    def toString(self) -> str:
        ...


    def clone(self) -> "Comparator":
        ...


    def isPowered(self) -> bool:
        """
        Checks if the comparator is powered

        Returns
        - True if the comparator is powered
        """
        ...


    def isBeingPowered(self) -> bool:
        """
        Checks if the comparator is being powered

        Returns
        - True if the comparator is being powered
        """
        ...
