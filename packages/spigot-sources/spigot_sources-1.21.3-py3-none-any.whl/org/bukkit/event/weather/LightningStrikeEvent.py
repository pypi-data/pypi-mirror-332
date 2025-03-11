"""
Python module generated from Java source file org.bukkit.event.weather.LightningStrikeEvent

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit import World
from org.bukkit.entity import LightningStrike
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.weather import *
from typing import Any, Callable, Iterable, Tuple


class LightningStrikeEvent(WeatherEvent, Cancellable):
    """
    Stores data for lightning striking
    """

    def __init__(self, world: "World", bolt: "LightningStrike"):
        ...


    def __init__(self, world: "World", bolt: "LightningStrike", cause: "Cause"):
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getLightning(self) -> "LightningStrike":
        """
        Gets the bolt which is striking the earth.

        Returns
        - lightning entity
        """
        ...


    def getCause(self) -> "Cause":
        """
        Gets the cause of this lightning strike.

        Returns
        - strike cause
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...


    class Cause(Enum):

        COMMAND = 0
        """
        Triggered by the /summon command.
        """
        CUSTOM = 1
        """
        Triggered by a Plugin.
        """
        SPAWNER = 2
        """
        Triggered by a Spawner.
        """
        TRIDENT = 3
        """
        Triggered by an enchanted trident.
        """
        TRAP = 4
        """
        Triggered by a skeleton horse trap.
        """
        WEATHER = 5
        """
        Triggered by weather.
        """
        ENCHANTMENT = 6
        """
        Triggered by an enchantment but not a trident.
        """
        UNKNOWN = 7
        """
        Unknown trigger.
        """
