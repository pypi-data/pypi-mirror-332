"""
Python module generated from Java source file org.bukkit.event.world.ChunkLoadEvent

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Chunk
from org.bukkit.event import HandlerList
from org.bukkit.event.world import *
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
        
        Note that if this chunk is new, it will not be populated at this time.

        Returns
        - True if the chunk is new, otherwise False
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
