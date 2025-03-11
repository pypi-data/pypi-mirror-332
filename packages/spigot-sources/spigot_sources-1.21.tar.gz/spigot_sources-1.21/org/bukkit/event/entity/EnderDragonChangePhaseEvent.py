"""
Python module generated from Java source file org.bukkit.event.entity.EnderDragonChangePhaseEvent

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from org.bukkit.entity import EnderDragon
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class EnderDragonChangePhaseEvent(EntityEvent, Cancellable):
    """
    Called when an EnderDragon switches controller phase.
    """

    def __init__(self, enderDragon: "EnderDragon", currentPhase: "EnderDragon.Phase", newPhase: "EnderDragon.Phase"):
        ...


    def getEntity(self) -> "EnderDragon":
        ...


    def getCurrentPhase(self) -> "EnderDragon.Phase":
        """
        Gets the current phase that the dragon is in. This method will return null
        when a dragon is first spawned and hasn't yet been assigned a phase.

        Returns
        - the current dragon phase
        """
        ...


    def getNewPhase(self) -> "EnderDragon.Phase":
        """
        Gets the new phase that the dragon will switch to.

        Returns
        - the new dragon phase
        """
        ...


    def setNewPhase(self, newPhase: "EnderDragon.Phase") -> None:
        """
        Sets the new phase for the ender dragon.

        Arguments
        - newPhase: the new dragon phase
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
