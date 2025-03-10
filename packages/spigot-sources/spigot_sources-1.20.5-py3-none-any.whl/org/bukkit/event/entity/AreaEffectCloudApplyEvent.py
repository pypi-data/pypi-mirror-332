"""
Python module generated from Java source file org.bukkit.event.entity.AreaEffectCloudApplyEvent

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import AreaEffectCloud
from org.bukkit.entity import LivingEntity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class AreaEffectCloudApplyEvent(EntityEvent, Cancellable):
    """
    Called when a lingering potion applies it's effects. Happens
    once every 5 ticks
    """

    def __init__(self, entity: "AreaEffectCloud", affectedEntities: list["LivingEntity"]):
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getEntity(self) -> "AreaEffectCloud":
        ...


    def getAffectedEntities(self) -> list["LivingEntity"]:
        """
        Retrieves a mutable list of the effected entities
        
        It is important to note that not every entity in this list
        is guaranteed to be effected.  The cloud may die during the
        application of its effects due to the depletion of AreaEffectCloud.getDurationOnUse()
        or AreaEffectCloud.getRadiusOnUse()

        Returns
        - the affected entity list
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
