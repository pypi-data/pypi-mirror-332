"""
Python module generated from Java source file org.bukkit.event.entity.ItemDespawnEvent

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Location
from org.bukkit.entity import Item
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class ItemDespawnEvent(EntityEvent, Cancellable):
    """
    This event is called when a org.bukkit.entity.Item is removed from
    the world because it has existed for 5 minutes.
    
    Cancelling the event results in the item being allowed to exist for 5 more
    minutes. This behavior is not guaranteed and may change in future versions.
    """

    def __init__(self, despawnee: "Item", loc: "Location"):
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getEntity(self) -> "Item":
        ...


    def getLocation(self) -> "Location":
        """
        Gets the location at which the item is despawning.

        Returns
        - The location at which the item is despawning
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
