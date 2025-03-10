"""
Python module generated from Java source file org.bukkit.event.block.BlockSpreadEvent

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.block import BlockState
from org.bukkit.event import HandlerList
from org.bukkit.event.block import *
from typing import Any, Callable, Iterable, Tuple


class BlockSpreadEvent(BlockFormEvent):
    """
    Called when a block spreads based on world conditions.
    
    Use BlockFormEvent to catch blocks that "randomly" form instead of
    actually spread.
    
    Examples:
    
    - Mushrooms spreading.
    - Fire spreading.
    
    
    If a Block Spread event is cancelled, the block will not spread.

    See
    - BlockFormEvent
    """

    def __init__(self, block: "Block", source: "Block", newState: "BlockState"):
        ...


    def getSource(self) -> "Block":
        """
        Gets the source block involved in this event.

        Returns
        - the Block for the source block involved in this event.
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
