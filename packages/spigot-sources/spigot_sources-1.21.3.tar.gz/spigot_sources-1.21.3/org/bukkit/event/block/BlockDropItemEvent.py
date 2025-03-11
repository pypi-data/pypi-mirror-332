"""
Python module generated from Java source file org.bukkit.event.block.BlockDropItemEvent

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.block import BlockState
from org.bukkit.entity import Item
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.block import *
from typing import Any, Callable, Iterable, Tuple


class BlockDropItemEvent(BlockEvent, Cancellable):
    """
    Called if a block broken by a player drops an item.
    
    If the block break is cancelled, this event won't be called.
    
    If isDropItems in BlockBreakEvent is set to False, this event won't be
    called.
    
    This event will also be called if the player breaks a multi block structure,
    for example a torch on top of a stone. Both items will have an event call.
    
    The Block is already broken as this event is called, so #getBlock() will be
    AIR in most cases. Use #getBlockState() for more Information about the broken
    block.
    """

    def __init__(self, block: "Block", blockState: "BlockState", player: "Player", items: list["Item"]):
        ...


    def getPlayer(self) -> "Player":
        """
        Gets the Player that is breaking the block involved in this event.

        Returns
        - The Player that is breaking the block involved in this event
        """
        ...


    def getBlockState(self) -> "BlockState":
        """
        Gets the BlockState of the block involved in this event before it was
        broken.

        Returns
        - The BlockState of the block involved in this event
        """
        ...


    def getItems(self) -> list["Item"]:
        """
        Gets list of the Item drops caused by the block break.
        
        This list is mutable - removing an item from it will cause it to not
        drop. It is not legal however to add new items to the list.

        Returns
        - The Item the block caused to drop
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
