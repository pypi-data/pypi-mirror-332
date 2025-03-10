"""
Python module generated from Java source file org.bukkit.event.world.EntitiesLoadEvent

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Chunk
from org.bukkit.entity import Entity
from org.bukkit.event import HandlerList
from org.bukkit.event.world import *
from typing import Any, Callable, Iterable, Tuple


class EntitiesLoadEvent(ChunkEvent):
    """
    Called when entities are loaded.
    
    The provided chunk may or may not be loaded.
    """

    def __init__(self, chunk: "Chunk", entities: list["Entity"]):
        ...


    def getEntities(self) -> list["Entity"]:
        """
        Get the entities which are being loaded.

        Returns
        - unmodifiable list of loaded entities.
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
