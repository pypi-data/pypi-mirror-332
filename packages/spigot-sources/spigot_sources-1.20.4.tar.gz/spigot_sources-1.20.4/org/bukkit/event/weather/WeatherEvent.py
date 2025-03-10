"""
Python module generated from Java source file org.bukkit.event.weather.WeatherEvent

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import World
from org.bukkit.event import Event
from org.bukkit.event.weather import *
from typing import Any, Callable, Iterable, Tuple


class WeatherEvent(Event):
    """
    Represents a Weather-related event
    """

    def __init__(self, where: "World"):
        ...


    def getWorld(self) -> "World":
        """
        Returns the World where this event is occurring

        Returns
        - World this event is occurring in
        """
        ...
