"""
Python module generated from Java source file org.bukkit.event.block.BlockPistonEvent

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.block import Block
from org.bukkit.block import BlockFace
from org.bukkit.event import Cancellable
from org.bukkit.event.block import *
from typing import Any, Callable, Iterable, Tuple


class BlockPistonEvent(BlockEvent, Cancellable):
    """
    Called when a piston block is triggered
    """

    def __init__(self, block: "Block", direction: "BlockFace"):
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancelled: bool) -> None:
        ...


    def isSticky(self) -> bool:
        """
        Returns True if the Piston in the event is sticky.

        Returns
        - stickiness of the piston
        """
        ...


    def getDirection(self) -> "BlockFace":
        """
        Return the direction in which the piston will operate.

        Returns
        - direction of the piston
        """
        ...
