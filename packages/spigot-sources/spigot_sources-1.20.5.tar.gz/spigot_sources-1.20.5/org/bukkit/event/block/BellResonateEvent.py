"""
Python module generated from Java source file org.bukkit.event.block.BellResonateEvent

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.entity import LivingEntity
from org.bukkit.event import HandlerList
from org.bukkit.event.block import *
from typing import Any, Callable, Iterable, Tuple


class BellResonateEvent(BlockEvent):
    """
    Called when a bell resonated after being rung and highlights nearby raiders.
    A bell will only resonate if raiders are in the vicinity of the bell.
    """

    def __init__(self, theBlock: "Block", resonatedEntities: list["LivingEntity"]):
        ...


    def getResonatedEntities(self) -> list["LivingEntity"]:
        """
        Get a mutable list of all LivingEntity LivingEntities to be
        highlighted by the bell's resonating. This list can be added to or
        removed from to change which entities are highlighted, and may be empty
        if no entities were resonated as a result of this event.
        
        While the highlighted entities will change, the particles that display
        over a resonated entity and their colors will not. This is handled by the
        client and cannot be controlled by the server.

        Returns
        - a list of resonated entities
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
