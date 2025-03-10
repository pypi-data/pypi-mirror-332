"""
Python module generated from Java source file org.bukkit.event.block.BlockFadeEvent

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

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


class BlockFadeEvent(BlockEvent, Cancellable):
    """
    Called when a block fades, melts or disappears based on world conditions
    
    Examples:
    
    - Snow melting due to being near a light source.
    - Ice melting due to being near a light source.
    - Fire burning out after time, without destroying fuel block.
    - Coral fading to dead coral due to lack of water
    - Turtle Egg bursting when a turtle hatches
    
    
    If a Block Fade event is cancelled, the block will not fade, melt or
    disappear.
    """

    def __init__(self, block: "Block", newState: "BlockState"):
        ...


    def getNewState(self) -> "BlockState":
        """
        Gets the state of the block that will be fading, melting or
        disappearing.

        Returns
        - The block state of the block that will be fading, melting or
            disappearing
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
