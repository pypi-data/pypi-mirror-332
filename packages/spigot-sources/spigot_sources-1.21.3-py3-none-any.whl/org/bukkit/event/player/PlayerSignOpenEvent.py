"""
Python module generated from Java source file org.bukkit.event.player.PlayerSignOpenEvent

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.block import Sign
from org.bukkit.block.sign import Side
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from typing import Any, Callable, Iterable, Tuple


class PlayerSignOpenEvent(PlayerEvent, Cancellable):
    """
    This event is fired when a sign is opened by the player.
    """

    def __init__(self, player: "Player", sign: "Sign", side: "Side", cause: "Cause"):
        ...


    def getSign(self) -> "Sign":
        """
        Gets the sign that was opened.

        Returns
        - opened sign
        """
        ...


    def getSide(self) -> "Side":
        """
        Gets side of the sign opened.

        Returns
        - side of sign opened
        """
        ...


    def getCause(self) -> "Cause":
        """
        Gets the cause of the sign open.

        Returns
        - sign open cause
        """
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...


    class Cause(Enum):

        INTERACT = 0
        """
        Indicate the sign was opened because of an interaction.
        """
        PLACE = 1
        """
        Indicate the sign was opened because the sign was placed.
        """
        PLUGIN = 2
        """
        Indicate the sign was opened because of a plugin.
        """
        UNKNOWN = 3
        """
        Indicate the sign was opened for an unknown reason.
        """
