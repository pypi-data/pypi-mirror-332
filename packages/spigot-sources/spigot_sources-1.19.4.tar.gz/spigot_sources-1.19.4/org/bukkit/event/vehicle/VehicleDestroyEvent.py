"""
Python module generated from Java source file org.bukkit.event.vehicle.VehicleDestroyEvent

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

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


class VehicleDestroyEvent(VehicleEvent, Cancellable):
    """
    Raised when a vehicle is destroyed, which could be caused by either a
    player or the environment. This is not raised if the boat is simply
    'removed' due to other means.
    """

    def __init__(self, vehicle: "Vehicle", attacker: "Entity"):
        ...


    def getAttacker(self) -> "Entity":
        """
        Gets the Entity that has destroyed the vehicle, potentially null

        Returns
        - the Entity that has destroyed the vehicle, potentially null
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
