"""
Python module generated from Java source file org.bukkit.event.player.PlayerLocaleChangeEvent

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from typing import Any, Callable, Iterable, Tuple


class PlayerLocaleChangeEvent(PlayerEvent):
    """
    Called when a player changes their locale in the client settings.
    """

    def __init__(self, who: "Player", locale: str):
        ...


    def getLocale(self) -> str:
        """
        Returns
        - the player's new locale

        See
        - Player.getLocale()
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
