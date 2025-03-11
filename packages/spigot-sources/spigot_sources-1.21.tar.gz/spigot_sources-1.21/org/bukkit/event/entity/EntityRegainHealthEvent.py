"""
Python module generated from Java source file org.bukkit.event.entity.EntityRegainHealthEvent

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.entity import Entity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class EntityRegainHealthEvent(EntityEvent, Cancellable):
    """
    Stores data for health-regain events
    """

    def __init__(self, entity: "Entity", amount: float, regainReason: "RegainReason"):
        ...


    def getAmount(self) -> float:
        """
        Gets the amount of regained health

        Returns
        - The amount of health regained
        """
        ...


    def setAmount(self, amount: float) -> None:
        """
        Sets the amount of regained health

        Arguments
        - amount: the amount of health the entity will regain
        """
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getRegainReason(self) -> "RegainReason":
        """
        Gets the reason for why the entity is regaining health

        Returns
        - A RegainReason detailing the reason for the entity regaining
            health
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...


    class RegainReason(Enum):
        """
        An enum to specify the type of health regaining that is occurring
        """

        REGEN = 0
        """
        When a player regains health from regenerating due to Peaceful mode
        (difficulty=0)
        """
        SATIATED = 1
        """
        When a player regains health from regenerating due to their hunger
        being satisfied
        """
        EATING = 2
        """
        When a player regains health from eating consumables
        """
        ENDER_CRYSTAL = 3
        """
        When an ender dragon regains health from an ender crystal
        """
        MAGIC = 4
        """
        When a player is healed by a potion or spell
        """
        MAGIC_REGEN = 5
        """
        When a player is healed over time by a potion or spell
        """
        WITHER_SPAWN = 6
        """
        When a wither is filling its health during spawning
        """
        WITHER = 7
        """
        When an entity is damaged by the Wither potion effect
        """
        CUSTOM = 8
        """
        Any other reason not covered by the reasons above
        """
