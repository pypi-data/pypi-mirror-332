"""
Python module generated from Java source file org.bukkit.generator.BlockPopulator

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Random
from org.bukkit import Chunk
from org.bukkit import World
from org.bukkit.generator import *
from typing import Any, Callable, Iterable, Tuple


class BlockPopulator:
    """
    A block populator is responsible for generating a small area of blocks.
    
    For example, generating glowstone inside the nether or generating dungeons
    full of treasure
    """

    def populate(self, world: "World", random: "Random", source: "Chunk") -> None:
        """
        Populates an area of blocks at or around the given chunk.
        
        The chunks on each side of the specified chunk must already exist; that
        is, there must be one north, east, south and west of the specified
        chunk. The "corner" chunks may not exist, in which scenario the
        populator should record any changes required for those chunks and
        perform the changes when they are ready.

        Arguments
        - world: The world to generate in
        - random: The random generator to use
        - source: The chunk to generate for
        """
        ...
