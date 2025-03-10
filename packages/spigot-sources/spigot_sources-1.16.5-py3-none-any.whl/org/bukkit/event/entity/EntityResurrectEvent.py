"""
Python module generated from Java source file org.bukkit.event.entity.EntityResurrectEvent

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import LivingEntity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class EntityResurrectEvent(EntityEvent, Cancellable):
    """
    Called when an entity dies and may have the opportunity to be resurrected.
    Will be called in a cancelled state if the entity does not have a totem
    equipped.
    """

    def __init__(self, what: "LivingEntity"):
        ...


    def getEntity(self) -> "LivingEntity":
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
