"""
Python module generated from Java source file org.bukkit.event.player.PlayerBedLeaveEvent

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Location
from org.bukkit.block import Block
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from typing import Any, Callable, Iterable, Tuple


class PlayerBedLeaveEvent(PlayerEvent, Cancellable):
    """
    This event is fired when the player is leaving a bed.
    """

    def __init__(self, who: "Player", bed: "Block", setBedSpawn: bool):
        ...


    def getBed(self) -> "Block":
        """
        Returns the bed block involved in this event.

        Returns
        - the bed block involved in this event
        """
        ...


    def shouldSetSpawnLocation(self) -> bool:
        """
        Get if this event should set the new spawn location for the
        Player.
        
        This does not remove any existing spawn location, only prevent it from
        being changed (if True).
        
        To change a Player's spawn location, use
        Player.setBedSpawnLocation(Location).

        Returns
        - True if the spawn location will be changed
        """
        ...


    def setSpawnLocation(self, setBedSpawn: bool) -> None:
        """
        Set if this event should set the new spawn location for the
        Player.
        
        This will not remove any existing spawn location, only prevent it from
        being changed (if True).
        
        To change a Player's spawn location, use
        Player.setBedSpawnLocation(Location).

        Arguments
        - setBedSpawn: True to change the new spawn location
        """
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancelled: bool) -> None:
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
