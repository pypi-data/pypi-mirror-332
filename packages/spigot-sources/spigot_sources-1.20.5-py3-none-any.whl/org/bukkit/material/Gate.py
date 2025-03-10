"""
Python module generated from Java source file org.bukkit.material.Gate

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import *
from typing import Any, Callable, Iterable, Tuple


class Gate(MaterialData, Directional, Openable):
    """
    Represents a fence gate

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


    def __init__(self, data: int):
        ...


    def setFacingDirection(self, face: "BlockFace") -> None:
        ...


    def getFacing(self) -> "BlockFace":
        ...


    def isOpen(self) -> bool:
        ...


    def setOpen(self, isOpen: bool) -> None:
        ...


    def toString(self) -> str:
        ...


    def clone(self) -> "Gate":
        ...
