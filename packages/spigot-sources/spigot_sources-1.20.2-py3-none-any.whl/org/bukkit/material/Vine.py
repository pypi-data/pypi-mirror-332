"""
Python module generated from Java source file org.bukkit.material.Vine

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Arrays
from java.util import EnumSet
from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import *
from typing import Any, Callable, Iterable, Tuple


class Vine(MaterialData):
    """
    Represents a vine

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
        """
        Arguments
        - data: the raw data value

        Deprecated
        - Magic value
        """
        ...


    def __init__(self, *faces: Tuple["BlockFace", ...]):
        ...


    def __init__(self, faces: "EnumSet"["BlockFace"]):
        ...


    def isOnFace(self, face: "BlockFace") -> bool:
        """
        Check if the vine is attached to the specified face of an adjacent
        block. You can check two faces at once by passing e.g. BlockFace.NORTH_EAST.

        Arguments
        - face: The face to check.

        Returns
        - Whether it is attached to that face.
        """
        ...


    def putOnFace(self, face: "BlockFace") -> None:
        """
        Attach the vine to the specified face of an adjacent block.

        Arguments
        - face: The face to attach.
        """
        ...


    def removeFromFace(self, face: "BlockFace") -> None:
        """
        Detach the vine from the specified face of an adjacent block.

        Arguments
        - face: The face to detach.
        """
        ...


    def toString(self) -> str:
        ...


    def clone(self) -> "Vine":
        ...
