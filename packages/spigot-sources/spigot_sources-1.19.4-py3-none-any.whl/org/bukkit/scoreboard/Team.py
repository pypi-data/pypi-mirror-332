"""
Python module generated from Java source file org.bukkit.scoreboard.Team

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit import ChatColor
from org.bukkit import OfflinePlayer
from org.bukkit.potion import PotionEffectType
from org.bukkit.scoreboard import *
from typing import Any, Callable, Iterable, Tuple


class Team:
    """
    A team on a scoreboard that has a common display theme and other
    properties. This team is only relevant to the display of the associated
    .getScoreboard() scoreboard.
    """

    def getName(self) -> str:
        """
        Gets the name of this Team

        Returns
        - Objective name

        Raises
        - IllegalStateException: if this team has been unregistered
        """
        ...


    def getDisplayName(self) -> str:
        """
        Gets the name displayed to entries for this team

        Returns
        - Team display name

        Raises
        - IllegalStateException: if this team has been unregistered
        """
        ...


    def setDisplayName(self, displayName: str) -> None:
        """
        Sets the name displayed to entries for this team

        Arguments
        - displayName: New display name

        Raises
        - IllegalArgumentException: if displayName is longer than 128
            characters.
        - IllegalStateException: if this team has been unregistered
        """
        ...


    def getPrefix(self) -> str:
        """
        Gets the prefix prepended to the display of entries on this team.

        Returns
        - Team prefix

        Raises
        - IllegalStateException: if this team has been unregistered
        """
        ...


    def setPrefix(self, prefix: str) -> None:
        """
        Sets the prefix prepended to the display of entries on this team.

        Arguments
        - prefix: New prefix

        Raises
        - IllegalArgumentException: if prefix is null
        - IllegalArgumentException: if prefix is longer than 64
            characters
        - IllegalStateException: if this team has been unregistered
        """
        ...


    def getSuffix(self) -> str:
        """
        Gets the suffix appended to the display of entries on this team.

        Returns
        - the team's current suffix

        Raises
        - IllegalStateException: if this team has been unregistered
        """
        ...


    def setSuffix(self, suffix: str) -> None:
        """
        Sets the suffix appended to the display of entries on this team.

        Arguments
        - suffix: the new suffix for this team.

        Raises
        - IllegalArgumentException: if suffix is null
        - IllegalArgumentException: if suffix is longer than 64
            characters
        - IllegalStateException: if this team has been unregistered
        """
        ...


    def getColor(self) -> "ChatColor":
        """
        Gets the color of the team.
        
        This only sets the team outline, other occurrences of colors such as in
        names are handled by prefixes / suffixes.

        Returns
        - team color, defaults to ChatColor.RESET

        Raises
        - IllegalStateException: if this team has been unregistered
        """
        ...


    def setColor(self, color: "ChatColor") -> None:
        """
        Sets the color of the team.
        
        This only sets the team outline, other occurrences of colors such as in
        names are handled by prefixes / suffixes.

        Arguments
        - color: new color, must be non-null. Use ChatColor.RESET for
        no color
        """
        ...


    def allowFriendlyFire(self) -> bool:
        """
        Gets the team friendly fire state

        Returns
        - True if friendly fire is enabled

        Raises
        - IllegalStateException: if this team has been unregistered
        """
        ...


    def setAllowFriendlyFire(self, enabled: bool) -> None:
        """
        Sets the team friendly fire state

        Arguments
        - enabled: True if friendly fire is to be allowed

        Raises
        - IllegalStateException: if this team has been unregistered
        """
        ...


    def canSeeFriendlyInvisibles(self) -> bool:
        """
        Gets the team's ability to see PotionEffectType.INVISIBILITY
        invisible teammates.

        Returns
        - True if team members can see invisible members

        Raises
        - IllegalStateException: if this team has been unregistered
        """
        ...


    def setCanSeeFriendlyInvisibles(self, enabled: bool) -> None:
        """
        Sets the team's ability to see PotionEffectType.INVISIBILITY
        invisible teammates.

        Arguments
        - enabled: True if invisible teammates are to be visible

        Raises
        - IllegalStateException: if this team has been unregistered
        """
        ...


    def getNameTagVisibility(self) -> "NameTagVisibility":
        """
        Gets the team's ability to see name tags

        Returns
        - the current name tag visibility for the team

        Raises
        - IllegalArgumentException: if this team has been unregistered

        Deprecated
        - see .getOption(org.bukkit.scoreboard.Team.Option)
        """
        ...


    def setNameTagVisibility(self, visibility: "NameTagVisibility") -> None:
        """
        Set's the team's ability to see name tags

        Arguments
        - visibility: The nameTagVisibility to set

        Raises
        - IllegalArgumentException: if this team has been unregistered

        Deprecated
        - see
        .setOption(org.bukkit.scoreboard.Team.Option, org.bukkit.scoreboard.Team.OptionStatus)
        """
        ...


    def getPlayers(self) -> set["OfflinePlayer"]:
        """
        Gets the Set of players on the team

        Returns
        - players on the team

        Raises
        - IllegalStateException: if this team has been unregistered

        See
        - .getEntries()

        Deprecated
        - Teams can contain entries that aren't players
        """
        ...


    def getEntries(self) -> set[str]:
        """
        Gets the Set of entries on the team

        Returns
        - entries on the team

        Raises
        - IllegalStateException: if this entries has been unregistered\
        """
        ...


    def getSize(self) -> int:
        """
        Gets the size of the team

        Returns
        - number of entries on the team

        Raises
        - IllegalStateException: if this team has been unregistered
        """
        ...


    def getScoreboard(self) -> "Scoreboard":
        """
        Gets the Scoreboard to which this team is attached

        Returns
        - Owning scoreboard, or null if this team has been .unregister() unregistered
        """
        ...


    def addPlayer(self, player: "OfflinePlayer") -> None:
        """
        This puts the specified player onto this team for the scoreboard.
        
        This will remove the player from any other team on the scoreboard.

        Arguments
        - player: the player to add

        Raises
        - IllegalArgumentException: if player is null
        - IllegalStateException: if this team has been unregistered

        See
        - .addEntry(String)

        Deprecated
        - Teams can contain entries that aren't players
        """
        ...


    def addEntry(self, entry: str) -> None:
        """
        This puts the specified entry onto this team for the scoreboard.
        
        This will remove the entry from any other team on the scoreboard.

        Arguments
        - entry: the entry to add

        Raises
        - IllegalArgumentException: if entry is null
        - IllegalStateException: if this team has been unregistered
        """
        ...


    def removePlayer(self, player: "OfflinePlayer") -> bool:
        """
        Removes the player from this team.

        Arguments
        - player: the player to remove

        Returns
        - if the player was on this team

        Raises
        - IllegalArgumentException: if player is null
        - IllegalStateException: if this team has been unregistered

        See
        - .removeEntry(String)

        Deprecated
        - Teams can contain entries that aren't players
        """
        ...


    def removeEntry(self, entry: str) -> bool:
        """
        Removes the entry from this team.

        Arguments
        - entry: the entry to remove

        Returns
        - if the entry was a part of this team

        Raises
        - IllegalArgumentException: if entry is null
        - IllegalStateException: if this team has been unregistered
        """
        ...


    def unregister(self) -> None:
        """
        Unregisters this team from the Scoreboard

        Raises
        - IllegalStateException: if this team has been unregistered
        """
        ...


    def hasPlayer(self, player: "OfflinePlayer") -> bool:
        """
        Checks to see if the specified player is a member of this team.

        Arguments
        - player: the player to search for

        Returns
        - True if the player is a member of this team

        Raises
        - IllegalArgumentException: if player is null
        - IllegalStateException: if this team has been unregistered

        See
        - .hasEntry(String)

        Deprecated
        - Teams can contain entries that aren't players
        """
        ...


    def hasEntry(self, entry: str) -> bool:
        """
        Checks to see if the specified entry is a member of this team.

        Arguments
        - entry: the entry to search for

        Returns
        - True if the entry is a member of this team

        Raises
        - IllegalArgumentException: if entry is null
        - IllegalStateException: if this team has been unregistered
        """
        ...


    def getOption(self, option: "Option") -> "OptionStatus":
        """
        Get an option for this team

        Arguments
        - option: the option to get

        Returns
        - the option status

        Raises
        - IllegalStateException: if this team has been unregistered
        """
        ...


    def setOption(self, option: "Option", status: "OptionStatus") -> None:
        """
        Set an option for this team

        Arguments
        - option: the option to set
        - status: the new option status

        Raises
        - IllegalStateException: if this team has been unregistered
        """
        ...


    class Option(Enum):
        """
        Represents an option which may be applied to this team.
        """

        NAME_TAG_VISIBILITY = 0
        """
        How to display the name tags of players on this team.
        """
        DEATH_MESSAGE_VISIBILITY = 1
        """
        How to display the death messages for players on this team.
        """
        COLLISION_RULE = 2
        """
        How players of this team collide with others.
        """


    class OptionStatus(Enum):
        """
        How an option may be applied to members of this team.
        """

        ALWAYS = 0
        """
        Apply this option to everyone.
        """
        NEVER = 1
        """
        Never apply this option.
        """
        FOR_OTHER_TEAMS = 2
        """
        Apply this option only for opposing teams.
        """
        FOR_OWN_TEAM = 3
        """
        Apply this option for only team members.
        """
