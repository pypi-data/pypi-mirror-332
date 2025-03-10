"""
Python module generated from Java source file org.bukkit.event.block.BlockGrowEvent

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.block import BlockState
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.block import *
from typing import Any, Callable, Iterable, Tuple


class BlockGrowEvent(BlockEvent, Cancellable):
    """
    Called when a block grows naturally in the world.
    
    Examples:
    
    - Wheat
    - Sugar Cane
    - Cactus
    - Watermelon
    - Pumpkin
    - Turtle Egg
    
    
    If a Block Grow event is cancelled, the block will not grow.
    """

    def __init__(self, block: "Block", newState: "BlockState"):
        ...


    def getNewState(self) -> "BlockState":
        """
        Gets the state of the block where it will form or spread to.

        Returns
        - The block state for this events block
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
