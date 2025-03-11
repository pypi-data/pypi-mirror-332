"""
Python module generated from Java source file org.bukkit.scoreboard.Objective

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import OfflinePlayer
from org.bukkit.scoreboard import *
from typing import Any, Callable, Iterable, Tuple


class Objective:
    """
    An objective on a scoreboard that can show scores specific to entries. This
    objective is only relevant to the display of the associated .getScoreboard() scoreboard.
    """

    def getName(self) -> str:
        """
        Gets the name of this Objective

        Returns
        - this objective's name

        Raises
        - IllegalStateException: if this objective has been unregistered
        """
        ...


    def getDisplayName(self) -> str:
        """
        Gets the name displayed to players for this objective

        Returns
        - this objective's display name

        Raises
        - IllegalStateException: if this objective has been unregistered
        """
        ...


    def setDisplayName(self, displayName: str) -> None:
        """
        Sets the name displayed to players for this objective.

        Arguments
        - displayName: Display name to set

        Raises
        - IllegalStateException: if this objective has been unregistered
        """
        ...


    def getCriteria(self) -> str:
        """
        Gets the criteria this objective tracks.

        Returns
        - this objective's criteria

        Raises
        - IllegalStateException: if this objective has been unregistered

        Deprecated
        - use .getTrackedCriteria()
        """
        ...


    def getTrackedCriteria(self) -> "Criteria":
        """
        Gets the criteria this objective tracks.

        Returns
        - this objective's criteria

        Raises
        - IllegalStateException: if this objective has been unregistered
        """
        ...


    def isModifiable(self) -> bool:
        """
        Gets if the objective's scores can be modified directly by a plugin.

        Returns
        - True if scores are modifiable

        Raises
        - IllegalStateException: if this objective has been unregistered

        See
        - Criterias.HEALTH
        """
        ...


    def getScoreboard(self) -> "Scoreboard":
        """
        Gets the scoreboard to which this objective is attached.

        Returns
        - Owning scoreboard, or null if it has been .unregister()
            unregistered
        """
        ...


    def unregister(self) -> None:
        """
        Unregisters this objective from the Scoreboard scoreboard.

        Raises
        - IllegalStateException: if this objective has been unregistered
        """
        ...


    def setDisplaySlot(self, slot: "DisplaySlot") -> None:
        """
        Sets this objective to display on the specified slot for the
        scoreboard, removing it from any other display slot.

        Arguments
        - slot: display slot to change, or null to not display

        Raises
        - IllegalStateException: if this objective has been unregistered
        """
        ...


    def getDisplaySlot(self) -> "DisplaySlot":
        """
        Gets the display slot this objective is displayed at.

        Returns
        - the display slot for this objective, or null if not displayed

        Raises
        - IllegalStateException: if this objective has been unregistered
        """
        ...


    def setRenderType(self, renderType: "RenderType") -> None:
        """
        Sets manner in which this objective will be rendered.

        Arguments
        - renderType: new render type

        Raises
        - IllegalStateException: if this objective has been unregistered
        """
        ...


    def getRenderType(self) -> "RenderType":
        """
        Sets manner in which this objective will be rendered.

        Returns
        - the render type

        Raises
        - IllegalStateException: if this objective has been unregistered
        """
        ...


    def getScore(self, player: "OfflinePlayer") -> "Score":
        """
        Gets a player's Score for an Objective on this Scoreboard

        Arguments
        - player: Player for the Score

        Returns
        - Score tracking the Objective and player specified

        Raises
        - IllegalStateException: if this objective has been unregistered

        See
        - .getScore(String)

        Deprecated
        - Scoreboards can contain entries that aren't players
        """
        ...


    def getScore(self, entry: str) -> "Score":
        """
        Gets an entry's Score for an Objective on this Scoreboard.

        Arguments
        - entry: Entry for the Score

        Returns
        - Score tracking the Objective and entry specified

        Raises
        - IllegalStateException: if this objective has been unregistered
        - IllegalArgumentException: if entry is longer than 32767 characters.
        """
        ...
