"""
Python module generated from Java source file org.bukkit.boss.BossBar

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.boss import *
from org.bukkit.entity import Player
from typing import Any, Callable, Iterable, Tuple


class BossBar:

    def getTitle(self) -> str:
        """
        Returns the title of this boss bar

        Returns
        - the title of the bar
        """
        ...


    def setTitle(self, title: str) -> None:
        """
        Sets the title of this boss bar

        Arguments
        - title: the title of the bar
        """
        ...


    def getColor(self) -> "BarColor":
        """
        Returns the color of this boss bar

        Returns
        - the color of the bar
        """
        ...


    def setColor(self, color: "BarColor") -> None:
        """
        Sets the color of this boss bar.

        Arguments
        - color: the color of the bar
        """
        ...


    def getStyle(self) -> "BarStyle":
        """
        Returns the style of this boss bar

        Returns
        - the style of the bar
        """
        ...


    def setStyle(self, style: "BarStyle") -> None:
        """
        Sets the bar style of this boss bar

        Arguments
        - style: the style of the bar
        """
        ...


    def removeFlag(self, flag: "BarFlag") -> None:
        """
        Remove an existing flag on this boss bar

        Arguments
        - flag: the existing flag to remove
        """
        ...


    def addFlag(self, flag: "BarFlag") -> None:
        """
        Add an optional flag to this boss bar

        Arguments
        - flag: an optional flag to set on the boss bar
        """
        ...


    def hasFlag(self, flag: "BarFlag") -> bool:
        """
        Returns whether this boss bar as the passed flag set

        Arguments
        - flag: the flag to check

        Returns
        - whether it has the flag
        """
        ...


    def setProgress(self, progress: float) -> None:
        """
        Sets the progress of the bar. Values should be between 0.0 (empty) and
        1.0 (full)

        Arguments
        - progress: the progress of the bar
        """
        ...


    def getProgress(self) -> float:
        """
        Returns the progress of the bar between 0.0 and 1.0

        Returns
        - the progress of the bar
        """
        ...


    def addPlayer(self, player: "Player") -> None:
        """
        Adds the player to this boss bar causing it to display on their screen.

        Arguments
        - player: the player to add
        """
        ...


    def removePlayer(self, player: "Player") -> None:
        """
        Removes the player from this boss bar causing it to be removed from their
        screen.

        Arguments
        - player: the player to remove
        """
        ...


    def removeAll(self) -> None:
        """
        Removes all players from this boss bar

        See
        - .removePlayer(Player)
        """
        ...


    def getPlayers(self) -> list["Player"]:
        """
        Returns all players viewing this boss bar

        Returns
        - a immutable list of players
        """
        ...


    def setVisible(self, visible: bool) -> None:
        """
        Set if the boss bar is displayed to attached players.

        Arguments
        - visible: visible status
        """
        ...


    def isVisible(self) -> bool:
        """
        Return if the boss bar is displayed to attached players.

        Returns
        - visible status
        """
        ...


    def show(self) -> None:
        """
        Shows the previously hidden boss bar to all attached players

        Deprecated
        - .setVisible(boolean)
        """
        ...


    def hide(self) -> None:
        """
        Hides this boss bar from all attached players

        Deprecated
        - .setVisible(boolean)
        """
        ...
