"""
Python module generated from Java source file org.bukkit.event.vehicle.VehicleExitEvent

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import LivingEntity
from org.bukkit.entity import Vehicle
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.vehicle import *
from typing import Any, Callable, Iterable, Tuple


class VehicleExitEvent(VehicleEvent, Cancellable):
    """
    Raised when a living entity exits a vehicle.
    """

    def __init__(self, vehicle: "Vehicle", exited: "LivingEntity"):
        ...


    def getExited(self) -> "LivingEntity":
        """
        Get the living entity that exited the vehicle.

        Returns
        - The entity.
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
