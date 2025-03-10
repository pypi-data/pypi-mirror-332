"""
Python module generated from Java source file org.bukkit.scoreboard.Scoreboard

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import OfflinePlayer
from org.bukkit.scoreboard import *
from typing import Any, Callable, Iterable, Tuple


class Scoreboard:
    """
    A scoreboard
    """

    def registerNewObjective(self, name: str, criteria: str) -> "Objective":
        """
        Registers an Objective on this Scoreboard

        Arguments
        - name: Name of the Objective
        - criteria: Criteria for the Objective

        Returns
        - The registered Objective

        Raises
        - IllegalArgumentException: if name is longer than 32767
            characters.
        - IllegalArgumentException: if an objective by that name already
            exists

        Deprecated
        - a displayName should be explicitly specified
        """
        ...


    def registerNewObjective(self, name: str, criteria: str, displayName: str) -> "Objective":
        """
        Registers an Objective on this Scoreboard

        Arguments
        - name: Name of the Objective
        - criteria: Criteria for the Objective
        - displayName: Name displayed to players for the Objective.

        Returns
        - The registered Objective

        Raises
        - IllegalArgumentException: if name is longer than 32767
            characters.
        - IllegalArgumentException: if an objective by that name already
            exists

        Deprecated
        - use .registerNewObjective(String, Criteria, String)
        """
        ...


    def registerNewObjective(self, name: str, criteria: str, displayName: str, renderType: "RenderType") -> "Objective":
        """
        Registers an Objective on this Scoreboard

        Arguments
        - name: Name of the Objective
        - criteria: Criteria for the Objective
        - displayName: Name displayed to players for the Objective.
        - renderType: Manner of rendering the Objective

        Returns
        - The registered Objective

        Raises
        - IllegalArgumentException: if name is longer than 32767
            characters.
        - IllegalArgumentException: if an objective by that name already
            exists

        Deprecated
        - use .registerNewObjective(String, Criteria, String, RenderType)
        """
        ...


    def registerNewObjective(self, name: str, criteria: "Criteria", displayName: str) -> "Objective":
        """
        Registers an Objective on this Scoreboard

        Arguments
        - name: Name of the Objective
        - criteria: Criteria for the Objective
        - displayName: Name displayed to players for the Objective.

        Returns
        - The registered Objective

        Raises
        - IllegalArgumentException: if name is longer than 32767
            characters.
        - IllegalArgumentException: if an objective by that name already
            exists
        """
        ...


    def registerNewObjective(self, name: str, criteria: "Criteria", displayName: str, renderType: "RenderType") -> "Objective":
        """
        Registers an Objective on this Scoreboard

        Arguments
        - name: Name of the Objective
        - criteria: Criteria for the Objective
        - displayName: Name displayed to players for the Objective.
        - renderType: Manner of rendering the Objective

        Returns
        - The registered Objective

        Raises
        - IllegalArgumentException: if name is longer than 32767
            characters.
        - IllegalArgumentException: if an objective by that name already
            exists
        """
        ...


    def getObjective(self, name: str) -> "Objective":
        """
        Gets an Objective on this Scoreboard by name

        Arguments
        - name: Name of the Objective

        Returns
        - the Objective or null if it does not exist
        """
        ...


    def getObjectivesByCriteria(self, criteria: str) -> set["Objective"]:
        """
        Gets all Objectives of a Criteria on the Scoreboard

        Arguments
        - criteria: Criteria to search by

        Returns
        - an immutable set of Objectives using the specified Criteria

        Deprecated
        - use .getObjectivesByCriteria(Criteria)
        """
        ...


    def getObjectivesByCriteria(self, criteria: "Criteria") -> set["Objective"]:
        """
        Gets all Objectives of a Criteria on the Scoreboard

        Arguments
        - criteria: Criteria to search by

        Returns
        - an immutable set of Objectives using the specified Criteria
        """
        ...


    def getObjectives(self) -> set["Objective"]:
        """
        Gets all Objectives on this Scoreboard

        Returns
        - An immutable set of all Objectives on this Scoreboard
        """
        ...


    def getObjective(self, slot: "DisplaySlot") -> "Objective":
        """
        Gets the Objective currently displayed in a DisplaySlot on this
        Scoreboard

        Arguments
        - slot: The DisplaySlot

        Returns
        - the Objective currently displayed or null if nothing is
            displayed in that DisplaySlot
        """
        ...


    def getScores(self, player: "OfflinePlayer") -> set["Score"]:
        """
        Gets all scores for a player on this Scoreboard

        Arguments
        - player: the player whose scores are being retrieved

        Returns
        - immutable set of all scores tracked for the player

        See
        - .getScores(String)

        Deprecated
        - Scoreboards can contain entries that aren't players
        """
        ...


    def getScores(self, entry: str) -> set["Score"]:
        """
        Gets all scores for an entry on this Scoreboard

        Arguments
        - entry: the entry whose scores are being retrieved

        Returns
        - immutable set of all scores tracked for the entry
        """
        ...


    def resetScores(self, player: "OfflinePlayer") -> None:
        """
        Removes all scores for a player on this Scoreboard

        Arguments
        - player: the player to drop all current scores for

        See
        - .resetScores(String)

        Deprecated
        - Scoreboards can contain entries that aren't players
        """
        ...


    def resetScores(self, entry: str) -> None:
        """
        Removes all scores for an entry on this Scoreboard

        Arguments
        - entry: the entry to drop all current scores for
        """
        ...


    def getPlayerTeam(self, player: "OfflinePlayer") -> "Team":
        """
        Gets a player's Team on this Scoreboard

        Arguments
        - player: the player to search for

        Returns
        - the player's Team or null if the player is not on a team

        See
        - .getEntryTeam(String)

        Deprecated
        - Scoreboards can contain entries that aren't players
        """
        ...


    def getEntryTeam(self, entry: str) -> "Team":
        """
        Gets a entries Team on this Scoreboard

        Arguments
        - entry: the entry to search for

        Returns
        - the entries Team or null if the entry is not on a team
        """
        ...


    def getTeam(self, teamName: str) -> "Team":
        """
        Gets a Team by name on this Scoreboard

        Arguments
        - teamName: Team name

        Returns
        - the matching Team or null if no matches
        """
        ...


    def getTeams(self) -> set["Team"]:
        """
        Gets all teams on this Scoreboard

        Returns
        - an immutable set of Teams
        """
        ...


    def registerNewTeam(self, name: str) -> "Team":
        """
        Registers a Team on this Scoreboard

        Arguments
        - name: Team name

        Returns
        - registered Team

        Raises
        - IllegalArgumentException: if team by that name already exists
        """
        ...


    def getPlayers(self) -> set["OfflinePlayer"]:
        """
        Gets all players tracked by this Scoreboard

        Returns
        - immutable set of all tracked players

        See
        - .getEntries()

        Deprecated
        - Scoreboards can contain entries that aren't players
        """
        ...


    def getEntries(self) -> set[str]:
        """
        Gets all entries tracked by this Scoreboard

        Returns
        - immutable set of all tracked entries
        """
        ...


    def clearSlot(self, slot: "DisplaySlot") -> None:
        """
        Clears any objective in the specified slot.

        Arguments
        - slot: the slot to remove objectives
        """
        ...
