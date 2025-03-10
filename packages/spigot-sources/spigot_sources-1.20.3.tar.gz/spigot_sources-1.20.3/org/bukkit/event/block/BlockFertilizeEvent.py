"""
Python module generated from Java source file org.bukkit.event.block.BlockFertilizeEvent

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.block import BlockState
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.block import *
from org.bukkit.event.world import StructureGrowEvent
from typing import Any, Callable, Iterable, Tuple


class BlockFertilizeEvent(BlockEvent, Cancellable):
    """
    Called with the block changes resulting from a player fertilizing a given
    block with bonemeal. Will be called after the applicable
    StructureGrowEvent.
    """

    def __init__(self, theBlock: "Block", player: "Player", blocks: list["BlockState"]):
        ...


    def getPlayer(self) -> "Player":
        """
        Gets the player that triggered the fertilization.

        Returns
        - triggering player, or null if not applicable
        """
        ...


    def getBlocks(self) -> list["BlockState"]:
        """
        Gets a list of all blocks changed by the fertilization.

        Returns
        - list of all changed blocks
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
