"""
Python module generated from Java source file org.bukkit.event.entity.ArrowBodyCountChangeEvent

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from org.bukkit.entity import LivingEntity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class ArrowBodyCountChangeEvent(EntityEvent, Cancellable):
    """
    Called when an arrow enters or exists an entity's body.
    """

    def __init__(self, entity: "LivingEntity", oldAmount: int, newAmount: int, isReset: bool):
        ...


    def isReset(self) -> bool:
        """
        Whether the event was called because the entity was reset.

        Returns
        - was reset
        """
        ...


    def getOldAmount(self) -> int:
        """
        Gets the old amount of arrows in the entity's body.

        Returns
        - amount of arrows
        """
        ...


    def getNewAmount(self) -> int:
        """
        Get the new amount of arrows in the entity's body.

        Returns
        - amount of arrows
        """
        ...


    def setNewAmount(self, newAmount: int) -> None:
        """
        Sets the final amount of arrows in the entity's body.

        Arguments
        - newAmount: amount of arrows
        """
        ...


    def getEntity(self) -> "LivingEntity":
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
