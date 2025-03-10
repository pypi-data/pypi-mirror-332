"""
Python module generated from Java source file org.bukkit.inventory.meta.BlockDataMeta

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.block.data import BlockData
from org.bukkit.inventory.meta import *
from typing import Any, Callable, Iterable, Tuple


class BlockDataMeta(ItemMeta):

    def hasBlockData(self) -> bool:
        """
        Returns whether the item has block data currently attached to it.

        Returns
        - whether block data is already attached
        """
        ...


    def getBlockData(self, material: "Material") -> "BlockData":
        """
        Returns the currently attached block data for this item or creates a new
        one if one doesn't exist.
        
        The state is a copy, it must be set back (or to another item) with
        .setBlockData(org.bukkit.block.data.BlockData)

        Arguments
        - material: the material we wish to get this data in the context of

        Returns
        - the attached data or new data
        """
        ...


    def setBlockData(self, blockData: "BlockData") -> None:
        """
        Attaches a copy of the passed block data to the item.

        Arguments
        - blockData: the block data to attach to the block.

        Raises
        - IllegalArgumentException: if the blockData is null or invalid for
        this item.
        """
        ...
