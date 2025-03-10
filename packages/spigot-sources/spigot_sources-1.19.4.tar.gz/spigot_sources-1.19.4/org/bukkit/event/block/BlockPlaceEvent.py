"""
Python module generated from Java source file org.bukkit.event.block.BlockPlaceEvent

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

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
from org.bukkit.inventory import EquipmentSlot
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class BlockPlaceEvent(BlockEvent, Cancellable):
    """
    Called when a block is placed by a player.
    
    If a Block Place event is cancelled, the block will not be placed.
    """

    def __init__(self, placedBlock: "Block", replacedBlockState: "BlockState", placedAgainst: "Block", itemInHand: "ItemStack", thePlayer: "Player", canBuild: bool):
        ...


    def __init__(self, placedBlock: "Block", replacedBlockState: "BlockState", placedAgainst: "Block", itemInHand: "ItemStack", thePlayer: "Player", canBuild: bool, hand: "EquipmentSlot"):
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getPlayer(self) -> "Player":
        """
        Gets the player who placed the block involved in this event.

        Returns
        - The Player who placed the block involved in this event
        """
        ...


    def getBlockPlaced(self) -> "Block":
        """
        Clarity method for getting the placed block. Not really needed except
        for reasons of clarity.

        Returns
        - The Block that was placed
        """
        ...


    def getBlockReplacedState(self) -> "BlockState":
        """
        Gets the BlockState for the block which was replaced. Material type air
        mostly.

        Returns
        - The BlockState for the block which was replaced.
        """
        ...


    def getBlockAgainst(self) -> "Block":
        """
        Gets the block that this block was placed against

        Returns
        - Block the block that the new block was placed against
        """
        ...


    def getItemInHand(self) -> "ItemStack":
        """
        Gets the item in the player's hand when they placed the block.

        Returns
        - The ItemStack for the item in the player's hand when they
            placed the block
        """
        ...


    def getHand(self) -> "EquipmentSlot":
        """
        Gets the hand which placed the block

        Returns
        - Main or off-hand, depending on which hand was used to place the block
        """
        ...


    def canBuild(self) -> bool:
        """
        Gets the value whether the player would be allowed to build here.
        Defaults to spawn if the server was going to stop them (such as, the
        player is in Spawn). Note that this is an entirely different check
        than BLOCK_CANBUILD, as this refers to a player, not universe-physics
        rule like cactus on dirt.

        Returns
        - boolean whether the server would allow a player to build here
        """
        ...


    def setBuild(self, canBuild: bool) -> None:
        """
        Sets the canBuild state of this event. Set to True if you want the
        player to be able to build.

        Arguments
        - canBuild: True if you want the player to be able to build
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
