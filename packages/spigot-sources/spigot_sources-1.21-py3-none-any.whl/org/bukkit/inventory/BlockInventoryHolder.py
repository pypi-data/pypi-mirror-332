"""
Python module generated from Java source file org.bukkit.inventory.BlockInventoryHolder

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.inventory import *
from typing import Any, Callable, Iterable, Tuple


class BlockInventoryHolder(InventoryHolder):
    """
    Represents a block inventory holder - either a BlockState, or a regular
    Block.
    """

    def getBlock(self) -> "Block":
        """
        Gets the block associated with this holder.

        Returns
        - the block associated with this holder

        Raises
        - IllegalStateException: if the holder is a block state and is not
        placed
        """
        ...
