"""
Python module generated from Java source file org.bukkit.event.player.PlayerLevelChangeEvent

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from typing import Any, Callable, Iterable, Tuple


class PlayerLevelChangeEvent(PlayerEvent):
    """
    Called when a players level changes
    """

    def __init__(self, player: "Player", oldLevel: int, newLevel: int):
        ...


    def getOldLevel(self) -> int:
        """
        Gets the old level of the player

        Returns
        - The old level of the player
        """
        ...


    def getNewLevel(self) -> int:
        """
        Gets the new level of the player

        Returns
        - The new (current) level of the player
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
