"""
Python module generated from Java source file org.bukkit.event.player.PlayerInteractAtEntityEvent

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Entity
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from org.bukkit.inventory import EquipmentSlot
from org.bukkit.util import Vector
from typing import Any, Callable, Iterable, Tuple


class PlayerInteractAtEntityEvent(PlayerInteractEntityEvent):
    """
    Represents an event that is called when a player right clicks an entity that
    also contains the location where the entity was clicked.
    
    Note that the client may sometimes spuriously send this packet in addition to PlayerInteractEntityEvent.
    Users are advised to listen to this (parent) class unless specifically required.
    """

    def __init__(self, who: "Player", clickedEntity: "Entity", position: "Vector"):
        ...


    def __init__(self, who: "Player", clickedEntity: "Entity", position: "Vector", hand: "EquipmentSlot"):
        ...


    def getClickedPosition(self) -> "Vector":
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
