"""
Python module generated from Java source file org.bukkit.event.block.BlockBreakEvent

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event.block import *
from typing import Any, Callable, Iterable, Tuple


class BlockBreakEvent(BlockExpEvent, Cancellable):
    """
    Called when a block is broken by a player.
    
    If you wish to have the block drop experience, you must set the experience
    value above 0. By default, experience will be set in the event if:
    <ol>
    - The player is not in creative or adventure mode
    - The player can loot the block (ie: does not destroy it completely, by
        using the correct tool)
    - The player does not have silk touch
    - The block drops experience in vanilla Minecraft
    </ol>
    
    Note:
    Plugins wanting to simulate a traditional block drop should set the block
    to air and utilize their own methods for determining what the default drop
    for the block being broken is and what to do about it, if anything.
    
    If a Block Break event is cancelled, the block will not break and
    experience will not drop.
    """

    def __init__(self, theBlock: "Block", player: "Player"):
        ...


    def getPlayer(self) -> "Player":
        """
        Gets the Player that is breaking the block involved in this event.

        Returns
        - The Player that is breaking the block involved in this event
        """
        ...


    def setDropItems(self, dropItems: bool) -> None:
        """
        Sets whether or not the block will attempt to drop items as it normally
        would.
        
        If and only if this is False then BlockDropItemEvent will not be
        called after this event.

        Arguments
        - dropItems: Whether or not the block will attempt to drop items
        """
        ...


    def isDropItems(self) -> bool:
        """
        Gets whether or not the block will attempt to drop items.
        
        If and only if this is False then BlockDropItemEvent will not be
        called after this event.

        Returns
        - Whether or not the block will attempt to drop items
        """
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...
