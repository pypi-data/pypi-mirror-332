"""
Python module generated from Java source file org.bukkit.Vibration

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import *
from org.bukkit.block import Block
from org.bukkit.entity import Entity
from typing import Any, Callable, Iterable, Tuple


class Vibration:
    """
    Represents a vibration from a Skulk sensor.
    """

    def __init__(self, origin: "Location", destination: "Destination", arrivalTime: int):
        ...


    def getOrigin(self) -> "Location":
        """
        Get the origin of the vibration.

        Returns
        - origin
        """
        ...


    def getDestination(self) -> "Destination":
        """
        Get the vibration destination.

        Returns
        - destination
        """
        ...


    def getArrivalTime(self) -> int:
        """
        Get the vibration arrival time in ticks.

        Returns
        - arrival time
        """
        ...


    class Destination:

        class EntityDestination(Destination):

            def __init__(self, entity: "Entity"):
                ...


            def getEntity(self) -> "Entity":
                ...


        class BlockDestination(Destination):

            def __init__(self, block: "Location"):
                ...


            def __init__(self, block: "Block"):
                ...


            def getLocation(self) -> "Location":
                ...


            def getBlock(self) -> "Block":
                ...
