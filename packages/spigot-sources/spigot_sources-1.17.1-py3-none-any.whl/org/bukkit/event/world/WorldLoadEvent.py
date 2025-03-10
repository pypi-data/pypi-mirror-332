"""
Python module generated from Java source file org.bukkit.event.world.WorldLoadEvent

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import World
from org.bukkit.event import HandlerList
from org.bukkit.event.world import *
from typing import Any, Callable, Iterable, Tuple


class WorldLoadEvent(WorldEvent):
    """
    Called when a World is loaded
    """

    def __init__(self, world: "World"):
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
