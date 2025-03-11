"""
Python module generated from Java source file org.bukkit.event.entity.EntityResurrectEvent

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import LivingEntity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from org.bukkit.inventory import EquipmentSlot
from typing import Any, Callable, Iterable, Tuple


class EntityResurrectEvent(EntityEvent, Cancellable):
    """
    Called when an entity dies and may have the opportunity to be resurrected.
    Will be called in a cancelled state if the entity does not have a totem
    equipped.
    """

    def __init__(self, what: "LivingEntity", hand: "EquipmentSlot"):
        ...


    def __init__(self, what: "LivingEntity"):
        ...


    def getEntity(self) -> "LivingEntity":
        ...


    def getHand(self) -> "EquipmentSlot":
        """
        Get the hand in which the totem of undying was found, or null if the
        entity did not have a totem of undying.

        Returns
        - the hand, or null
        """
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancelled: bool) -> None:
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
