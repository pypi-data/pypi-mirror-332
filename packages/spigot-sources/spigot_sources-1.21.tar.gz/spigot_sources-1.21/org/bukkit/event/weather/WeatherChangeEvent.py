"""
Python module generated from Java source file org.bukkit.event.weather.WeatherChangeEvent

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import World
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.weather import *
from typing import Any, Callable, Iterable, Tuple


class WeatherChangeEvent(WeatherEvent, Cancellable):
    """
    Stores data for weather changing in a world
    """

    def __init__(self, world: "World", to: bool):
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def toWeatherState(self) -> bool:
        """
        Gets the state of weather that the world is being set to

        Returns
        - True if the weather is being set to raining, False otherwise
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
