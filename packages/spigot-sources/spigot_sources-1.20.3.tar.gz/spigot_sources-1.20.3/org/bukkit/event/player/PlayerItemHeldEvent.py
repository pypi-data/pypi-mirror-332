"""
Python module generated from Java source file org.bukkit.event.player.PlayerItemHeldEvent

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from typing import Any, Callable, Iterable, Tuple


class PlayerItemHeldEvent(PlayerEvent, Cancellable):
    """
    Fired when a player changes their currently held item
    """

    def __init__(self, player: "Player", previous: int, current: int):
        ...


    def getPreviousSlot(self) -> int:
        """
        Gets the previous held slot index

        Returns
        - Previous slot index
        """
        ...


    def getNewSlot(self) -> int:
        """
        Gets the new held slot index

        Returns
        - New slot index
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
