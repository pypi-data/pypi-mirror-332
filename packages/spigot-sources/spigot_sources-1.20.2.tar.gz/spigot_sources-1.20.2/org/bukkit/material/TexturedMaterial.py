"""
Python module generated from Java source file org.bukkit.material.TexturedMaterial

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.material import *
from typing import Any, Callable, Iterable, Tuple


class TexturedMaterial(MaterialData):
    """
    Represents textured materials like steps and smooth bricks

    Deprecated
    - all usage of MaterialData is deprecated and subject to removal.
    Use org.bukkit.block.data.BlockData.
    """

    def __init__(self, m: "Material"):
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


    def getTextures(self) -> list["Material"]:
        """
        Retrieve a list of possible textures. The first element of the list
        will be used as a default.

        Returns
        - a list of possible textures for this block
        """
        ...


    def getMaterial(self) -> "Material":
        """
        Gets the current Material this block is made of

        Returns
        - Material of this block
        """
        ...


    def setMaterial(self, material: "Material") -> None:
        """
        Sets the material this block is made of

        Arguments
        - material: New material of this block
        """
        ...


    def toString(self) -> str:
        ...


    def clone(self) -> "TexturedMaterial":
        ...
