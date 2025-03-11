"""
Python module generated from Java source file org.bukkit.event.player.PlayerDropItemEvent

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Item
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from typing import Any, Callable, Iterable, Tuple


class PlayerDropItemEvent(PlayerEvent, Cancellable):
    """
    Thrown when a player drops an item from their inventory
    """

    def __init__(self, player: "Player", drop: "Item"):
        ...


    def getItemDrop(self) -> "Item":
        """
        Gets the ItemDrop created by the player

        Returns
        - ItemDrop created by the player
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
