"""
Python module generated from Java source file org.bukkit.event.raid.RaidTriggerEvent

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Raid
from org.bukkit import World
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.raid import *
from typing import Any, Callable, Iterable, Tuple


class RaidTriggerEvent(RaidEvent, Cancellable):
    """
    Called when a Raid is triggered (e.g: a player with Bad Omen effect
    enters a village).
    """

    def __init__(self, raid: "Raid", world: "World", player: "Player"):
        ...


    def getPlayer(self) -> "Player":
        """
        Returns the player who triggered the raid.

        Returns
        - triggering player
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
