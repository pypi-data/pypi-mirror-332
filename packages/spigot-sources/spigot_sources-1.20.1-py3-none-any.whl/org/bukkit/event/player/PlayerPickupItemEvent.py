"""
Python module generated from Java source file org.bukkit.event.player.PlayerPickupItemEvent

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Warning
from org.bukkit.entity import Item
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import EntityPickupItemEvent
from org.bukkit.event.player import *
from typing import Any, Callable, Iterable, Tuple


class PlayerPickupItemEvent(PlayerEvent, Cancellable):
    """
    Thrown when a player picks an item up from the ground

    Deprecated
    - EntityPickupItemEvent
    """

    def __init__(self, player: "Player", item: "Item", remaining: int):
        ...


    def getItem(self) -> "Item":
        """
        Gets the Item picked up by the player.

        Returns
        - Item
        """
        ...


    def getRemaining(self) -> int:
        """
        Gets the amount remaining on the ground, if any

        Returns
        - amount remaining on the ground
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
