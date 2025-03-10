"""
Python module generated from Java source file org.bukkit.material.FlowerPot

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import GrassSpecies
from org.bukkit import Material
from org.bukkit import TreeSpecies
from org.bukkit.material import *
from typing import Any, Callable, Iterable, Tuple


class FlowerPot(MaterialData):
    """
    Represents a flower pot.

    Deprecated
    - all usage of MaterialData is deprecated and subject to removal.
    Use org.bukkit.block.data.BlockData.
    """

    def __init__(self):
        """
        Default constructor for a flower pot.
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


    def getContents(self) -> "MaterialData":
        """
        Get the material in the flower pot

        Returns
        - material MaterialData for the block currently in the flower pot
            or null if empty
        """
        ...


    def setContents(self, materialData: "MaterialData") -> None:
        """
        Set the contents of the flower pot

        Arguments
        - materialData: MaterialData of the block to put in the flower pot.
        """
        ...


    def toString(self) -> str:
        ...


    def clone(self) -> "FlowerPot":
        ...
