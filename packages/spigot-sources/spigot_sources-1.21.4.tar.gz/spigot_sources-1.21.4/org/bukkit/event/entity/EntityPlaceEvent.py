"""
Python module generated from Java source file org.bukkit.event.entity.EntityPlaceEvent

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.block import BlockFace
from org.bukkit.entity import Entity
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from org.bukkit.inventory import EquipmentSlot
from typing import Any, Callable, Iterable, Tuple


class EntityPlaceEvent(EntityEvent, Cancellable):
    """
    Triggered when a entity is created in the world by a player "placing" an item
    on a block.
    
    Note that this event is currently only fired for four specific placements:
    armor stands, boats, minecarts, and end crystals.
    """

    def __init__(self, entity: "Entity", player: "Player", block: "Block", blockFace: "BlockFace", hand: "EquipmentSlot"):
        ...


    def __init__(self, entity: "Entity", player: "Player", block: "Block", blockFace: "BlockFace"):
        ...


    def getPlayer(self) -> "Player":
        """
        Returns the player placing the entity

        Returns
        - the player placing the entity
        """
        ...


    def getBlock(self) -> "Block":
        """
        Returns the block that the entity was placed on

        Returns
        - the block that the entity was placed on
        """
        ...


    def getBlockFace(self) -> "BlockFace":
        """
        Returns the face of the block that the entity was placed on

        Returns
        - the face of the block that the entity was placed on
        """
        ...


    def getHand(self) -> "EquipmentSlot":
        """
        Get the hand used to place the entity.

        Returns
        - the hand
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
