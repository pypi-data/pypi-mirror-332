"""
Python module generated from Java source file org.bukkit.event.entity.EntityTameEvent

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import AnimalTamer
from org.bukkit.entity import LivingEntity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class EntityTameEvent(EntityEvent, Cancellable):
    """
    Thrown when a LivingEntity is tamed
    """

    def __init__(self, entity: "LivingEntity", owner: "AnimalTamer"):
        ...


    def getEntity(self) -> "LivingEntity":
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getOwner(self) -> "AnimalTamer":
        """
        Gets the owning AnimalTamer

        Returns
        - the owning AnimalTamer
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
