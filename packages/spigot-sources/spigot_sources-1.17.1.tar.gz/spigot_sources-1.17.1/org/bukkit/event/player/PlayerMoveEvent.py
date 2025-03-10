"""
Python module generated from Java source file org.bukkit.event.player.PlayerMoveEvent

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from org.bukkit import Location
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from typing import Any, Callable, Iterable, Tuple


class PlayerMoveEvent(PlayerEvent, Cancellable):
    """
    Holds information for player movement events
    """

    def __init__(self, player: "Player", from: "Location", to: "Location"):
        ...


    def isCancelled(self) -> bool:
        """
        Gets the cancellation state of this event. A cancelled event will not
        be executed in the server, but will still pass to other plugins
        
        If a move or teleport event is cancelled, the player will be moved or
        teleported back to the Location as defined by getFrom(). This will not
        fire an event

        Returns
        - True if this event is cancelled
        """
        ...


    def setCancelled(self, cancel: bool) -> None:
        """
        Sets the cancellation state of this event. A cancelled event will not
        be executed in the server, but will still pass to other plugins
        
        If a move or teleport event is cancelled, the player will be moved or
        teleported back to the Location as defined by getFrom(). This will not
        fire an event

        Arguments
        - cancel: True if you wish to cancel this event
        """
        ...


    def getFrom(self) -> "Location":
        """
        Gets the location this player moved from

        Returns
        - Location the player moved from
        """
        ...


    def setFrom(self, from: "Location") -> None:
        """
        Sets the location to mark as where the player moved from

        Arguments
        - from: New location to mark as the players previous location
        """
        ...


    def getTo(self) -> "Location":
        """
        Gets the location this player moved to

        Returns
        - Location the player moved to
        """
        ...


    def setTo(self, to: "Location") -> None:
        """
        Sets the location that this player will move to

        Arguments
        - to: New Location this player will move to
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
