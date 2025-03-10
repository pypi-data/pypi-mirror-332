"""
Python module generated from Java source file org.bukkit.event.block.SpongeAbsorbEvent

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.block import Block
from org.bukkit.block import BlockState
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.block import *
from typing import Any, Callable, Iterable, Tuple


class SpongeAbsorbEvent(BlockEvent, Cancellable):
    """
    Called when a sponge absorbs water from the world.
    
    The world will be in its previous state, and .getBlocks() will
    represent the changes to be made to the world, if the event is not cancelled.
    
    As this is a physics based event it may be called multiple times for "the
    same" changes.
    """

    def __init__(self, block: "Block", waterblocks: list["BlockState"]):
        ...


    def getBlocks(self) -> list["BlockState"]:
        """
        Get a list of all blocks to be removed by the sponge.
        
        This list is mutable and contains the blocks in their removed state, i.e.
        having a type of Material.AIR.

        Returns
        - list of the to be removed blocks.
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
