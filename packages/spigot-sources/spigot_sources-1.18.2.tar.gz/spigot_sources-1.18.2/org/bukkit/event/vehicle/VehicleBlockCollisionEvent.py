"""
Python module generated from Java source file org.bukkit.event.vehicle.VehicleBlockCollisionEvent

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.entity import Vehicle
from org.bukkit.event import HandlerList
from org.bukkit.event.vehicle import *
from typing import Any, Callable, Iterable, Tuple


class VehicleBlockCollisionEvent(VehicleCollisionEvent):
    """
    Raised when a vehicle collides with a block.
    """

    def __init__(self, vehicle: "Vehicle", block: "Block"):
        ...


    def getBlock(self) -> "Block":
        """
        Gets the block the vehicle collided with

        Returns
        - the block the vehicle collided with
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
