"""
Python module generated from Java source file org.bukkit.event.world.WorldEvent

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import World
from org.bukkit.event import Event
from org.bukkit.event.world import *
from typing import Any, Callable, Iterable, Tuple


class WorldEvent(Event):
    """
    Represents events within a world
    """

    def __init__(self, world: "World"):
        ...


    def __init__(self, world: "World", isAsync: bool):
        ...


    def getWorld(self) -> "World":
        """
        Gets the world primarily involved with this event

        Returns
        - World which caused this event
        """
        ...
