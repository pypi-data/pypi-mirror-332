"""
Python module generated from Java source file org.bukkit.event.vehicle.VehicleEvent

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Vehicle
from org.bukkit.event import Event
from org.bukkit.event.vehicle import *
from typing import Any, Callable, Iterable, Tuple


class VehicleEvent(Event):
    """
    Represents a vehicle-related event.
    """

    def __init__(self, vehicle: "Vehicle"):
        ...


    def getVehicle(self) -> "Vehicle":
        """
        Get the vehicle.

        Returns
        - the vehicle
        """
        ...
