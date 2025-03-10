"""
Python module generated from Java source file org.bukkit.entity.Skeleton

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Skeleton(Monster):
    """
    Represents a Skeleton.
    """

    def getSkeletonType(self) -> "SkeletonType":
        """
        Gets the current type of this skeleton.

        Returns
        - Current type

        Deprecated
        - should check what class instance this is
        """
        ...


    def setSkeletonType(self, type: "SkeletonType") -> None:
        """
        Arguments
        - type: type

        Deprecated
        - Must spawn a new subtype variant
        """
        ...


    class SkeletonType(Enum):

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
