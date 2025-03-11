"""
Python module generated from Java source file org.bukkit.event.block.BlockPistonExtendEvent

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Collections
from org.bukkit.block import Block
from org.bukkit.block import BlockFace
from org.bukkit.event import HandlerList
from org.bukkit.event.block import *
from typing import Any, Callable, Iterable, Tuple


class BlockPistonExtendEvent(BlockPistonEvent):
    """
    Called when a piston extends
    """

    def __init__(self, block: "Block", length: int, direction: "BlockFace"):
        ...


    def __init__(self, block: "Block", blocks: list["Block"], direction: "BlockFace"):
        ...


    def getLength(self) -> int:
        """
        Get the amount of blocks which will be moved while extending.

        Returns
        - the amount of moving blocks

        Deprecated
        - slime blocks make the value of this method
                 inaccurate due to blocks being pushed at the side
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
