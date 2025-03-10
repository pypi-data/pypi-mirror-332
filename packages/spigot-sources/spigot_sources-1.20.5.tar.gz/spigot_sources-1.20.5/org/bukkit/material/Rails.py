"""
Python module generated from Java source file org.bukkit.material.Rails

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import *
from typing import Any, Callable, Iterable, Tuple


class Rails(MaterialData):
    """
    Represents minecart rails.

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


    def isOnSlope(self) -> bool:
        """
        Returns
        - the whether this track is set on a slope
        """
        ...


    def isCurve(self) -> bool:
        """
        Returns
        - the whether this track is set as a curve
        """
        ...


    def getDirection(self) -> "BlockFace":
        """
        Returns
        - the direction these tracks are set
            
            Note that tracks are bidirectional and that the direction returned
            is the ascending direction if the track is set on a slope. If it is
            set as a curve, the corner of the track is returned.
        """
        ...


    def toString(self) -> str:
        ...


    def setDirection(self, face: "BlockFace", isOnSlope: bool) -> None:
        """
        Set the direction of these tracks
        
        Note that tracks are bidirectional and that the direction returned is
        the ascending direction if the track is set on a slope. If it is set as
        a curve, the corner of the track should be supplied.

        Arguments
        - face: the direction the track should be facing
        - isOnSlope: whether or not the track should be on a slope
        """
        ...


    def clone(self) -> "Rails":
        ...
