"""
Python module generated from Java source file org.bukkit.event.entity.EntityCombustByBlockEvent

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.entity import Entity
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class EntityCombustByBlockEvent(EntityCombustEvent):
    """
    Called when a block causes an entity to combust.
    """

    def __init__(self, combuster: "Block", combustee: "Entity", duration: int):
        ...


    def __init__(self, combuster: "Block", combustee: "Entity", duration: float):
        ...


    def getCombuster(self) -> "Block":
        """
        The combuster can be lava or a block that is on fire.
        
        WARNING: block may be null.

        Returns
        - the Block that set the combustee alight.
        """
        ...
