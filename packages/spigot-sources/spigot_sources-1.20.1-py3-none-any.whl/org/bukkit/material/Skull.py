"""
Python module generated from Java source file org.bukkit.material.Skull

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import *
from typing import Any, Callable, Iterable, Tuple


class Skull(MaterialData, Directional):
    """
    Represents a skull.

    Deprecated
    - all usage of MaterialData is deprecated and subject to removal.
    Use org.bukkit.block.data.BlockData.
    """

    def __init__(self):
        ...


    def __init__(self, direction: "BlockFace"):
        """
        Instantiate a skull facing in a particular direction.

        Arguments
        - direction: the direction the skull's face is facing
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


    def setFacingDirection(self, face: "BlockFace") -> None:
        ...


    def getFacing(self) -> "BlockFace":
        ...


    def toString(self) -> str:
        ...


    def clone(self) -> "Skull":
        ...
