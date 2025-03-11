"""
Python module generated from Java source file org.bukkit.event.block.BlockRedstoneEvent

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.event import HandlerList
from org.bukkit.event.block import *
from typing import Any, Callable, Iterable, Tuple


class BlockRedstoneEvent(BlockEvent):
    """
    Called when a redstone current changes
    """

    def __init__(self, block: "Block", oldCurrent: int, newCurrent: int):
        ...


    def getOldCurrent(self) -> int:
        """
        Gets the old current of this block

        Returns
        - The previous current
        """
        ...


    def getNewCurrent(self) -> int:
        """
        Gets the new current of this block

        Returns
        - The new current
        """
        ...


    def setNewCurrent(self, newCurrent: int) -> None:
        """
        Sets the new current of this block

        Arguments
        - newCurrent: The new current to set
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
