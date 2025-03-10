"""
Python module generated from Java source file org.bukkit.event.entity.ExplosionPrimeEvent

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Entity
from org.bukkit.entity import Explosive
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class ExplosionPrimeEvent(EntityEvent, Cancellable):
    """
    Called when an entity has made a decision to explode.
    """

    def __init__(self, what: "Entity", radius: float, fire: bool):
        ...


    def __init__(self, explosive: "Explosive"):
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getRadius(self) -> float:
        """
        Gets the radius of the explosion

        Returns
        - returns the radius of the explosion
        """
        ...


    def setRadius(self, radius: float) -> None:
        """
        Sets the radius of the explosion

        Arguments
        - radius: the radius of the explosion
        """
        ...


    def getFire(self) -> bool:
        """
        Gets whether this explosion will create fire or not

        Returns
        - True if this explosion will create fire
        """
        ...


    def setFire(self, fire: bool) -> None:
        """
        Sets whether this explosion will create fire or not

        Arguments
        - fire: True if you want this explosion to create fire
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
