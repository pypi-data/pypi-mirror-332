"""
Python module generated from Java source file org.bukkit.event.block.CauldronLevelChangeEvent

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from enum import Enum
from org.bukkit.block import Block
from org.bukkit.entity import Entity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.block import *
from typing import Any, Callable, Iterable, Tuple


class CauldronLevelChangeEvent(BlockEvent, Cancellable):

    def __init__(self, block: "Block", entity: "Entity", reason: "ChangeReason", oldLevel: int, newLevel: int):
        ...


    def getEntity(self) -> "Entity":
        """
        Get entity which did this. May be null.

        Returns
        - acting entity
        """
        ...


    def getReason(self) -> "ChangeReason":
        ...


    def getOldLevel(self) -> int:
        ...


    def getNewLevel(self) -> int:
        ...


    def setNewLevel(self, newLevel: int) -> None:
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancelled: bool) -> None:
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...


    class ChangeReason(Enum):

        BUCKET_FILL = 0
        """
        Player emptying the cauldron by filling their bucket.
        """
        BUCKET_EMPTY = 1
        """
        Player filling the cauldron by emptying their bucket.
        """
        BOTTLE_FILL = 2
        """
        Player emptying the cauldron by filling their bottle.
        """
        BOTTLE_EMPTY = 3
        """
        Player filling the cauldron by emptying their bottle.
        """
        BANNER_WASH = 4
        """
        Player cleaning their banner.
        """
        ARMOR_WASH = 5
        """
        Player cleaning their armor.
        """
        EXTINGUISH = 6
        """
        Entity being extinguished.
        """
        EVAPORATE = 7
        """
        Evaporating due to biome dryness.
        """
        UNKNOWN = 8
        """
        Unknown.
        """
