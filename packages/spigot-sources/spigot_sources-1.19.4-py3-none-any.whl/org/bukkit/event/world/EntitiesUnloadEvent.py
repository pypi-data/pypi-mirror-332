"""
Python module generated from Java source file org.bukkit.event.world.EntitiesUnloadEvent

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Chunk
from org.bukkit.entity import Entity
from org.bukkit.event import HandlerList
from org.bukkit.event.world import *
from typing import Any, Callable, Iterable, Tuple


class EntitiesUnloadEvent(ChunkEvent):
    """
    Called when entities are unloaded.
    
    The provided chunk may or may not be loaded.
    """

    def __init__(self, chunk: "Chunk", entities: list["Entity"]):
        ...


    def getEntities(self) -> list["Entity"]:
        """
        Get the entities which are being unloaded.

        Returns
        - unmodifiable list of unloaded entities.
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
