"""
Python module generated from Java source file org.bukkit.event.block.BlockExplodeEvent

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import ExplosionResult
from org.bukkit.block import Block
from org.bukkit.block import BlockState
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.block import *
from typing import Any, Callable, Iterable, Tuple


class BlockExplodeEvent(BlockEvent, Cancellable):
    """
    Called when a block explodes.
    
    Note that due to the nature of explosions, .getBlock() will always be
    an air block. .getExplodedBlockState() should be used to get
    information about the block state that exploded.
    """

    def __init__(self, what: "Block", blockState: "BlockState", blocks: list["Block"], yield: float, result: "ExplosionResult"):
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getExplosionResult(self) -> "ExplosionResult":
        """
        Returns the result of the explosion if it is not cancelled.

        Returns
        - the result of the explosion
        """
        ...


    def getExplodedBlockState(self) -> "BlockState":
        """
        Returns the captured BlockState of the block that exploded.

        Returns
        - the block state
        """
        ...


    def blockList(self) -> list["Block"]:
        """
        Returns the list of blocks that would have been removed or were removed
        from the explosion event.

        Returns
        - All blown-up blocks
        """
        ...


    def getYield(self) -> float:
        """
        Returns the percentage of blocks to drop from this explosion

        Returns
        - The yield.
        """
        ...


    def setYield(self, yield: float) -> None:
        """
        Sets the percentage of blocks to drop from this explosion

        Arguments
        - yield: The new yield percentage
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
