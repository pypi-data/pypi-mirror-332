"""
Python module generated from Java source file org.bukkit.event.entity.EntityShootBowEvent

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Entity
from org.bukkit.entity import LivingEntity
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from org.bukkit.inventory import EquipmentSlot
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class EntityShootBowEvent(EntityEvent, Cancellable):
    """
    Called when a LivingEntity shoots a bow firing an arrow
    """

    def __init__(self, shooter: "LivingEntity", bow: "ItemStack", consumable: "ItemStack", projectile: "Entity", hand: "EquipmentSlot", force: float, consumeItem: bool):
        ...


    def getEntity(self) -> "LivingEntity":
        ...


    def getBow(self) -> "ItemStack":
        """
        Gets the bow ItemStack used to fire the arrow.

        Returns
        - the bow involved in this event
        """
        ...


    def getConsumable(self) -> "ItemStack":
        """
        Get the ItemStack to be consumed in this event (if any).
        
        For instance, bows will consume an arrow ItemStack in a player's
        inventory.

        Returns
        - the consumable item
        """
        ...


    def getProjectile(self) -> "Entity":
        """
        Gets the projectile which will be launched by this event

        Returns
        - the launched projectile
        """
        ...


    def setProjectile(self, projectile: "Entity") -> None:
        """
        Replaces the projectile which will be launched

        Arguments
        - projectile: the new projectile
        """
        ...


    def getHand(self) -> "EquipmentSlot":
        """
        Get the hand from which the bow was shot.

        Returns
        - the hand
        """
        ...


    def getForce(self) -> float:
        """
        Gets the force the arrow was launched with

        Returns
        - bow shooting force, up to 1.0
        """
        ...


    def setConsumeItem(self, consumeItem: bool) -> None:
        """
        Set whether or not the consumable item should be consumed in this event.
        
        If set to False, it is recommended that a call to
        Player.updateInventory() is made as the client may disagree with
        the server's decision to not consume a consumable item.
        
        This value is ignored for entities where items are not required
        (skeletons, pillagers, etc.) or with crossbows (as no item is being
        consumed).

        Arguments
        - consumeItem: whether or not to consume the item
        """
        ...


    def shouldConsumeItem(self) -> bool:
        """
        Get whether or not the consumable item should be consumed in this event.

        Returns
        - True if consumed, False otherwise
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
