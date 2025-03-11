"""
Python module generated from Java source file org.bukkit.event.entity.EntityAirChangeEvent

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Entity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class EntityAirChangeEvent(EntityEvent, Cancellable):
    """
    Called when the amount of air an entity has remaining changes.
    """

    def __init__(self, what: "Entity", amount: int):
        ...


    def getAmount(self) -> int:
        """
        Gets the amount of air the entity has left (measured in ticks).

        Returns
        - amount of air remaining
        """
        ...


    def setAmount(self, amount: int) -> None:
        """
        Sets the amount of air remaining for the entity (measured in ticks.

        Arguments
        - amount: amount of air remaining
        """
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancelled: bool) -> None:
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
