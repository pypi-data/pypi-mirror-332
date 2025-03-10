"""
Python module generated from Java source file org.bukkit.event.entity.ItemSpawnEvent

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Location
from org.bukkit.entity import Item
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class ItemSpawnEvent(EntitySpawnEvent):
    """
    Called when an item is spawned into a world
    """

    def __init__(self, spawnee: "Item", loc: "Location"):
        ...


    def __init__(self, spawnee: "Item"):
        ...


    def getEntity(self) -> "Item":
        ...
