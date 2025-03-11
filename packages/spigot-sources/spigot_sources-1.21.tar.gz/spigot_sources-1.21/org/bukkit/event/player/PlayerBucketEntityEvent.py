"""
Python module generated from Java source file org.bukkit.event.player.PlayerBucketEntityEvent

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.entity import Entity
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from org.bukkit.inventory import EquipmentSlot
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class PlayerBucketEntityEvent(PlayerEvent, Cancellable):
    """
    This event is called whenever a player captures an entity in a bucket.
    """

    def __init__(self, player: "Player", entity: "Entity", originalBucket: "ItemStack", entityBucket: "ItemStack", hand: "EquipmentSlot"):
        ...


    def getEntity(self) -> "Entity":
        """
        Gets the Entity being put into the bucket.

        Returns
        - The Entity being put into the bucket
        """
        ...


    def getOriginalBucket(self) -> "ItemStack":
        """
        Gets the bucket used to capture the Entity.
        
        This refers to the bucket clicked with, eg Material.WATER_BUCKET.

        Returns
        - The used bucket
        """
        ...


    def getEntityBucket(self) -> "ItemStack":
        """
        Gets the bucket that the Entity will be put into.
        
        This refers to the bucket with the entity, eg
        Material.PUFFERFISH_BUCKET.

        Returns
        - The bucket that the Entity will be put into
        """
        ...


    def getHand(self) -> "EquipmentSlot":
        """
        Get the hand that was used to bucket the entity.

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
