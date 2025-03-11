"""
Python module generated from Java source file org.bukkit.event.block.BlockPistonRetractEvent

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Location
from org.bukkit.block import Block
from org.bukkit.block import BlockFace
from org.bukkit.event import HandlerList
from org.bukkit.event.block import *
from typing import Any, Callable, Iterable, Tuple


class BlockPistonRetractEvent(BlockPistonEvent):
    """
    Called when a piston retracts
    """

    def __init__(self, block: "Block", blocks: list["Block"], direction: "BlockFace"):
        ...


    def getRetractLocation(self) -> "Location":
        """
        Gets the location where the possible moving block might be if the
        retracting piston is sticky.

        Returns
        - The possible location of the possibly moving block.
        """
        ...


    def getBlocks(self) -> list["Block"]:
        """
        Get an immutable list of the blocks which will be moved by the
        extending.

        Returns
        - Immutable list of the moved blocks.
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
