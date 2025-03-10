"""
Python module generated from Java source file org.bukkit.structure.Palette

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import BlockState
from org.bukkit.structure import *
from typing import Any, Callable, Iterable, Tuple


class Palette:
    """
    Represent a variation of a structure.
    
    Most structures, like the ones generated with structure blocks, only have a
    single variant.
    """

    def getBlocks(self) -> list["BlockState"]:
        """
        Gets a copy of the blocks this Palette is made of.
        
        The BlockState.getLocation() positions of the returned block
        states are offsets relative to the structure's position that is provided
        once the structure is placed into the world.

        Returns
        - The blocks in this palette
        """
        ...


    def getBlockCount(self) -> int:
        """
        Gets the number of blocks stored in this palette.

        Returns
        - The number of blocks in this palette
        """
        ...
