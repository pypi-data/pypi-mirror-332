"""
Python module generated from Java source file org.bukkit.event.world.WorldUnloadEvent

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import World
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.world import *
from typing import Any, Callable, Iterable, Tuple


class WorldUnloadEvent(WorldEvent, Cancellable):
    """
    Called when a World is unloaded
    """

    def __init__(self, world: "World"):
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
