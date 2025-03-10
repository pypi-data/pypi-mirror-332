"""
Python module generated from Java source file org.bukkit.event.player.PlayerHarvestBlockEvent

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class PlayerHarvestBlockEvent(PlayerEvent, Cancellable):
    """
    This event is called whenever a player harvests a block.
    
    A 'harvest' is when a block drops an item (usually some sort of crop) and
    changes state, but is not broken in order to drop the item.
    
    This event is not called for when a block is broken, to handle that, listen
    for org.bukkit.event.block.BlockBreakEvent and
    org.bukkit.event.block.BlockDropItemEvent.
    """

    def __init__(self, player: "Player", harvestedBlock: "Block", itemsHarvested: list["ItemStack"]):
        ...


    def getHarvestedBlock(self) -> "Block":
        """
        Gets the block that is being harvested.

        Returns
        - The block that is being harvested
        """
        ...


    def getItemsHarvested(self) -> list["ItemStack"]:
        """
        Gets a list of items that are being harvested from this block.

        Returns
        - A list of items that are being harvested from this block
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
