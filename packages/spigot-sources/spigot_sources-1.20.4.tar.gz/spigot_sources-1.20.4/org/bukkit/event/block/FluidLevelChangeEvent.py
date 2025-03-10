"""
Python module generated from Java source file org.bukkit.event.block.FluidLevelChangeEvent

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from org.bukkit.block import Block
from org.bukkit.block.data import BlockData
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.block import *
from typing import Any, Callable, Iterable, Tuple


class FluidLevelChangeEvent(BlockEvent, Cancellable):
    """
    Called when the fluid level of a block changes due to changes in adjacent
    blocks.
    """

    def __init__(self, theBlock: "Block", newData: "BlockData"):
        ...


    def getNewData(self) -> "BlockData":
        """
        Gets the new data of the changed block.

        Returns
        - new data
        """
        ...


    def setNewData(self, newData: "BlockData") -> None:
        """
        Sets the new data of the changed block. Must be of the same Material as
        the old one.

        Arguments
        - newData: the new data
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
