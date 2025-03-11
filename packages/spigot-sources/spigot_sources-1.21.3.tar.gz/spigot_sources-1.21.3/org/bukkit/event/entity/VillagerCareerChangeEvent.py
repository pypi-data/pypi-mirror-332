"""
Python module generated from Java source file org.bukkit.event.entity.VillagerCareerChangeEvent

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.entity import Villager
from org.bukkit.entity.Villager import Profession
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class VillagerCareerChangeEvent(EntityEvent, Cancellable):

    def __init__(self, what: "Villager", profession: "Profession", reason: "ChangeReason"):
        ...


    def getEntity(self) -> "Villager":
        ...


    def getProfession(self) -> "Profession":
        """
        Gets the future profession of the villager.

        Returns
        - The profession the villager will change to
        """
        ...


    def setProfession(self, profession: "Profession") -> None:
        """
        Sets the profession the villager will become from this event.

        Arguments
        - profession: new profession
        """
        ...


    def getReason(self) -> "ChangeReason":
        """
        Gets the reason for why the villager's career is changing.

        Returns
        - Reason for villager's profession changing
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


    class ChangeReason(Enum):
        """
        Reasons for the villager's profession changing.
        """

        LOSING_JOB = 0
        """
        Villager lost their job due to too little experience.
        """
        EMPLOYED = 1
        """
        Villager gained employment.
        """
