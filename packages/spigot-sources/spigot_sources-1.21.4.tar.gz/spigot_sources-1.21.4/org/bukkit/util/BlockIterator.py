"""
Python module generated from Java source file org.bukkit.util.BlockIterator

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from java.util import Iterator
from java.util import NoSuchElementException
from org.bukkit import Location
from org.bukkit import World
from org.bukkit.block import Block
from org.bukkit.block import BlockFace
from org.bukkit.entity import LivingEntity
from org.bukkit.util import *
from typing import Any, Callable, Iterable, Tuple


class BlockIterator(Iterator):
    """
    This class performs ray tracing and iterates along blocks on a line
    """

    def __init__(self, world: "World", start: "Vector", direction: "Vector", yOffset: float, maxDistance: int):
        """
        Constructs the BlockIterator.
        
        This considers all blocks as 1x1x1 in size.

        Arguments
        - world: The world to use for tracing
        - start: A Vector giving the initial location for the trace
        - direction: A Vector pointing in the direction for the trace
        - yOffset: The trace begins vertically offset from the start vector
            by this value
        - maxDistance: This is the maximum distance in blocks for the
            trace. Setting this value above 140 may lead to problems with
            unloaded chunks. A value of 0 indicates no limit
        """
        ...


    def __init__(self, loc: "Location", yOffset: float, maxDistance: int):
        """
        Constructs the BlockIterator.
        
        This considers all blocks as 1x1x1 in size.

        Arguments
        - loc: The location for the start of the ray trace
        - yOffset: The trace begins vertically offset from the start vector
            by this value
        - maxDistance: This is the maximum distance in blocks for the
            trace. Setting this value above 140 may lead to problems with
            unloaded chunks. A value of 0 indicates no limit
        """
        ...


    def __init__(self, loc: "Location", yOffset: float):
        ...


    def __init__(self, loc: "Location"):
        ...


    def __init__(self, entity: "LivingEntity", maxDistance: int):
        ...


    def __init__(self, entity: "LivingEntity"):
        ...


    def hasNext(self) -> bool:
        ...


    def next(self) -> "Block":
        """
        Returns the next Block in the trace

        Returns
        - the next Block in the trace
        """
        ...


    def remove(self) -> None:
        ...
