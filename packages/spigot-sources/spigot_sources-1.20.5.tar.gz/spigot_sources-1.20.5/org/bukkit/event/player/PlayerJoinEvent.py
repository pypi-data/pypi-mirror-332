"""
Python module generated from Java source file org.bukkit.event.player.PlayerJoinEvent

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from typing import Any, Callable, Iterable, Tuple


class PlayerJoinEvent(PlayerEvent):
    """
    Called when a player joins a server
    """

    def __init__(self, playerJoined: "Player", joinMessage: str):
        ...


    def getJoinMessage(self) -> str:
        """
        Gets the join message to send to all online players

        Returns
        - string join message. Can be null
        """
        ...


    def setJoinMessage(self, joinMessage: str) -> None:
        """
        Sets the join message to send to all online players

        Arguments
        - joinMessage: join message. If null, no message will be sent
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
