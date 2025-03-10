"""
Python module generated from Java source file org.bukkit.event.player.PlayerBucketEvent

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.block import Block
from org.bukkit.block import BlockFace
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event.player import *
from org.bukkit.inventory import EquipmentSlot
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class PlayerBucketEvent(PlayerEvent, Cancellable):
    """
    Called when a player interacts with a Bucket
    """

    def __init__(self, who: "Player", blockClicked: "Block", blockFace: "BlockFace", bucket: "Material", itemInHand: "ItemStack"):
        ...


    def __init__(self, who: "Player", block: "Block", blockClicked: "Block", blockFace: "BlockFace", bucket: "Material", itemInHand: "ItemStack"):
        ...


    def __init__(self, who: "Player", block: "Block", blockClicked: "Block", blockFace: "BlockFace", bucket: "Material", itemInHand: "ItemStack", hand: "EquipmentSlot"):
        ...


    def getBucket(self) -> "Material":
        """
        Returns the bucket used in this event

        Returns
        - the used bucket
        """
        ...


    def getItemStack(self) -> "ItemStack":
        """
        Get the resulting item in hand after the bucket event

        Returns
        - ItemStack hold in hand after the event.
        """
        ...


    def setItemStack(self, itemStack: "ItemStack") -> None:
        """
        Set the item in hand after the event

        Arguments
        - itemStack: the new held ItemStack after the bucket event.
        """
        ...


    def getBlock(self) -> "Block":
        """
        Gets the block involved in this event.

        Returns
        - The Block which block is involved in this event
        """
        ...


    def getBlockClicked(self) -> "Block":
        """
        Return the block clicked

        Returns
        - the clicked block
        """
        ...


    def getBlockFace(self) -> "BlockFace":
        """
        Get the face on the clicked block

        Returns
        - the clicked face
        """
        ...


    def getHand(self) -> "EquipmentSlot":
        """
        Get the hand that was used in this event.

        Returns
        - the hand
        """
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...
