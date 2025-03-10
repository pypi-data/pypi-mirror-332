"""
Python module generated from Java source file org.bukkit.material.TrapDoor

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import *
from typing import Any, Callable, Iterable, Tuple


class TrapDoor(SimpleAttachableMaterialData, Openable):
    """
    Represents a trap door

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
        - type: the type
        - data: the raw data value

        Deprecated
        - Magic value
        """
        ...


    def isOpen(self) -> bool:
        ...


    def setOpen(self, isOpen: bool) -> None:
        ...


    def isInverted(self) -> bool:
        """
        Test if trapdoor is inverted

        Returns
        - True if inverted (top half), False if normal (bottom half)
        """
        ...


    def setInverted(self, inv: bool) -> None:
        """
        Set trapdoor inverted state

        Arguments
        - inv: - True if inverted (top half), False if normal (bottom half)
        """
        ...


    def getAttachedFace(self) -> "BlockFace":
        ...


    def setFacingDirection(self, face: "BlockFace") -> None:
        ...


    def toString(self) -> str:
        ...


    def clone(self) -> "TrapDoor":
        ...
