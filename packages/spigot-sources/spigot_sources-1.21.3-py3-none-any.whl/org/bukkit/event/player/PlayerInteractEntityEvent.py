"""
Python module generated from Java source file org.bukkit.event.player.PlayerInteractEntityEvent

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Entity
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from org.bukkit.inventory import EquipmentSlot
from typing import Any, Callable, Iterable, Tuple


class PlayerInteractEntityEvent(PlayerEvent, Cancellable):
    """
    Represents an event that is called when a player right clicks an entity.
    """

    def __init__(self, who: "Player", clickedEntity: "Entity"):
        ...


    def __init__(self, who: "Player", clickedEntity: "Entity", hand: "EquipmentSlot"):
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getRightClicked(self) -> "Entity":
        """
        Gets the entity that was right-clicked by the player.

        Returns
        - entity right clicked by player
        """
        ...


    def getHand(self) -> "EquipmentSlot":
        """
        The hand used to perform this interaction.

        Returns
        - the hand used to interact
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
