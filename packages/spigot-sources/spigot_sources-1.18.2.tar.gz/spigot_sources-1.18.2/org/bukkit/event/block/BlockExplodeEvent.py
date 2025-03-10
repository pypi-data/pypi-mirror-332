"""
Python module generated from Java source file org.bukkit.event.block.BlockExplodeEvent

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.block import *
from typing import Any, Callable, Iterable, Tuple


class BlockExplodeEvent(BlockEvent, Cancellable):
    """
    Called when a block explodes
    """

    def __init__(self, what: "Block", blocks: list["Block"], yield: float):
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def blockList(self) -> list["Block"]:
        """
        Returns the list of blocks that would have been removed or were removed
        from the explosion event.

        Returns
        - All blown-up blocks
        """
        ...


    def getYield(self) -> float:
        """
        Returns the percentage of blocks to drop from this explosion

        Returns
        - The yield.
        """
        ...


    def setYield(self, yield: float) -> None:
        """
        Sets the percentage of blocks to drop from this explosion

        Arguments
        - yield: The new yield percentage
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
