"""
Python module generated from Java source file org.bukkit.event.block.BlockDamageAbortEvent

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.block import *
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class BlockDamageAbortEvent(BlockEvent):
    """
    Called when a player stops damaging a Block.

    See
    - BlockDamageEvent
    """

    def __init__(self, player: "Player", block: "Block", itemInHand: "ItemStack"):
        ...


    def getPlayer(self) -> "Player":
        """
        Gets the player that stopped damaging the block involved in this event.

        Returns
        - The player that stopped damaging the block
        """
        ...


    def getItemInHand(self) -> "ItemStack":
        """
        Gets the ItemStack for the item currently in the player's hand.

        Returns
        - The ItemStack for the item currently in the player's hand
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
