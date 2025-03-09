"""
Python module generated from Java source file org.bukkit.event.player.PlayerStatisticIncrementEvent

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Bukkit
from org.bukkit import Material
from org.bukkit import Statistic
from org.bukkit.entity import EntityType
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from org.bukkit.material import MaterialData
from typing import Any, Callable, Iterable, Tuple


class PlayerStatisticIncrementEvent(PlayerEvent, Cancellable):
    """
    Called when a player statistic is incremented.
    
    This event is not called for some high frequency statistics, e.g. movement
    based statistics.
    """

    def __init__(self, player: "Player", statistic: "Statistic", initialValue: int, newValue: int):
        ...


    def __init__(self, player: "Player", statistic: "Statistic", initialValue: int, newValue: int, entityType: "EntityType"):
        ...


    def __init__(self, player: "Player", statistic: "Statistic", initialValue: int, newValue: int, material: "Material"):
        ...


    def getStatistic(self) -> "Statistic":
        """
        Gets the statistic that is being incremented.

        Returns
        - the incremented statistic
        """
        ...


    def getPreviousValue(self) -> int:
        """
        Gets the previous value of the statistic.

        Returns
        - the previous value of the statistic
        """
        ...


    def getNewValue(self) -> int:
        """
        Gets the new value of the statistic.

        Returns
        - the new value of the statistic
        """
        ...


    def getEntityType(self) -> "EntityType":
        """
        Gets the EntityType if .getStatistic() getStatistic() is an
        entity statistic otherwise returns null.

        Returns
        - the EntityType of the statistic
        """
        ...


    def getMaterial(self) -> "Material":
        """
        Gets the Material if .getStatistic() getStatistic() is a block
        or item statistic otherwise returns null.

        Returns
        - the Material of the statistic
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
