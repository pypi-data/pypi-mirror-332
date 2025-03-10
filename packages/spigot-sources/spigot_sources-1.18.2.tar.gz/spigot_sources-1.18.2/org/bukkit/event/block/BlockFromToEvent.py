"""
Python module generated from Java source file org.bukkit.event.block.BlockFromToEvent

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.block import BlockFace
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.block import *
from typing import Any, Callable, Iterable, Tuple


class BlockFromToEvent(BlockEvent, Cancellable):
    """
    Represents events with a source block and a destination block, currently
    only applies to liquid (lava and water) and teleporting dragon eggs.
    
    If a Block From To event is cancelled, the block will not move (the liquid
    will not flow).
    """

    def __init__(self, block: "Block", face: "BlockFace"):
        ...


    def __init__(self, block: "Block", toBlock: "Block"):
        ...


    def getFace(self) -> "BlockFace":
        """
        Gets the BlockFace that the block is moving to.

        Returns
        - The BlockFace that the block is moving to
        """
        ...


    def getToBlock(self) -> "Block":
        """
        Convenience method for getting the faced Block.

        Returns
        - The faced Block
        """
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
