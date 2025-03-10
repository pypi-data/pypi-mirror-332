"""
Python module generated from Java source file org.bukkit.ChunkSnapshot

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import *
from org.bukkit.block import Biome
from org.bukkit.block.data import BlockData
from typing import Any, Callable, Iterable, Tuple


class ChunkSnapshot:
    """
    Represents a static, thread-safe snapshot of chunk of blocks.
    
    Purpose is to allow clean, efficient copy of a chunk data to be made, and
    then handed off for processing in another thread (e.g. map rendering)
    """

    def getX(self) -> int:
        """
        Gets the X-coordinate of this chunk

        Returns
        - X-coordinate
        """
        ...


    def getZ(self) -> int:
        """
        Gets the Z-coordinate of this chunk

        Returns
        - Z-coordinate
        """
        ...


    def getWorldName(self) -> str:
        """
        Gets name of the world containing this chunk

        Returns
        - Parent World Name
        """
        ...


    def getBlockType(self, x: int, y: int, z: int) -> "Material":
        """
        Get block type for block at corresponding coordinate in the chunk

        Arguments
        - x: 0-15
        - y: 0-255
        - z: 0-15

        Returns
        - block material type
        """
        ...


    def getBlockData(self, x: int, y: int, z: int) -> "BlockData":
        """
        Get block data for block at corresponding coordinate in the chunk

        Arguments
        - x: 0-15
        - y: 0-255
        - z: 0-15

        Returns
        - block material type
        """
        ...


    def getData(self, x: int, y: int, z: int) -> int:
        """
        Get block data for block at corresponding coordinate in the chunk

        Arguments
        - x: 0-15
        - y: 0-255
        - z: 0-15

        Returns
        - 0-15

        Deprecated
        - Magic value
        """
        ...


    def getBlockSkyLight(self, x: int, y: int, z: int) -> int:
        """
        Get sky light level for block at corresponding coordinate in the chunk

        Arguments
        - x: 0-15
        - y: 0-255
        - z: 0-15

        Returns
        - 0-15
        """
        ...


    def getBlockEmittedLight(self, x: int, y: int, z: int) -> int:
        """
        Get light level emitted by block at corresponding coordinate in the
        chunk

        Arguments
        - x: 0-15
        - y: 0-255
        - z: 0-15

        Returns
        - 0-15
        """
        ...


    def getHighestBlockYAt(self, x: int, z: int) -> int:
        """
        Gets the highest non-air coordinate at the given coordinates

        Arguments
        - x: X-coordinate of the blocks (0-15)
        - z: Z-coordinate of the blocks (0-15)

        Returns
        - Y-coordinate of the highest non-air block
        """
        ...


    def getBiome(self, x: int, z: int) -> "Biome":
        """
        Get biome at given coordinates

        Arguments
        - x: X-coordinate (0-15)
        - z: Z-coordinate (0-15)

        Returns
        - Biome at given coordinate

        Deprecated
        - biomes are now 3-dimensional
        """
        ...


    def getBiome(self, x: int, y: int, z: int) -> "Biome":
        """
        Get biome at given coordinates

        Arguments
        - x: X-coordinate (0-15)
        - y: Y-coordinate (0-255)
        - z: Z-coordinate (0-15)

        Returns
        - Biome at given coordinate
        """
        ...


    def getRawBiomeTemperature(self, x: int, z: int) -> float:
        """
        Get raw biome temperature at given coordinates

        Arguments
        - x: X-coordinate (0-15)
        - z: Z-coordinate (0-15)

        Returns
        - temperature at given coordinate

        Deprecated
        - biomes are now 3-dimensional
        """
        ...


    def getRawBiomeTemperature(self, x: int, y: int, z: int) -> float:
        """
        Get raw biome temperature at given coordinates

        Arguments
        - x: X-coordinate (0-15)
        - y: Y-coordinate (0-15)
        - z: Z-coordinate (0-15)

        Returns
        - temperature at given coordinate
        """
        ...


    def getCaptureFullTime(self) -> int:
        """
        Get world full time when chunk snapshot was captured

        Returns
        - time in ticks
        """
        ...


    def isSectionEmpty(self, sy: int) -> bool:
        """
        Test if section is empty

        Arguments
        - sy: - section Y coordinate (block Y / 16, 0-255)

        Returns
        - True if empty, False if not
        """
        ...


    def contains(self, block: "BlockData") -> bool:
        """
        Tests if this snapshot contains the specified block.

        Arguments
        - block: block to test

        Returns
        - if the block is contained within
        """
        ...
