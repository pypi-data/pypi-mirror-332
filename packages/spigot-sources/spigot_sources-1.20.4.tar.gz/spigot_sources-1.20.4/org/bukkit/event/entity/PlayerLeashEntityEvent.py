"""
Python module generated from Java source file org.bukkit.event.entity.PlayerLeashEntityEvent

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Entity
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import Event
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from org.bukkit.inventory import EquipmentSlot
from typing import Any, Callable, Iterable, Tuple


class PlayerLeashEntityEvent(Event, Cancellable):
    """
    Called immediately prior to a creature being leashed by a player.
    """

    def __init__(self, what: "Entity", leashHolder: "Entity", leasher: "Player", hand: "EquipmentSlot"):
        ...


    def __init__(self, what: "Entity", leashHolder: "Entity", leasher: "Player"):
        ...


    def getLeashHolder(self) -> "Entity":
        """
        Returns the entity that is holding the leash.

        Returns
        - The leash holder
        """
        ...


    def getEntity(self) -> "Entity":
        """
        Returns the entity being leashed.

        Returns
        - The entity
        """
        ...


    def getPlayer(self) -> "Player":
        """
        Returns the player involved in this event

        Returns
        - Player who is involved in this event
        """
        ...


    def getHand(self) -> "EquipmentSlot":
        """
        Returns the hand used by the player to leash the entity.

        Returns
        - the hand
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...
