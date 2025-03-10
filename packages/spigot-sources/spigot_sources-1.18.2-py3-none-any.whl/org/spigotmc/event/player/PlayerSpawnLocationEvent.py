"""
Python module generated from Java source file org.spigotmc.event.player.PlayerSpawnLocationEvent

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Location
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import PlayerEvent
from org.spigotmc.event.player import *
from typing import Any, Callable, Iterable, Tuple


class PlayerSpawnLocationEvent(PlayerEvent):
    """
    Called when player is about to spawn in a world after joining the server.
    """

    def __init__(self, who: "Player", spawnLocation: "Location"):
        ...


    def getSpawnLocation(self) -> "Location":
        """
        Gets player's spawn location.
        If the player Player.hasPlayedBefore(), it's going to default to the location inside player.dat file.
        For new players, the default spawn location is spawn of the main Bukkit world.

        Returns
        - the spawn location
        """
        ...


    def setSpawnLocation(self, location: "Location") -> None:
        """
        Sets player's spawn location.

        Arguments
        - location: the spawn location
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
