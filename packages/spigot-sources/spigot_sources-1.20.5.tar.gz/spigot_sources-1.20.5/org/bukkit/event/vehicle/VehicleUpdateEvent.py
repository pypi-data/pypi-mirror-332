"""
Python module generated from Java source file org.bukkit.event.vehicle.VehicleUpdateEvent

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Vehicle
from org.bukkit.event import HandlerList
from org.bukkit.event.vehicle import *
from typing import Any, Callable, Iterable, Tuple


class VehicleUpdateEvent(VehicleEvent):
    """
    Called when a vehicle updates
    """

    def __init__(self, vehicle: "Vehicle"):
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
