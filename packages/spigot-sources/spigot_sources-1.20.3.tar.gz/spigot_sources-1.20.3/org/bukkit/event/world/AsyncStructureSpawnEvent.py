"""
Python module generated from Java source file org.bukkit.event.world.AsyncStructureSpawnEvent

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import World
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.world import *
from org.bukkit.generator.structure import Structure
from org.bukkit.util import BoundingBox
from typing import Any, Callable, Iterable, Tuple


class AsyncStructureSpawnEvent(WorldEvent, Cancellable):
    """
    Called when a Structure is naturally generated in the world.
    """

    def __init__(self, world: "World", structure: "Structure", boundingBox: "BoundingBox", chunkX: int, chunkZ: int):
        ...


    def getStructure(self) -> "Structure":
        """
        Get the structure reference that is generated.

        Returns
        - the structure
        """
        ...


    def getBoundingBox(self) -> "BoundingBox":
        """
        Get the bounding box of the structure.

        Returns
        - the bounding box
        """
        ...


    def getChunkX(self) -> int:
        """
        Get the x coordinate of the origin chunk of the structure.
        
        **Note, it is not safe to attempt to retrieve or interact with this
        chunk. This event is informative only!**

        Returns
        - the chunk x coordinate
        """
        ...


    def getChunkZ(self) -> int:
        """
        Get the z coordinate of the origin chunk of the structure.
        
        **Note, it is not safe to attempt to retrieve or interact with this
        chunk. This event is informative only!**

        Returns
        - the chunk z coordinate
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
