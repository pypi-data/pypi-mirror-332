"""
Python module generated from Java source file org.bukkit.event.entity.EntityToggleSwimEvent

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import LivingEntity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class EntityToggleSwimEvent(EntityEvent, Cancellable):
    """
    Sent when an entity's swimming status is toggled.
    """

    def __init__(self, who: "LivingEntity", isSwimming: bool):
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def isSwimming(self) -> bool:
        """
        Returns True if the entity is now swims or
        False if the entity stops swimming.

        Returns
        - new swimming state
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
