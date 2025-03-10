"""
Python module generated from Java source file org.bukkit.event.block.CauldronLevelChangeEvent

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from enum import Enum
from org.bukkit import Material
from org.bukkit.block import Block
from org.bukkit.block import BlockState
from org.bukkit.block.data import BlockData
from org.bukkit.block.data import Levelled
from org.bukkit.entity import Entity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.block import *
from typing import Any, Callable, Iterable, Tuple


class CauldronLevelChangeEvent(BlockEvent, Cancellable):

    def __init__(self, block: "Block", entity: "Entity", reason: "ChangeReason", newBlock: "BlockState"):
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


    def getNewState(self) -> "BlockState":
        """
        Gets the new state of the cauldron.

        Returns
        - The block state of the block that will be changed
        """
        ...


    def getOldLevel(self) -> int:
        """
        Gets the old level of the cauldron.

        Returns
        - old level

        See
        - .getBlock()

        Deprecated
        - not all cauldron contents are Levelled
        """
        ...


    def getNewLevel(self) -> int:
        """
        Gets the new level of the cauldron.

        Returns
        - new level

        See
        - .getNewState()

        Deprecated
        - not all cauldron contents are Levelled
        """
        ...


    def setNewLevel(self, newLevel: int) -> None:
        """
        Sets the new level of the cauldron.

        Arguments
        - newLevel: new level

        See
        - .getNewState()

        Deprecated
        - not all cauldron contents are Levelled
        """
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
        SHULKER_WASH = 6
        """
        Player cleaning a shulker box.
        """
        EXTINGUISH = 7
        """
        Entity being extinguished.
        """
        EVAPORATE = 8
        """
        Evaporating due to biome dryness.
        """
        NATURAL_FILL = 9
        """
        Filling due to natural fluid sources, eg rain or dripstone.
        """
        UNKNOWN = 10
        """
        Unknown.
        """
