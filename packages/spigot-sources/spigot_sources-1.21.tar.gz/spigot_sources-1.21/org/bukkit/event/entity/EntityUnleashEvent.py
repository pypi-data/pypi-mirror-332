"""
Python module generated from Java source file org.bukkit.event.entity.EntityUnleashEvent

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.entity import Entity
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class EntityUnleashEvent(EntityEvent):
    """
    Called immediately prior to an entity being unleashed.
    """

    def __init__(self, entity: "Entity", reason: "UnleashReason"):
        ...


    def getReason(self) -> "UnleashReason":
        """
        Returns the reason for the unleashing.

        Returns
        - The reason
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...


    class UnleashReason(Enum):

        HOLDER_GONE = 0
        """
        When the entity's leashholder has died or logged out, and so is
        unleashed
        """
        PLAYER_UNLEASH = 1
        """
        When the entity's leashholder attempts to unleash it
        """
        DISTANCE = 2
        """
        When the entity's leashholder is more than 10 blocks away
        """
        UNKNOWN = 3
