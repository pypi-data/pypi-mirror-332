"""
Python module generated from Java source file org.bukkit.event.entity.PigZapEvent

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Collections
from org.bukkit.entity import Entity
from org.bukkit.entity import LightningStrike
from org.bukkit.entity import Pig
from org.bukkit.entity import PigZombie
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class PigZapEvent(EntityTransformEvent, Cancellable):
    """
    Stores data for pigs being zapped
    """

    def __init__(self, pig: "Pig", bolt: "LightningStrike", pigzombie: "PigZombie"):
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getEntity(self) -> "Pig":
        ...


    def getLightning(self) -> "LightningStrike":
        """
        Gets the bolt which is striking the pig.

        Returns
        - lightning entity
        """
        ...


    def getPigZombie(self) -> "PigZombie":
        """
        Gets the zombie pig that will replace the pig, provided the event is
        not cancelled first.

        Returns
        - resulting entity

        Deprecated
        - use EntityTransformEvent.getTransformedEntity()
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
