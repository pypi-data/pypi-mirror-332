"""
Python module generated from Java source file org.bukkit.event.block.MoistureChangeEvent

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.block import BlockState
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.block import *
from typing import Any, Callable, Iterable, Tuple


class MoistureChangeEvent(BlockEvent, Cancellable):
    """
    Called when the moisture level of a soil block changes.
    """

    def __init__(self, block: "Block", newState: "BlockState"):
        ...


    def getNewState(self) -> "BlockState":
        """
        Gets the new state of the affected block.

        Returns
        - new block state
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
