"""
Python module generated from Java source file org.bukkit.event.block.BlockEvent

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.event import Event
from org.bukkit.event.block import *
from typing import Any, Callable, Iterable, Tuple


class BlockEvent(Event):
    """
    Represents a block related event.
    """

    def __init__(self, theBlock: "Block"):
        ...


    def getBlock(self) -> "Block":
        """
        Gets the block involved in this event.

        Returns
        - The Block which block is involved in this event
        """
        ...
