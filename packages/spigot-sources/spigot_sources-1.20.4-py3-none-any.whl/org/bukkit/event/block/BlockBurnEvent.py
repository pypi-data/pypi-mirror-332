"""
Python module generated from Java source file org.bukkit.event.block.BlockBurnEvent

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.block import *
from typing import Any, Callable, Iterable, Tuple


class BlockBurnEvent(BlockEvent, Cancellable):
    """
    Called when a block is destroyed as a result of being burnt by fire.
    
    If a Block Burn event is cancelled, the block will not be destroyed as a
    result of being burnt by fire.
    """

    def __init__(self, block: "Block"):
        ...


    def __init__(self, block: "Block", ignitingBlock: "Block"):
        ...


    def getIgnitingBlock(self) -> "Block":
        """
        Gets the block which ignited this block.

        Returns
        - The Block that ignited and burned this block, or null if no
        source block exists
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
