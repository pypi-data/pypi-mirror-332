"""
Python module generated from Java source file org.bukkit.event.vehicle.VehicleCollisionEvent

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Vehicle
from org.bukkit.event.vehicle import *
from typing import Any, Callable, Iterable, Tuple


class VehicleCollisionEvent(VehicleEvent):
    """
    Raised when a vehicle collides.
    """

    def __init__(self, vehicle: "Vehicle"):
        ...
