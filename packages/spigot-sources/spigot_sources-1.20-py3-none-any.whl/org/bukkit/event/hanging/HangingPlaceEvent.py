"""
Python module generated from Java source file org.bukkit.event.hanging.HangingPlaceEvent

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.block import BlockFace
from org.bukkit.entity import Hanging
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.hanging import *
from org.bukkit.inventory import EquipmentSlot
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class HangingPlaceEvent(HangingEvent, Cancellable):
    """
    Triggered when a hanging entity is created in the world
    """

    def __init__(self, hanging: "Hanging", player: "Player", block: "Block", blockFace: "BlockFace", hand: "EquipmentSlot"):
        ...


    def __init__(self, hanging: "Hanging", player: "Player", block: "Block", blockFace: "BlockFace", hand: "EquipmentSlot", itemStack: "ItemStack"):
        ...


    def getPlayer(self) -> "Player":
        """
        Returns the player placing the hanging entity

        Returns
        - the player placing the hanging entity
        """
        ...


    def getBlock(self) -> "Block":
        """
        Returns the block that the hanging entity was placed on

        Returns
        - the block that the hanging entity was placed on
        """
        ...


    def getBlockFace(self) -> "BlockFace":
        """
        Returns the face of the block that the hanging entity was placed on

        Returns
        - the face of the block that the hanging entity was placed on
        """
        ...


    def getHand(self) -> "EquipmentSlot":
        """
        Returns the hand that was used to place the hanging entity, or null
        if a player did not place the hanging entity.

        Returns
        - the hand
        """
        ...


    def getItemStack(self) -> "ItemStack":
        """
        Gets the item from which the hanging entity originated

        Returns
        - the item from which the hanging entity originated
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
