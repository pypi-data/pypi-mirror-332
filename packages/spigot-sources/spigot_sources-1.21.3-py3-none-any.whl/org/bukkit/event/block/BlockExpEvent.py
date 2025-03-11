"""
Python module generated from Java source file org.bukkit.event.block.BlockExpEvent

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.event import HandlerList
from org.bukkit.event.block import *
from typing import Any, Callable, Iterable, Tuple


class BlockExpEvent(BlockEvent):
    """
    An event that's called when a block yields experience.
    """

    def __init__(self, block: "Block", exp: int):
        ...


    def getExpToDrop(self) -> int:
        """
        Get the experience dropped by the block after the event has processed

        Returns
        - The experience to drop
        """
        ...


    def setExpToDrop(self, exp: int) -> None:
        """
        Set the amount of experience dropped by the block after the event has
        processed

        Arguments
        - exp: 1 or higher to drop experience, else nothing will drop
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
