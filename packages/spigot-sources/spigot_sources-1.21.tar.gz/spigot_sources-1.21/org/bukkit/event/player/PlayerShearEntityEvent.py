"""
Python module generated from Java source file org.bukkit.event.player.PlayerShearEntityEvent

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


class PlayerShearEntityEvent(PlayerEvent, Cancellable):
    """
    Called when a player shears an entity
    """

    def __init__(self, who: "Player", what: "Entity", item: "ItemStack", hand: "EquipmentSlot"):
        ...


    def __init__(self, who: "Player", what: "Entity"):
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getEntity(self) -> "Entity":
        """
        Gets the entity the player is shearing

        Returns
        - the entity the player is shearing
        """
        ...


    def getItem(self) -> "ItemStack":
        """
        Gets the item used to shear the entity.

        Returns
        - the shears
        """
        ...


    def getHand(self) -> "EquipmentSlot":
        """
        Gets the hand used to shear the entity.

        Returns
        - the hand
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
