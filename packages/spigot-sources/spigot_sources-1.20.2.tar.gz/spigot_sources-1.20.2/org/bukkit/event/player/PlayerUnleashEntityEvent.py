"""
Python module generated from Java source file org.bukkit.event.player.PlayerUnleashEntityEvent

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Entity
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event.entity import EntityUnleashEvent
from org.bukkit.event.player import *
from org.bukkit.inventory import EquipmentSlot
from typing import Any, Callable, Iterable, Tuple


class PlayerUnleashEntityEvent(EntityUnleashEvent, Cancellable):
    """
    Called prior to an entity being unleashed due to a player's action.
    """

    def __init__(self, entity: "Entity", player: "Player", hand: "EquipmentSlot"):
        ...


    def __init__(self, entity: "Entity", player: "Player"):
        ...


    def getPlayer(self) -> "Player":
        """
        Returns the player who is unleashing the entity.

        Returns
        - The player
        """
        ...


    def getHand(self) -> "EquipmentSlot":
        """
        Get the hand used by the player to unleash the entity.

        Returns
        - the hand
        """
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...
