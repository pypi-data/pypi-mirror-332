"""
Python module generated from Java source file org.bukkit.event.world.ChunkLoadEvent

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Chunk
from org.bukkit.event import HandlerList
from org.bukkit.event.world import *
from org.bukkit.generator import BlockPopulator
from typing import Any, Callable, Iterable, Tuple


class ChunkLoadEvent(ChunkEvent):
    """
    Called when a chunk is loaded
    """

    def __init__(self, chunk: "Chunk", newChunk: bool):
        ...


    def isNewChunk(self) -> bool:
        """
        Gets if this chunk was newly created or not.
        
        **Note:** Do not use this to generated blocks in a newly generated chunk.
        Use a BlockPopulator instead.

        Returns
        - True if the chunk is new, otherwise False
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
