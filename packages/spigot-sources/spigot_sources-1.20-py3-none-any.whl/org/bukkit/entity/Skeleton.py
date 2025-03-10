"""
Python module generated from Java source file org.bukkit.entity.Skeleton

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Skeleton(AbstractSkeleton):
    """
    Represents a Skeleton.
    
    This interface only represents the normal skeleton type on the server.
    Other skeleton-like entities, such as the WitherSkeleton or the
    Stray are not related to this type.
    """

    def isConverting(self) -> bool:
        """
        Computes whether or not this skeleton is currently in the process of
        converting to a Stray due to it being frozen by powdered snow.

        Returns
        - whether or not the skeleton is converting to a stray.
        """
        ...


    def getConversionTime(self) -> int:
        """
        Gets the amount of ticks until this entity will be converted to a stray
        as a result of being frozen by a powdered snow block.
        
        When this reaches 0, the entity will be converted.

        Returns
        - the conversion time left represented in ticks.

        Raises
        - IllegalStateException: if .isConverting() is False.
        """
        ...


    def setConversionTime(self, time: int) -> None:
        """
        Sets the amount of ticks until this entity will be converted to a stray
        as a result of being frozen by a powdered snow block.
        
        When this reaches 0, the entity will be converted. A value of less than 0
        will stop the current conversion process without converting the current
        entity.

        Arguments
        - time: the new conversion time left before the conversion in ticks.
        """
        ...


    class SkeletonType(Enum):
        """
        A legacy enum that defines the different variances of skeleton-like
        entities on the server.

        Deprecated
        - classes are different types. This interface only remains in
            the Skeleton interface to preserve backwards compatibility.
        """

        NORMAL = 0
        """
        Standard skeleton type.
        """
        WITHER = 1
        """
        Wither skeleton. Generally found in Nether fortresses.
        """
        STRAY = 2
        """
        Stray skeleton. Generally found in ice biomes. Shoots tipped arrows.
        """
