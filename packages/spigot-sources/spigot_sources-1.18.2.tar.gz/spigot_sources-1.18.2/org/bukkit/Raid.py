"""
Python module generated from Java source file org.bukkit.Raid

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from java.util import UUID
from org.bukkit import *
from org.bukkit.entity import Raider
from typing import Any, Callable, Iterable, Tuple


class Raid:
    """
    Represents a raid event.
    """

    def isStarted(self) -> bool:
        """
        Get whether this raid started.

        Returns
        - whether raid is started
        """
        ...


    def getActiveTicks(self) -> int:
        """
        Gets the amount of ticks this raid has existed.

        Returns
        - active ticks
        """
        ...


    def getBadOmenLevel(self) -> int:
        """
        Gets the Bad Omen level of this raid.

        Returns
        - Bad Omen level (between 0 and 5)
        """
        ...


    def setBadOmenLevel(self, badOmenLevel: int) -> None:
        """
        Sets the Bad Omen level.
        
        If the level is higher than 1, there will be an additional wave that as
        strong as the final wave.

        Arguments
        - badOmenLevel: new Bad Omen level (from 0-5)

        Raises
        - IllegalArgumentException: if invalid Bad Omen level
        """
        ...


    def getLocation(self) -> "Location":
        """
        Gets the center location where the raid occurs.

        Returns
        - location
        """
        ...


    def getStatus(self) -> "RaidStatus":
        """
        Gets the current status of the raid.
        
        Do not use this method to check if the raid has been started, call
        .isStarted() instead.

        Returns
        - Raids status
        """
        ...


    def getSpawnedGroups(self) -> int:
        """
        Gets the number of raider groups which have spawned.

        Returns
        - total spawned groups
        """
        ...


    def getTotalGroups(self) -> int:
        """
        Gets the number of raider groups which would spawn.
        
        This also includes the group which spawns in the additional wave (if
        present).

        Returns
        - total groups
        """
        ...


    def getTotalWaves(self) -> int:
        """
        Gets the number of waves in this raid (exclude the additional wave).

        Returns
        - number of waves
        """
        ...


    def getTotalHealth(self) -> float:
        """
        Gets the sum of all raider's health.

        Returns
        - total raiders health
        """
        ...


    def getHeroes(self) -> set["UUID"]:
        """
        Get the UUID of all heroes in this raid.

        Returns
        - a set of unique ids
        """
        ...


    def getRaiders(self) -> list["Raider"]:
        """
        Gets all remaining Raider in the present wave.

        Returns
        - a list of current raiders
        """
        ...


    class RaidStatus(Enum):
        """
        Represents the status of a Raid.
        """

        ONGOING = 0
        """
        The raid is in progress.
        """
        VICTORY = 1
        """
        The raid was beaten by heroes.
        """
        LOSS = 2
        """
        The village has fallen (i.e. all villagers died).
        """
        STOPPED = 3
        """
        The raid was terminated.
        """
