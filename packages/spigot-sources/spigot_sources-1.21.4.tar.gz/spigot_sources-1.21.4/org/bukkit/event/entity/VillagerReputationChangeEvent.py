"""
Python module generated from Java source file org.bukkit.event.entity.VillagerReputationChangeEvent

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from java.util import UUID
from org.bukkit import Bukkit
from org.bukkit.entity import Entity
from org.bukkit.entity import Villager
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class VillagerReputationChangeEvent(EntityEvent, Cancellable):
    """
    Called whenever an entity's reputation with a villager changes.
    """

    def __init__(self, villager: "Villager", targetUUID: "UUID", reason: "Villager.ReputationEvent", reputationType: "Villager.ReputationType", oldValue: int, newValue: int, maxValue: int):
        ...


    def getTargetUUID(self) -> "UUID":
        """
        Get UUID of the entity for whom the reputation with a villager changes.

        Returns
        - UUID of the entity for whom the reputation with a villager
                changes
        """
        ...


    def getTarget(self) -> "Entity":
        """
        Get the Entity for whom the reputation with a villager changes.

        Returns
        - the Entity for whom the reputation with a villager changes,
                or `null` if it isn't found
        """
        ...


    def getReason(self) -> "Villager.ReputationEvent":
        """
        Get the reason of this reputation change.

        Returns
        - the reason of this reputation change
        """
        ...


    def getReputationType(self) -> "Villager.ReputationType":
        """
        Get the type of changed reputation.

        Returns
        - the type of changed reputation
        """
        ...


    def getOldValue(self) -> int:
        """
        Get the reputation value before the change.

        Returns
        - the reputation value before the change
        """
        ...


    def getNewValue(self) -> int:
        """
        Get new reputation value after the change.

        Returns
        - the reputation value after the change
        """
        ...


    def setNewValue(self, newValue: int) -> None:
        """
        Set new reputation value for this event.
        
        If the final value is below the reputation discard threshold, gossip
        associated with this reputation type will be removed.
        
        The provided value must be between 0 and
        VillagerReputationChangeEvent.getMaxValue(), otherwise an
        IllegalArgumentException will be thrown. Each reputation type
        may have a different maximum value.

        Arguments
        - newValue: the reputation value after the change

        See
        - Villager.ReputationType.getMaxValue()
        """
        ...


    def getMaxValue(self) -> int:
        """
        Get maximum value for the reputation type affected by this event.

        Returns
        - the maximum value for the reputation type affected by this event

        See
        - Villager.ReputationType.getMaxValue()
        """
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getEntity(self) -> "Villager":
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
