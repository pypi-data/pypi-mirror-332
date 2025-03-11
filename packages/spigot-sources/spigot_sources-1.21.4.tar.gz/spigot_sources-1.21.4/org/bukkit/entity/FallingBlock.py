"""
Python module generated from Java source file org.bukkit.entity.FallingBlock

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

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
        Get if the falling block will break into an item if it cannot be placed.
        
        Note that if .getCancelDrop() is `True`, the falling block
        will not drop an item regardless of whether or not the returned value is
        `True`.

        Returns
        - True if the block will break into an item when obstructed
        """
        ...


    def setDropItem(self, drop: bool) -> None:
        """
        Set if the falling block will break into an item if it cannot be placed.
        
        Note that if .getCancelDrop() is `True`, the falling block
        will not drop an item regardless of whether or not the value is set to
        `True`.

        Arguments
        - drop: True to break into an item when obstructed
        """
        ...


    def getCancelDrop(self) -> bool:
        """
        Get if the falling block will not become a block upon landing and not drop
        an item.
        
        Unlike .getDropItem(), this property will prevent the block from
        forming into a block when it lands, causing it to disappear. If this property
        is True and .getDropItem() is True, an item will <strong>NOT</strong>
        be dropped.

        Returns
        - True if the block will disappear
        """
        ...


    def setCancelDrop(self, cancelDrop: bool) -> None:
        """
        Get if the falling block will not become a block upon landing and not drop
        an item.
        
        Unlike .setDropItem(boolean), this property will prevent the block
        from forming into a block when it lands, causing it to disappear. If this
        property is True and .getDropItem() is True, an item will
        <strong>NOT</strong> be dropped.

        Arguments
        - cancelDrop: True to make the block disappear when landing
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


    def getDamagePerBlock(self) -> float:
        """
        Get the amount of damage inflicted upon entities multiplied by the distance
        that the block had fallen when this falling block lands on them.

        Returns
        - the damage per block
        """
        ...


    def setDamagePerBlock(self, damage: float) -> None:
        """
        Set the amount of damage inflicted upon entities multiplied by the distance
        that the block had fallen when this falling block lands on them.
        
        If `damage` is non-zero, this method will automatically call
        .setHurtEntities(boolean) setHurtEntities(True).

        Arguments
        - damage: the damage per block to set. Must be >= 0.0
        """
        ...


    def getMaxDamage(self) -> int:
        """
        Get the maximum amount of damage that can be inflicted upon entities when
        this falling block lands on them.

        Returns
        - the max damage
        """
        ...


    def setMaxDamage(self, damage: int) -> None:
        """
        Set the maximum amount of damage that can be inflicted upon entities when
        this falling block lands on them.
        
        If `damage` is non-zero, this method will automatically call
        .setHurtEntities(boolean) setHurtEntities(True).

        Arguments
        - damage: the max damage to set. Must be >= 0
        """
        ...
