"""
Python module generated from Java source file org.bukkit.event.world.ChunkUnloadEvent

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Chunk
from org.bukkit.event import HandlerList
from org.bukkit.event.world import *
from typing import Any, Callable, Iterable, Tuple


class ChunkUnloadEvent(ChunkEvent):
    """
    Called when a chunk is unloaded
    """

    def __init__(self, chunk: "Chunk"):
        ...


    def __init__(self, chunk: "Chunk", save: bool):
        ...


    def isSaveChunk(self) -> bool:
        """
        Return whether this chunk will be saved to disk.

        Returns
        - chunk save status
        """
        ...


    def setSaveChunk(self, saveChunk: bool) -> None:
        """
        Set whether this chunk will be saved to disk.

        Arguments
        - saveChunk: chunk save status
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
