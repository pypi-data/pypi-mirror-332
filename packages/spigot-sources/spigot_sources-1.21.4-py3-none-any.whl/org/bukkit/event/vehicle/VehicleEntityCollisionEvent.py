"""
Python module generated from Java source file org.bukkit.event.vehicle.VehicleEntityCollisionEvent

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Entity
from org.bukkit.entity import Vehicle
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.vehicle import *
from typing import Any, Callable, Iterable, Tuple


class VehicleEntityCollisionEvent(VehicleCollisionEvent, Cancellable):
    """
    Raised when a vehicle collides with an entity.
    """

    def __init__(self, vehicle: "Vehicle", entity: "Entity"):
        ...


    def getEntity(self) -> "Entity":
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def isPickupCancelled(self) -> bool:
        ...


    def setPickupCancelled(self, cancel: bool) -> None:
        ...


    def isCollisionCancelled(self) -> bool:
        ...


    def setCollisionCancelled(self, cancel: bool) -> None:
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
