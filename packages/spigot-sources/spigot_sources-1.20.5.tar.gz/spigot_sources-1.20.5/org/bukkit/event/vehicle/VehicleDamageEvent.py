"""
Python module generated from Java source file org.bukkit.event.vehicle.VehicleDamageEvent

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

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


class VehicleDamageEvent(VehicleEvent, Cancellable):
    """
    Raised when a vehicle receives damage.
    """

    def __init__(self, vehicle: "Vehicle", attacker: "Entity", damage: float):
        ...


    def getAttacker(self) -> "Entity":
        """
        Gets the Entity that is attacking the vehicle

        Returns
        - the Entity that is attacking the vehicle
        """
        ...


    def getDamage(self) -> float:
        """
        Gets the damage done to the vehicle

        Returns
        - the damage done to the vehicle
        """
        ...


    def setDamage(self, damage: float) -> None:
        """
        Sets the damage done to the vehicle

        Arguments
        - damage: The damage
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
