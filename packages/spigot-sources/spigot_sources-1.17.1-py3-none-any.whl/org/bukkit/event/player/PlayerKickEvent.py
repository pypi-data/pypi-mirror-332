"""
Python module generated from Java source file org.bukkit.event.player.PlayerKickEvent

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from typing import Any, Callable, Iterable, Tuple


class PlayerKickEvent(PlayerEvent, Cancellable):
    """
    Called when a player gets kicked from the server
    """

    def __init__(self, playerKicked: "Player", kickReason: str, leaveMessage: str):
        ...


    def getReason(self) -> str:
        """
        Gets the reason why the player is getting kicked

        Returns
        - string kick reason
        """
        ...


    def getLeaveMessage(self) -> str:
        """
        Gets the leave message send to all online players

        Returns
        - string kick reason
        """
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def setReason(self, kickReason: str) -> None:
        """
        Sets the reason why the player is getting kicked

        Arguments
        - kickReason: kick reason
        """
        ...


    def setLeaveMessage(self, leaveMessage: str) -> None:
        """
        Sets the leave message send to all online players

        Arguments
        - leaveMessage: leave message
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
