"""
Python module generated from Java source file org.bukkit.event.player.PlayerQuitEvent

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from typing import Any, Callable, Iterable, Tuple


class PlayerQuitEvent(PlayerEvent):
    """
    Called when a player leaves a server
    """

    def __init__(self, who: "Player", quitMessage: str):
        ...


    def getQuitMessage(self) -> str:
        """
        Gets the quit message to send to all online players

        Returns
        - string quit message
        """
        ...


    def setQuitMessage(self, quitMessage: str) -> None:
        """
        Sets the quit message to send to all online players

        Arguments
        - quitMessage: quit message
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
