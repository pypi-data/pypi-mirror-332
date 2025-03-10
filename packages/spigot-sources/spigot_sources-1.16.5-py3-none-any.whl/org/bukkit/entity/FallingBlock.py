"""
Python module generated from Java source file org.bukkit.entity.FallingBlock

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.block.data import BlockData
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class FallingBlock(Entity):
    """
    Represents a falling block
    """

    def getMaterial(self) -> "Material":
        """
        Get the Material of the falling block

        Returns
        - Material of the block

        Deprecated
        - use .getBlockData()
        """
        ...


    def getBlockData(self) -> "BlockData":
        """
        Get the data for the falling block

        Returns
        - data of the block
        """
        ...


    def getDropItem(self) -> bool:
        """
        Get if the falling block will break into an item if it cannot be placed

        Returns
        - True if the block will break into an item when obstructed
        """
        ...


    def setDropItem(self, drop: bool) -> None:
        """
        Set if the falling block will break into an item if it cannot be placed

        Arguments
        - drop: True to break into an item when obstructed
        """
        ...


    def canHurtEntities(self) -> bool:
        """
        Get the HurtEntities state of this block.

        Returns
        - whether entities will be damaged by this block.
        """
        ...


    def setHurtEntities(self, hurtEntities: bool) -> None:
        """
        Set the HurtEntities state of this block.

        Arguments
        - hurtEntities: whether entities will be damaged by this block.
        """
        ...
