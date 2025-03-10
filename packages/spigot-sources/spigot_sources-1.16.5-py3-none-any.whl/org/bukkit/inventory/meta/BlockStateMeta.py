"""
Python module generated from Java source file org.bukkit.inventory.meta.BlockStateMeta

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import BlockState
from org.bukkit.inventory.meta import *
from typing import Any, Callable, Iterable, Tuple


class BlockStateMeta(ItemMeta):

    def hasBlockState(self) -> bool:
        """
        Returns whether the item has a block state currently
        attached to it.

        Returns
        - whether a block state is already attached
        """
        ...


    def getBlockState(self) -> "BlockState":
        """
        Returns the currently attached block state for this
        item or creates a new one if one doesn't exist.
        
        The state is a copy, it must be set back (or to another
        item) with .setBlockState(org.bukkit.block.BlockState)

        Returns
        - the attached state or a new state
        """
        ...


    def setBlockState(self, blockState: "BlockState") -> None:
        """
        Attaches a copy of the passed block state to the item.

        Arguments
        - blockState: the block state to attach to the block.

        Raises
        - IllegalArgumentException: if the blockState is null
                or invalid for this item.
        """
        ...
