"""
Python module generated from Java source file org.bukkit.event.player.PlayerChangedMainHandEvent

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from org.bukkit.inventory import MainHand
from typing import Any, Callable, Iterable, Tuple


class PlayerChangedMainHandEvent(PlayerEvent):
    """
    Called when a player changes their main hand in the client settings.
    """

    def __init__(self, who: "Player", mainHand: "MainHand"):
        ...


    def getMainHand(self) -> "MainHand":
        """
        Gets the new main hand of the player. The old hand is still momentarily
        available via Player.getMainHand().

        Returns
        - the new MainHand of the player
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
