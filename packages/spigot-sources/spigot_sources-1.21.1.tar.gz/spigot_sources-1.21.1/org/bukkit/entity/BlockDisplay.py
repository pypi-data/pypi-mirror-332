"""
Python module generated from Java source file org.bukkit.entity.BlockDisplay

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import BlockData
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class BlockDisplay(Display):
    """
    Represents a block display entity.
    """

    def getBlock(self) -> "BlockData":
        """
        Gets the displayed block.

        Returns
        - the displayed block
        """
        ...


    def setBlock(self, block: "BlockData") -> None:
        """
        Sets the displayed block.

        Arguments
        - block: the new block
        """
        ...
