"""
Python module generated from Java source file org.bukkit.event.raid.RaidSpawnWaveEvent

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Collections
from org.bukkit import Raid
from org.bukkit import World
from org.bukkit.entity import Raider
from org.bukkit.event import HandlerList
from org.bukkit.event.raid import *
from typing import Any, Callable, Iterable, Tuple


class RaidSpawnWaveEvent(RaidEvent):
    """
    Called when a raid wave spawns.
    """

    def __init__(self, raid: "Raid", world: "World", leader: "Raider", raiders: list["Raider"]):
        ...


    def getPatrolLeader(self) -> "Raider":
        """
        Returns the patrol leader.

        Returns
        - Raider
        """
        ...


    def getRaiders(self) -> list["Raider"]:
        """
        Returns all Raider that spawned in this wave.

        Returns
        - an immutable list of raiders
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
