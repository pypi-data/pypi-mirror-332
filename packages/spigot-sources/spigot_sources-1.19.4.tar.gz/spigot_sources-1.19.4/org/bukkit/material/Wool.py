"""
Python module generated from Java source file org.bukkit.material.Wool

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import DyeColor
from org.bukkit import Material
from org.bukkit.material import *
from typing import Any, Callable, Iterable, Tuple


class Wool(MaterialData, Colorable):
    """
    Represents a Wool/Cloth block

    Deprecated
    - all usage of MaterialData is deprecated and subject to removal.
    Use org.bukkit.block.data.BlockData.
    """

    def __init__(self):
        ...


    def __init__(self, color: "DyeColor"):
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


    def getColor(self) -> "DyeColor":
        """
        Gets the current color of this dye

        Returns
        - DyeColor of this dye
        """
        ...


    def setColor(self, color: "DyeColor") -> None:
        """
        Sets the color of this dye

        Arguments
        - color: New color of this dye
        """
        ...


    def toString(self) -> str:
        ...


    def clone(self) -> "Wool":
        ...
