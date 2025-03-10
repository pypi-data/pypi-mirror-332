"""
Python module generated from Java source file org.bukkit.block.DecoratedPot

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.block import *
from typing import Any, Callable, Iterable, Tuple


class DecoratedPot(TileState):
    """
    Represents a captured state of a decorated pot.
    """

    def getShards(self) -> list["Material"]:
        """
        Gets the shards which will be dropped when this pot is broken.

        Returns
        - shards
        """
        ...
