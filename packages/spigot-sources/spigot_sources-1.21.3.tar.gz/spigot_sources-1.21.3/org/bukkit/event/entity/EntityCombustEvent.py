"""
Python module generated from Java source file org.bukkit.event.entity.EntityCombustEvent

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Entity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class EntityCombustEvent(EntityEvent, Cancellable):
    """
    Called when an entity combusts.
    
    If an Entity Combust event is cancelled, the entity will not combust.
    """

    def __init__(self, combustee: "Entity", duration: int):
        ...


    def __init__(self, combustee: "Entity", duration: float):
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getDuration(self) -> float:
        """
        Returns
        - the amount of time (in seconds) the combustee should be alight
            for
        """
        ...


    def setDuration(self, duration: float) -> None:
        """
        The number of seconds the combustee should be alight for.
        
        This value will only ever increase the combustion time, not decrease
        existing combustion times.

        Arguments
        - duration: the time in seconds to be alight for.
        """
        ...


    def setDuration(self, duration: int) -> None:
        """
        The number of seconds the combustee should be alight for.
        
        This value will only ever increase the combustion time, not decrease
        existing combustion times.

        Arguments
        - duration: the time in seconds to be alight for.

        See
        - .setDuration(float)

        Deprecated
        - duration is now a float
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
