"""
Python module generated from Java source file org.bukkit.event.entity.PigZombieAngerEvent

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Entity
from org.bukkit.entity import PigZombie
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class PigZombieAngerEvent(EntityEvent, Cancellable):
    """
    Called when a Pig Zombie is angered by another entity.
    
    If the event is cancelled, the pig zombie will not be angered.
    """

    def __init__(self, pigZombie: "PigZombie", target: "Entity", newAnger: int):
        ...


    def getTarget(self) -> "Entity":
        """
        Gets the entity (if any) which triggered this anger update.

        Returns
        - triggering entity, or null
        """
        ...


    def getNewAnger(self) -> int:
        """
        Gets the new anger resulting from this event.

        Returns
        - new anger

        See
        - PigZombie.getAnger()
        """
        ...


    def setNewAnger(self, newAnger: int) -> None:
        """
        Sets the new anger resulting from this event.

        Arguments
        - newAnger: the new anger

        See
        - PigZombie.setAnger(int)
        """
        ...


    def getEntity(self) -> "PigZombie":
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
