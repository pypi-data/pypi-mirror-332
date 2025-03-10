"""
Python module generated from Java source file org.bukkit.boss.DragonBattle

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit import Location
from org.bukkit.boss import *
from org.bukkit.entity import EnderCrystal
from org.bukkit.entity import EnderDragon
from typing import Any, Callable, Iterable, Tuple


class DragonBattle:
    """
    Represents a dragon battle state for a world with an end environment.
    """

    def getEnderDragon(self) -> "EnderDragon":
        """
        Get the EnderDragon active in this battle.
        
        Will return null if the dragon has been slain.

        Returns
        - the ender dragon. null if dead
        """
        ...


    def getBossBar(self) -> "BossBar":
        """
        Get the boss bar to be displayed for this dragon battle.

        Returns
        - the boss bar
        """
        ...


    def getEndPortalLocation(self) -> "Location":
        """
        Get the location of the end portal.
        
        This location will be at the center of the base (bottom) of the portal.

        Returns
        - the end portal location or null if not generated
        """
        ...


    def generateEndPortal(self, withPortals: bool) -> bool:
        """
        Generate the end portal.

        Arguments
        - withPortals: whether end portal blocks should be generated

        Returns
        - True if generated, False if already present
        """
        ...


    def hasBeenPreviouslyKilled(self) -> bool:
        """
        Check whether the first dragon has been killed already.

        Returns
        - True if killed before, False otherwise
        """
        ...


    def initiateRespawn(self) -> None:
        """
        Try to initiate a respawn sequence to summon the dragon as though a player has
        placed 4 end crystals on the portal.
        """
        ...


    def initiateRespawn(self, enderCrystals: Iterable["EnderCrystal"]) -> bool:
        """
        Try to initiate a respawn sequence to summon the dragon.

        Arguments
        - enderCrystals: the EnderCrystal EnderCrystals to use in the
        respawn, or a null or empty list to render the respawn sequence
        uncancellable. null entries or crystals that do not reside in the same
        world as this dragon battle will be ignored.

        Returns
        - True if the respawn was initiated, False otherwise.
        """
        ...


    def getRespawnPhase(self) -> "RespawnPhase":
        """
        Get this battle's current respawn phase.

        Returns
        - the current respawn phase.
        """
        ...


    def setRespawnPhase(self, phase: "RespawnPhase") -> bool:
        """
        Set the dragon's respawn phase.
        
        This method will is unsuccessful if a dragon respawn is not in progress.

        Arguments
        - phase: the phase to set

        Returns
        - True if successful, False otherwise

        See
        - .initiateRespawn()
        """
        ...


    def resetCrystals(self) -> None:
        """
        Reset the crystals located on the obsidian pillars (remove their beam
        targets and invulnerability).
        """
        ...


    class RespawnPhase(Enum):
        """
        Represents a phase in the dragon respawn process.
        """

        START = 0
        """
        The crystal beams are directed upwards into the sky.
        """
        PREPARING_TO_SUMMON_PILLARS = 1
        """
        The crystal beams remain directed upwards.
        """
        SUMMONING_PILLARS = 2
        """
        The crystal beams are directed from pillar to pillar, regenerating
        their crystals if necessary.
        """
        SUMMONING_DRAGON = 3
        """
        All crystals (including those from the pillars) are aimed towards the
        sky. Shortly thereafter summoning the dragon and destroying the
        crystals used to initiate the dragon's respawn.
        """
        END = 4
        """
        The end of the respawn sequence. The dragon is actually summoned.
        """
        NONE = 5
        """
        No respawn is in progress.
        """
