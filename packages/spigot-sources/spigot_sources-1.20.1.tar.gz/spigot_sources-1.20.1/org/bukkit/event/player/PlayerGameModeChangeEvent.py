"""
Python module generated from Java source file org.bukkit.event.player.PlayerGameModeChangeEvent

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import GameMode
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from typing import Any, Callable, Iterable, Tuple


class PlayerGameModeChangeEvent(PlayerEvent, Cancellable):
    """
    Called when the GameMode of the player is changed.
    """

    def __init__(self, player: "Player", newGameMode: "GameMode"):
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getNewGameMode(self) -> "GameMode":
        """
        Gets the GameMode the player is switched to.

        Returns
        - player's new GameMode
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
