"""
Python module generated from Java source file org.bukkit.event.entity.EntityEnterLoveModeEvent

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Animals
from org.bukkit.entity import HumanEntity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class EntityEnterLoveModeEvent(EntityEvent, Cancellable):
    """
    Called when an entity enters love mode.
    
    This can be cancelled but the item will still be consumed that was used to
    make the entity enter into love mode.
    """

    def __init__(self, animalInLove: "Animals", humanEntity: "HumanEntity", ticksInLove: int):
        ...


    def getEntity(self) -> "Animals":
        """
        Gets the animal that is entering love mode.

        Returns
        - The animal that is entering love mode
        """
        ...


    def getHumanEntity(self) -> "HumanEntity":
        """
        Gets the Human Entity that caused the animal to enter love mode.

        Returns
        - The Human entity that caused the animal to enter love mode, or
        null if there wasn't one.
        """
        ...


    def getTicksInLove(self) -> int:
        """
        Gets the amount of ticks that the animal will fall in love for.

        Returns
        - The amount of ticks that the animal will fall in love for
        """
        ...


    def setTicksInLove(self, ticksInLove: int) -> None:
        """
        Sets the amount of ticks that the animal will fall in love for.

        Arguments
        - ticksInLove: The amount of ticks that the animal will fall in love
        for
        """
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
