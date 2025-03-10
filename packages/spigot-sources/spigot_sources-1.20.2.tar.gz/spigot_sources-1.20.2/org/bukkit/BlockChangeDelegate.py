"""
Python module generated from Java source file org.bukkit.BlockChangeDelegate

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import *
from org.bukkit.block.data import BlockData
from typing import Any, Callable, Iterable, Tuple


class BlockChangeDelegate:
    """
    A delegate for handling block changes. This serves as a direct interface
    between generation algorithms in the server implementation and utilizing
    code.
    """

    def setBlockData(self, x: int, y: int, z: int, blockData: "BlockData") -> bool:
        """
        Set a block data at the specified coordinates.

        Arguments
        - x: X coordinate
        - y: Y coordinate
        - z: Z coordinate
        - blockData: Block data

        Returns
        - True if the block was set successfully
        """
        ...


    def getBlockData(self, x: int, y: int, z: int) -> "BlockData":
        """
        Get the block data at the location.

        Arguments
        - x: X coordinate
        - y: Y coordinate
        - z: Z coordinate

        Returns
        - The block data
        """
        ...


    def getHeight(self) -> int:
        """
        Gets the height of the world.

        Returns
        - Height of the world
        """
        ...


    def isEmpty(self, x: int, y: int, z: int) -> bool:
        """
        Checks if the specified block is empty (air) or not.

        Arguments
        - x: X coordinate
        - y: Y coordinate
        - z: Z coordinate

        Returns
        - True if the block is considered empty.
        """
        ...
