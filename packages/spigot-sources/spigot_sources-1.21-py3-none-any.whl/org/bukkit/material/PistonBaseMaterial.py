"""
Python module generated from Java source file org.bukkit.material.PistonBaseMaterial

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import *
from typing import Any, Callable, Iterable, Tuple


class PistonBaseMaterial(MaterialData, Directional, Redstone):
    """
    Material data for the piston base block

    Deprecated
    - all usage of MaterialData is deprecated and subject to removal.
    Use org.bukkit.block.data.BlockData.
    """

    def __init__(self, type: "Material"):
        ...


    def __init__(self, type: "Material", data: int):
        """
        Constructs a PistonBaseMaterial.

        Arguments
        - type: the material type to use
        - data: the raw data value

        Deprecated
        - Magic value
        """
        ...


    def setFacingDirection(self, face: "BlockFace") -> None:
        ...


    def getFacing(self) -> "BlockFace":
        ...


    def isPowered(self) -> bool:
        ...


    def setPowered(self, powered: bool) -> None:
        """
        Sets the current state of this piston

        Arguments
        - powered: True if the piston is extended & powered, or False
        """
        ...


    def isSticky(self) -> bool:
        """
        Checks if this piston base is sticky, and returns True if so

        Returns
        - True if this piston is "sticky", or False
        """
        ...


    def clone(self) -> "PistonBaseMaterial":
        ...
