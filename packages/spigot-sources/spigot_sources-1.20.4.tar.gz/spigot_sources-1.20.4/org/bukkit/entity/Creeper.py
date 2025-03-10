"""
Python module generated from Java source file org.bukkit.entity.Creeper

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Creeper(Monster):
    """
    Represents a Creeper
    """

    def isPowered(self) -> bool:
        """
        Checks if this Creeper is powered (Electrocuted)

        Returns
        - True if this creeper is powered
        """
        ...


    def setPowered(self, value: bool) -> None:
        """
        Sets the Powered status of this Creeper

        Arguments
        - value: New Powered status
        """
        ...


    def setMaxFuseTicks(self, ticks: int) -> None:
        """
        Set the maximum fuse ticks for this Creeper, where the maximum ticks
        is the amount of time in which a creeper is allowed to be in the
        primed state before exploding.

        Arguments
        - ticks: the new maximum fuse ticks
        """
        ...


    def getMaxFuseTicks(self) -> int:
        """
        Get the maximum fuse ticks for this Creeper, where the maximum ticks
        is the amount of time in which a creeper is allowed to be in the
        primed state before exploding.

        Returns
        - the maximum fuse ticks
        """
        ...


    def setFuseTicks(self, ticks: int) -> None:
        """
        Set the fuse ticks for this Creeper, where the ticks is the amount of
        time in which a creeper has been in the primed state.

        Arguments
        - ticks: the new fuse ticks
        """
        ...


    def getFuseTicks(self) -> int:
        """
        Get the maximum fuse ticks for this Creeper, where the ticks is the
        amount of time in which a creeper has been in the primed state.

        Returns
        - the fuse ticks
        """
        ...


    def setExplosionRadius(self, radius: int) -> None:
        """
        Set the explosion radius in which this Creeper's explosion will affect.

        Arguments
        - radius: the new explosion radius
        """
        ...


    def getExplosionRadius(self) -> int:
        """
        Get the explosion radius in which this Creeper's explosion will affect.

        Returns
        - the explosion radius
        """
        ...


    def explode(self) -> None:
        """
        Makes this Creeper explode instantly.
        
        The resulting explosion can be cancelled by an
        org.bukkit.event.entity.ExplosionPrimeEvent and obeys the mob
        griefing gamerule.
        """
        ...


    def ignite(self) -> None:
        """
        Ignites this Creeper, beginning its fuse.
        
        The amount of time the Creeper takes to explode will depend on what
        .setMaxFuseTicks is set as.
        
        The resulting explosion can be cancelled by an
        org.bukkit.event.entity.ExplosionPrimeEvent and obeys the mob
        griefing gamerule.
        """
        ...
