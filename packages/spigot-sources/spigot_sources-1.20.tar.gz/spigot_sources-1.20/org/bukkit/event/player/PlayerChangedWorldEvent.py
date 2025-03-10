"""
Python module generated from Java source file org.bukkit.event.player.PlayerChangedWorldEvent

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import World
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from typing import Any, Callable, Iterable, Tuple


class PlayerChangedWorldEvent(PlayerEvent):
    """
    Called when a player switches to another world.
    """

    def __init__(self, player: "Player", from: "World"):
        ...


    def getFrom(self) -> "World":
        """
        Gets the world the player is switching from.

        Returns
        - player's previous world
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
