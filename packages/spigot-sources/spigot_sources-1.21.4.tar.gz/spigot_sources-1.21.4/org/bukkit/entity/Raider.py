"""
Python module generated from Java source file org.bukkit.entity.Raider

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Raid
from org.bukkit import Sound
from org.bukkit.block import Block
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Raider(Monster):

    def setRaid(self, raid: "Raid") -> None:
        """
        Set the Raid that this raider is participating in.

        Arguments
        - raid: the raid to set
        """
        ...


    def getRaid(self) -> "Raid":
        """
        Get the Raid that this raider is participating in, if any.

        Returns
        - the raid, or null if not participating in a raid
        """
        ...


    def getWave(self) -> int:
        """
        Get the raid wave that this raider spawned as part of.

        Returns
        - the raid wave, or 0 if not participating in a raid
        """
        ...


    def setWave(self, wave: int) -> None:
        """
        Set the raid wave that this raider was spawned as part of.

        Arguments
        - wave: the raid wave to set. Must be >= 0
        """
        ...


    def getPatrolTarget(self) -> "Block":
        """
        Gets the block the raider is targeting to patrol.

        Returns
        - target block or null
        """
        ...


    def setPatrolTarget(self, block: "Block") -> None:
        """
        Sets the block the raider is targeting to patrol.

        Arguments
        - block: target block or null. Must be in same world as the entity
        """
        ...


    def isPatrolLeader(self) -> bool:
        """
        Gets whether this entity is a patrol leader.

        Returns
        - patrol leader status
        """
        ...


    def setPatrolLeader(self, leader: bool) -> None:
        """
        Sets whether this entity is a patrol leader.

        Arguments
        - leader: patrol leader status
        """
        ...


    def isCanJoinRaid(self) -> bool:
        """
        Gets whether this mob can join an active raid.

        Returns
        - CanJoinRaid status
        """
        ...


    def setCanJoinRaid(self, join: bool) -> None:
        """
        Sets whether this mob can join an active raid.

        Arguments
        - join: CanJoinRaid status
        """
        ...


    def getTicksOutsideRaid(self) -> int:
        """
        Get the amount of ticks that this mob has exited the bounds of a village
        as a raid participant.
        
        This value is increased only when the mob has had no action for 2,400 ticks
        (according to .getNoActionTicks()). Once both the no action ticks have
        reached that value and the ticks outside a raid exceeds 30, the mob will be
        expelled from the raid.

        Returns
        - the ticks outside of a raid
        """
        ...


    def setTicksOutsideRaid(self, ticks: int) -> None:
        """
        Set the amount of ticks that this mob has exited the bounds of a village
        as a raid participant.
        
        This value is considered only when the mob has had no action for 2,400 ticks
        (according to .getNoActionTicks()). Once both the no action ticks have
        reached that value and the ticks outside a raid exceeds 30, the mob will be
        expelled from the raid.

        Arguments
        - ticks: the ticks outside of a raid
        """
        ...


    def isCelebrating(self) -> bool:
        """
        Check whether or not this raider is celebrating a raid victory.

        Returns
        - True if celebrating, False otherwise
        """
        ...


    def setCelebrating(self, celebrating: bool) -> None:
        """
        Set whether or not this mob is celebrating a raid victory.

        Arguments
        - celebrating: whether or not to celebrate
        """
        ...


    def getCelebrationSound(self) -> "Sound":
        """
        Get the Sound this entity will play when celebrating.

        Returns
        - the celebration sound
        """
        ...
