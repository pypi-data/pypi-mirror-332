"""
Python module generated from Java source file org.bukkit.event.server.MapInitializeEvent

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.event import HandlerList
from org.bukkit.event.server import *
from org.bukkit.map import MapView
from typing import Any, Callable, Iterable, Tuple


class MapInitializeEvent(ServerEvent):
    """
    Called when a map is initialized.
    """

    def __init__(self, mapView: "MapView"):
        ...


    def getMap(self) -> "MapView":
        """
        Gets the map initialized in this event.

        Returns
        - Map for this event
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
