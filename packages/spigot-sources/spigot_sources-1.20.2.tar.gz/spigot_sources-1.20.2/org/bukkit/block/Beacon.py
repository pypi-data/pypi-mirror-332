"""
Python module generated from Java source file org.bukkit.block.Beacon

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Nameable
from org.bukkit.block import *
from org.bukkit.entity import LivingEntity
from org.bukkit.potion import PotionEffect
from org.bukkit.potion import PotionEffectType
from typing import Any, Callable, Iterable, Tuple


class Beacon(TileState, Lockable, Nameable):
    """
    Represents a captured state of a beacon.
    """

    def getEntitiesInRange(self) -> Iterable["LivingEntity"]:
        """
        Returns the list of players within the beacon's range of effect.
        
        This will return an empty list if the block represented by this state is
        no longer a beacon.

        Returns
        - the players in range

        Raises
        - IllegalStateException: if this block state is not placed
        """
        ...


    def getTier(self) -> int:
        """
        Returns the tier of the beacon pyramid (0-4). The tier refers to the
        beacon's power level, based on how many layers of blocks are in the
        pyramid. Tier 1 refers to a beacon with one layer of 9 blocks under it.

        Returns
        - the beacon tier
        """
        ...


    def getPrimaryEffect(self) -> "PotionEffect":
        """
        Returns the primary effect set on the beacon

        Returns
        - the primary effect or null if not set
        """
        ...


    def setPrimaryEffect(self, effect: "PotionEffectType") -> None:
        """
        Set the primary effect on this beacon, or null to clear.

        Arguments
        - effect: new primary effect
        """
        ...


    def getSecondaryEffect(self) -> "PotionEffect":
        """
        Returns the secondary effect set on the beacon.

        Returns
        - the secondary effect or null if no secondary effect
        """
        ...


    def setSecondaryEffect(self, effect: "PotionEffectType") -> None:
        """
        Set the secondary effect on this beacon, or null to clear. Note that tier
        must be &gt;= 4 for this effect to be active.

        Arguments
        - effect: desired secondary effect
        """
        ...
