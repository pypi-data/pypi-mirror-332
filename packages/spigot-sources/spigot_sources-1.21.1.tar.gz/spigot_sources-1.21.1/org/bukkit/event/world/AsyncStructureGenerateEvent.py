"""
Python module generated from Java source file org.bukkit.event.world.AsyncStructureGenerateEvent

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from enum import Enum
from java.util import Collections
from org.bukkit import NamespacedKey
from org.bukkit import World
from org.bukkit.event import HandlerList
from org.bukkit.event.world import *
from org.bukkit.generator.structure import Structure
from org.bukkit.util import BlockTransformer
from org.bukkit.util import BoundingBox
from org.bukkit.util import EntityTransformer
from typing import Any, Callable, Iterable, Tuple


class AsyncStructureGenerateEvent(WorldEvent):
    """
    This event will sometimes fire synchronously, depending on how it was
    triggered.
    
    The constructor provides a boolean to indicate if the event was fired
    synchronously or asynchronously. When asynchronous, this event can be called
    from any thread, sans the main thread, and has limited access to the API.
    
    If a Structure is naturally placed in a chunk of the world, this
    event will be asynchronous. If a player executes the '/place structure'
    command, this event will be synchronous.
    
    Allows to register transformers that can modify the blocks placed and
    entities spawned by the structure.
    
    Care should be taken to check .isAsynchronous() and treat the event
    appropriately.
    """

    def __init__(self, world: "World", async: bool, cause: "Cause", structure: "Structure", boundingBox: "BoundingBox", chunkX: int, chunkZ: int):
        ...


    def getCause(self) -> "Cause":
        """
        Gets the event cause.

        Returns
        - the event cause
        """
        ...


    def getBlockTransformer(self, key: "NamespacedKey") -> "BlockTransformer":
        """
        Gets a block transformer by key.

        Arguments
        - key: the key of the block transformer

        Returns
        - the block transformer or null
        """
        ...


    def setBlockTransformer(self, key: "NamespacedKey", transformer: "BlockTransformer") -> None:
        """
        Sets a block transformer to a key.

        Arguments
        - key: the key
        - transformer: the block transformer
        """
        ...


    def removeBlockTransformer(self, key: "NamespacedKey") -> None:
        """
        Removes a block transformer.

        Arguments
        - key: the key of the block transformer
        """
        ...


    def clearBlockTransformers(self) -> None:
        """
        Removes all block transformers.
        """
        ...


    def getBlockTransformers(self) -> dict["NamespacedKey", "BlockTransformer"]:
        """
        Gets all block transformers in a unmodifiable map.

        Returns
        - the block transformers in a map
        """
        ...


    def getEntityTransformer(self, key: "NamespacedKey") -> "EntityTransformer":
        """
        Gets a entity transformer by key.

        Arguments
        - key: the key of the entity transformer

        Returns
        - the entity transformer or null
        """
        ...


    def setEntityTransformer(self, key: "NamespacedKey", transformer: "EntityTransformer") -> None:
        """
        Sets a entity transformer to a key.

        Arguments
        - key: the key
        - transformer: the entity transformer
        """
        ...


    def removeEntityTransformer(self, key: "NamespacedKey") -> None:
        """
        Removes a entity transformer.

        Arguments
        - key: the key of the entity transformer
        """
        ...


    def clearEntityTransformers(self) -> None:
        """
        Removes all entity transformers.
        """
        ...


    def getEntityTransformers(self) -> dict["NamespacedKey", "EntityTransformer"]:
        """
        Gets all entity transformers in a unmodifiable map.

        Returns
        - the entity transformers in a map
        """
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

        Returns
        - the chunk x coordinate
        """
        ...


    def getChunkZ(self) -> int:
        """
        Get the z coordinate of the origin chunk of the structure.

        Returns
        - the chunk z coordinate
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...


    class Cause(Enum):

        COMMAND = 0
        WORLD_GENERATION = 1
        CUSTOM = 2
