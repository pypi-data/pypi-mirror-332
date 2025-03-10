"""
Python module generated from Java source file org.bukkit.block.EntityBlockStorage

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import *
from org.bukkit.entity import Entity
from typing import Any, Callable, Iterable, Tuple


class EntityBlockStorage(TileState):
    """
    Represents a captured state of a block which stores entities.
    
    Type `<T>`: Entity this block can store
    """

    def isFull(self) -> bool:
        """
        Check if the block is completely full of entities.

        Returns
        - True if block is full
        """
        ...


    def getEntityCount(self) -> int:
        """
        Get the amount of entities currently in this block.

        Returns
        - Amount of entities currently in this block
        """
        ...


    def getMaxEntities(self) -> int:
        """
        Get the maximum amount of entities this block can hold.

        Returns
        - Maximum amount of entities this block can hold
        """
        ...


    def setMaxEntities(self, max: int) -> None:
        """
        Set the maximum amount of entities this block can hold.

        Arguments
        - max: Maximum amount of entities this block can hold
        """
        ...


    def releaseEntities(self) -> list["T"]:
        """
        Release all the entities currently stored in the block.

        Returns
        - List of all entities which were released
        """
        ...


    def addEntity(self, entity: "T") -> None:
        """
        Add an entity to the block.

        Arguments
        - entity: Entity to add to the block
        """
        ...
