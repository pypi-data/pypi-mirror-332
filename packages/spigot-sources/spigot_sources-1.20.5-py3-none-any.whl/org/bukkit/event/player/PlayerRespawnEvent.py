"""
Python module generated from Java source file org.bukkit.event.player.PlayerRespawnEvent

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from enum import Enum
from org.bukkit import Location
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from typing import Any, Callable, Iterable, Tuple


class PlayerRespawnEvent(PlayerEvent):
    """
    Called when a player respawns.
    """

    def __init__(self, respawnPlayer: "Player", respawnLocation: "Location", isBedSpawn: bool):
        ...


    def __init__(self, respawnPlayer: "Player", respawnLocation: "Location", isBedSpawn: bool, isAnchorSpawn: bool):
        ...


    def __init__(self, respawnPlayer: "Player", respawnLocation: "Location", isBedSpawn: bool, isAnchorSpawn: bool, respawnReason: "RespawnReason"):
        ...


    def getRespawnLocation(self) -> "Location":
        """
        Gets the current respawn location

        Returns
        - Location current respawn location
        """
        ...


    def setRespawnLocation(self, respawnLocation: "Location") -> None:
        """
        Sets the new respawn location

        Arguments
        - respawnLocation: new location for the respawn
        """
        ...


    def isBedSpawn(self) -> bool:
        """
        Gets whether the respawn location is the player's bed.

        Returns
        - True if the respawn location is the player's bed.
        """
        ...


    def isAnchorSpawn(self) -> bool:
        """
        Gets whether the respawn location is the player's respawn anchor.

        Returns
        - True if the respawn location is the player's respawn anchor.
        """
        ...


    def getRespawnReason(self) -> "RespawnReason":
        """
        Gets the reason this respawn event was called.

        Returns
        - the reason the event was called.
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...


    class RespawnReason(Enum):
        """
        An enum to specify the reason a respawn event was called.
        """

        DEATH = 0
        """
        When the player dies and presses the respawn button.
        """
        END_PORTAL = 1
        """
        When the player exits the end through the end portal.
        """
        PLUGIN = 2
        """
        When a plugin respawns the player.
        """
