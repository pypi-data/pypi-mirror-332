"""
Python module generated from Java source file org.bukkit.generator.LimitedRegion

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Location
from org.bukkit import RegionAccessor
from org.bukkit.block import BlockState
from org.bukkit.generator import *
from typing import Any, Callable, Iterable, Tuple


class LimitedRegion(RegionAccessor):
    """
    A limited region is used in world generation for features which are
    going over a chunk. For example, trees or ores.
    
    Use .getBuffer() to know how much you can go beyond the central
    chunk. The buffer zone may or may not be already populated.
    
    The coordinates are **absolute** from the world origin.
    """

    def getBuffer(self) -> int:
        """
        Gets the buffer around the central chunk which is accessible.
        The returned value is in normal world coordinate scale.
        
        For example: If the method returns 16 you have a working area of 48x48.

        Returns
        - The buffer in X and Z direction
        """
        ...


    def isInRegion(self, location: "Location") -> bool:
        """
        Checks if the given Location is in the region.

        Arguments
        - location: the location to check

        Returns
        - True if the location is in the region, otherwise False.
        """
        ...


    def isInRegion(self, x: int, y: int, z: int) -> bool:
        """
        Checks if the given coordinates are in the region.

        Arguments
        - x: X-coordinate to check
        - y: Y-coordinate to check
        - z: Z-coordinate to check

        Returns
        - True if the coordinates are in the region, otherwise False.
        """
        ...


    def getTileEntities(self) -> list["BlockState"]:
        """
        Gets a list of all tile entities in the limited region including the
        buffer zone.

        Returns
        - a list of tile entities.
        """
        ...
