"""
Python module generated from Java source file org.bukkit.scoreboard.Score

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import OfflinePlayer
from org.bukkit.scoreboard import *
from typing import Any, Callable, Iterable, Tuple


class Score:
    """
    A score entry for an .getEntry() entry on an .getObjective() objective. Changing this will not affect any other
    objective or scoreboard.
    """

    def getPlayer(self) -> "OfflinePlayer":
        """
        Gets the OfflinePlayer being tracked by this Score

        Returns
        - this Score's tracked player

        See
        - .getEntry()

        Deprecated
        - Scoreboards can contain entries that aren't players
        """
        ...


    def getEntry(self) -> str:
        """
        Gets the entry being tracked by this Score

        Returns
        - this Score's tracked entry
        """
        ...


    def getObjective(self) -> "Objective":
        """
        Gets the Objective being tracked by this Score

        Returns
        - this Score's tracked objective
        """
        ...


    def getScore(self) -> int:
        """
        Gets the current score

        Returns
        - the current score

        Raises
        - IllegalStateException: if the associated objective has been
            unregistered
        """
        ...


    def setScore(self, score: int) -> None:
        """
        Sets the current score.

        Arguments
        - score: New score

        Raises
        - IllegalStateException: if the associated objective has been
            unregistered
        """
        ...


    def isScoreSet(self) -> bool:
        """
        Shows if this score has been set at any point in time.

        Returns
        - if this score has been set before

        Raises
        - IllegalStateException: if the associated objective has been
            unregistered
        """
        ...


    def getScoreboard(self) -> "Scoreboard":
        """
        Gets the scoreboard for the associated objective.

        Returns
        - the owning objective's scoreboard, or null if it has been
            Objective.unregister() unregistered
        """
        ...
