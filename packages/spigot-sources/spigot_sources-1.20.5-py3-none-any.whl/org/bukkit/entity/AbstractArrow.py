"""
Python module generated from Java source file org.bukkit.entity.AbstractArrow

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.block import Block
from org.bukkit.entity import *
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class AbstractArrow(Projectile):
    """
    Represents an arrow.
    """

    def getKnockbackStrength(self) -> int:
        """
        Gets the knockback strength for an arrow, which is the
        org.bukkit.enchantments.Enchantment.KNOCKBACK KnockBack level
        of the bow that shot it.

        Returns
        - the knockback strength value
        """
        ...


    def setKnockbackStrength(self, knockbackStrength: int) -> None:
        """
        Sets the knockback strength for an arrow.

        Arguments
        - knockbackStrength: the knockback strength value
        """
        ...


    def getDamage(self) -> float:
        """
        Gets the base amount of damage this arrow will do.
        
        Defaults to 2.0 for a normal arrow with
        `0.5 * (1 + power level)` added for arrows fired from
        enchanted bows.

        Returns
        - base damage amount
        """
        ...


    def setDamage(self, damage: float) -> None:
        """
        Sets the base amount of damage this arrow will do.

        Arguments
        - damage: new damage amount
        """
        ...


    def getPierceLevel(self) -> int:
        """
        Gets the number of times this arrow can pierce through an entity.

        Returns
        - pierce level
        """
        ...


    def setPierceLevel(self, pierceLevel: int) -> None:
        """
        Sets the number of times this arrow can pierce through an entity.
        
        Must be between 0 and 127 times.

        Arguments
        - pierceLevel: new pierce level
        """
        ...


    def isCritical(self) -> bool:
        """
        Gets whether this arrow is critical.
        
        Critical arrows have increased damage and cause particle effects.
        
        Critical arrows generally occur when a player fully draws a bow before
        firing.

        Returns
        - True if it is critical
        """
        ...


    def setCritical(self, critical: bool) -> None:
        """
        Sets whether or not this arrow should be critical.

        Arguments
        - critical: whether or not it should be critical
        """
        ...


    def isInBlock(self) -> bool:
        """
        Gets whether this arrow is in a block or not.
        
        Arrows in a block are motionless and may be picked up by players.

        Returns
        - True if in a block
        """
        ...


    def getAttachedBlock(self) -> "Block":
        """
        Gets the block to which this arrow is attached.

        Returns
        - the attached block or null if not attached
        """
        ...


    def getPickupStatus(self) -> "PickupStatus":
        """
        Gets the current pickup status of this arrow.

        Returns
        - the pickup status of this arrow.
        """
        ...


    def setPickupStatus(self, status: "PickupStatus") -> None:
        """
        Sets the current pickup status of this arrow.

        Arguments
        - status: new pickup status of this arrow.
        """
        ...


    def isShotFromCrossbow(self) -> bool:
        """
        Gets if this arrow was shot from a crossbow.

        Returns
        - if shot from a crossbow
        """
        ...


    def setShotFromCrossbow(self, shotFromCrossbow: bool) -> None:
        """
        Sets if this arrow was shot from a crossbow.

        Arguments
        - shotFromCrossbow: if shot from a crossbow
        """
        ...


    def getItem(self) -> "ItemStack":
        """
        Gets the ItemStack which will be picked up from this arrow.

        Returns
        - The picked up ItemStack
        """
        ...


    def setItem(self, item: "ItemStack") -> None:
        """
        Sets the ItemStack which will be picked up from this arrow.

        Arguments
        - item: ItemStack set to be picked up
        """
        ...


    class PickupStatus(Enum):
        """
        Represents the pickup status of this arrow.
        """

        DISALLOWED = 0
        """
        The arrow cannot be picked up.
        """
        ALLOWED = 1
        """
        The arrow can be picked up.
        """
        CREATIVE_ONLY = 2
        """
        The arrow can only be picked up by players in creative mode.
        """
