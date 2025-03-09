"""
Python module generated from Java source file org.bukkit.event.player.PlayerAdvancementDoneEvent

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.advancement import Advancement
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from typing import Any, Callable, Iterable, Tuple


class PlayerAdvancementDoneEvent(PlayerEvent):
    """
    Called when a player has completed all criteria in an advancement.
    """

    def __init__(self, who: "Player", advancement: "Advancement"):
        ...


    def getAdvancement(self) -> "Advancement":
        """
        Get the advancement which has been completed.

        Returns
        - completed advancement
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
