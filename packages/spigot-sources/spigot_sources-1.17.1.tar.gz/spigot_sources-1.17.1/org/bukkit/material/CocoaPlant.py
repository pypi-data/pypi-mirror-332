"""
Python module generated from Java source file org.bukkit.material.CocoaPlant

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import *
from typing import Any, Callable, Iterable, Tuple


class CocoaPlant(MaterialData, Directional, Attachable):
    """
    Represents the cocoa plant

    Deprecated
    - all usage of MaterialData is deprecated and subject to removal.
    Use org.bukkit.block.data.BlockData.
    """

    def __init__(self):
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


    def __init__(self, sz: "CocoaPlantSize"):
        ...


    def __init__(self, sz: "CocoaPlantSize", dir: "BlockFace"):
        ...


    def getSize(self) -> "CocoaPlantSize":
        """
        Get size of plant

        Returns
        - size
        """
        ...


    def setSize(self, sz: "CocoaPlantSize") -> None:
        """
        Set size of plant

        Arguments
        - sz: - size of plant
        """
        ...


    def getAttachedFace(self) -> "BlockFace":
        ...


    def setFacingDirection(self, face: "BlockFace") -> None:
        ...


    def getFacing(self) -> "BlockFace":
        ...


    def clone(self) -> "CocoaPlant":
        ...


    def toString(self) -> str:
        ...


    class CocoaPlantSize(Enum):

        SMALL = 0
        MEDIUM = 1
        LARGE = 2
