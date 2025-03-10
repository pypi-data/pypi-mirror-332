"""
Python module generated from Java source file org.bukkit.event.entity.PotionSplashEvent

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from org.bukkit.entity import LivingEntity
from org.bukkit.entity import ThrownPotion
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class PotionSplashEvent(ProjectileHitEvent, Cancellable):
    """
    Called when a splash potion hits an area
    """

    def __init__(self, potion: "ThrownPotion", affectedEntities: dict["LivingEntity", "Double"]):
        ...


    def getEntity(self) -> "ThrownPotion":
        ...


    def getPotion(self) -> "ThrownPotion":
        """
        Gets the potion which caused this event

        Returns
        - The thrown potion entity
        """
        ...


    def getAffectedEntities(self) -> Iterable["LivingEntity"]:
        """
        Retrieves a list of all effected entities

        Returns
        - A fresh copy of the affected entity list
        """
        ...


    def getIntensity(self, entity: "LivingEntity") -> float:
        """
        Gets the intensity of the potion's effects for given entity; This
        depends on the distance to the impact center

        Arguments
        - entity: Which entity to get intensity for

        Returns
        - intensity relative to maximum effect; 0.0: not affected; 1.0:
            fully hit by potion effects
        """
        ...


    def setIntensity(self, entity: "LivingEntity", intensity: float) -> None:
        """
        Overwrites the intensity for a given entity

        Arguments
        - entity: For which entity to define a new intensity
        - intensity: relative to maximum effect
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
