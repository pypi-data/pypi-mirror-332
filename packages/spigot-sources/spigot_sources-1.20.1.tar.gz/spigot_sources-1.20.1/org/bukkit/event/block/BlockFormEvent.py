"""
Python module generated from Java source file org.bukkit.event.block.BlockFormEvent

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.block import BlockState
from org.bukkit.event import HandlerList
from org.bukkit.event.block import *
from typing import Any, Callable, Iterable, Tuple


class BlockFormEvent(BlockGrowEvent):
    """
    Called when a block is formed or spreads based on world conditions.
    
    Use BlockSpreadEvent to catch blocks that actually spread and don't
    just "randomly" form.
    
    Examples:
    
    - Snow forming due to a snow storm.
    - Ice forming in a snowy Biome like Taiga or Tundra.
    -  Obsidian / Cobblestone forming due to contact with water.
    -  Concrete forming due to mixing of concrete powder and water.
    
    
    If a Block Form event is cancelled, the block will not be formed.

    See
    - BlockSpreadEvent
    """

    def __init__(self, block: "Block", newState: "BlockState"):
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
