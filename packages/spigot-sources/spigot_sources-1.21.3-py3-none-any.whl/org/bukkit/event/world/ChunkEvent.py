"""
Python module generated from Java source file org.bukkit.event.world.ChunkEvent

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Chunk
from org.bukkit.event.world import *
from typing import Any, Callable, Iterable, Tuple


class ChunkEvent(WorldEvent):
    """
    Represents a Chunk related event
    """

    def getChunk(self) -> "Chunk":
        """
        Gets the chunk being loaded/unloaded

        Returns
        - Chunk that triggered this event
        """
        ...
