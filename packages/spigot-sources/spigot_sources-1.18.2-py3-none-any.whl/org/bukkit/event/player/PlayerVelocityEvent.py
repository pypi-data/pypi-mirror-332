"""
Python module generated from Java source file org.bukkit.event.player.PlayerVelocityEvent

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from org.bukkit.util import Vector
from typing import Any, Callable, Iterable, Tuple


class PlayerVelocityEvent(PlayerEvent, Cancellable):
    """
    Called when the velocity of a player changes.
    """

    def __init__(self, player: "Player", velocity: "Vector"):
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getVelocity(self) -> "Vector":
        """
        Gets the velocity vector that will be sent to the player

        Returns
        - Vector the player will get
        """
        ...


    def setVelocity(self, velocity: "Vector") -> None:
        """
        Sets the velocity vector in meters per tick that will be sent to the player

        Arguments
        - velocity: The velocity vector that will be sent to the player
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
