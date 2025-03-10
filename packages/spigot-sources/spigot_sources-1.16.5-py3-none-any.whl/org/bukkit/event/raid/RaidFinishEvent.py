"""
Python module generated from Java source file org.bukkit.event.raid.RaidFinishEvent

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Collections
from org.bukkit import Raid
from org.bukkit import World
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.raid import *
from typing import Any, Callable, Iterable, Tuple


class RaidFinishEvent(RaidEvent):
    """
    This event is called when a Raid was complete with a clear result.
    """

    def __init__(self, raid: "Raid", world: "World", winners: list["Player"]):
        ...


    def getWinners(self) -> list["Player"]:
        """
        Returns an immutable list contains all winners.
        
        **Note: Players who are considered as heroes but were not online at the
        end would not be included in this list.**

        Returns
        - winners
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
