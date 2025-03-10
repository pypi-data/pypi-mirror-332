"""
Python module generated from Java source file org.bukkit.event.block.BlockDamageEvent

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.block import *
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class BlockDamageEvent(BlockEvent, Cancellable):
    """
    Called when a block is damaged by a player.
    
    If a Block Damage event is cancelled, the block will not be damaged.

    See
    - BlockDamageAbortEvent
    """

    def __init__(self, player: "Player", block: "Block", itemInHand: "ItemStack", instaBreak: bool):
        ...


    def getPlayer(self) -> "Player":
        """
        Gets the player damaging the block involved in this event.

        Returns
        - The player damaging the block involved in this event
        """
        ...


    def getInstaBreak(self) -> bool:
        """
        Gets if the block is set to instantly break when damaged by the player.

        Returns
        - True if the block should instantly break when damaged by the
            player
        """
        ...


    def setInstaBreak(self, bool: bool) -> None:
        """
        Sets if the block should instantly break when damaged by the player.

        Arguments
        - bool: True if you want the block to instantly break when damaged
            by the player
        """
        ...


    def getItemInHand(self) -> "ItemStack":
        """
        Gets the ItemStack for the item currently in the player's hand.

        Returns
        - The ItemStack for the item currently in the player's hand
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
