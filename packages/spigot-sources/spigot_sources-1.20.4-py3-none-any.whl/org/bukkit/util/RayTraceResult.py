"""
Python module generated from Java source file org.bukkit.util.RayTraceResult

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from java.util import Objects
from org.bukkit.block import Block
from org.bukkit.block import BlockFace
from org.bukkit.entity import Entity
from org.bukkit.util import *
from typing import Any, Callable, Iterable, Tuple


class RayTraceResult:
    """
    The hit result of a ray trace.
    
    Only the hit position is guaranteed to always be available. The availability
    of the other attributes depends on what got hit and on the context in which
    the ray trace was performed.
    """

    def __init__(self, hitPosition: "Vector"):
        """
        Creates a RayTraceResult.

        Arguments
        - hitPosition: the hit position
        """
        ...


    def __init__(self, hitPosition: "Vector", hitBlockFace: "BlockFace"):
        """
        Creates a RayTraceResult.

        Arguments
        - hitPosition: the hit position
        - hitBlockFace: the hit block face
        """
        ...


    def __init__(self, hitPosition: "Vector", hitBlock: "Block", hitBlockFace: "BlockFace"):
        """
        Creates a RayTraceResult.

        Arguments
        - hitPosition: the hit position
        - hitBlock: the hit block
        - hitBlockFace: the hit block face
        """
        ...


    def __init__(self, hitPosition: "Vector", hitEntity: "Entity"):
        """
        Creates a RayTraceResult.

        Arguments
        - hitPosition: the hit position
        - hitEntity: the hit entity
        """
        ...


    def __init__(self, hitPosition: "Vector", hitEntity: "Entity", hitBlockFace: "BlockFace"):
        """
        Creates a RayTraceResult.

        Arguments
        - hitPosition: the hit position
        - hitEntity: the hit entity
        - hitBlockFace: the hit block face
        """
        ...


    def getHitPosition(self) -> "Vector":
        """
        Gets the exact position of the hit.

        Returns
        - a copy of the exact hit position
        """
        ...


    def getHitBlock(self) -> "Block":
        """
        Gets the hit block.

        Returns
        - the hit block, or `null` if not available
        """
        ...


    def getHitBlockFace(self) -> "BlockFace":
        """
        Gets the hit block face.

        Returns
        - the hit block face, or `null` if not available
        """
        ...


    def getHitEntity(self) -> "Entity":
        """
        Gets the hit entity.

        Returns
        - the hit entity, or `null` if not available
        """
        ...


    def hashCode(self) -> int:
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def toString(self) -> str:
        ...
