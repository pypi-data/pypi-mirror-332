"""
Python module generated from Java source file org.bukkit.event.block.EntityBlockFormEvent

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.block import BlockState
from org.bukkit.entity import Entity
from org.bukkit.event.block import *
from typing import Any, Callable, Iterable, Tuple


class EntityBlockFormEvent(BlockFormEvent):
    """
    Called when a block is formed by entities.
    
    Examples:
    
    - Snow formed by a org.bukkit.entity.Snowman.
    - Frosted Ice formed by the Frost Walker enchantment.
    """

    def __init__(self, entity: "Entity", block: "Block", blockstate: "BlockState"):
        ...


    def getEntity(self) -> "Entity":
        """
        Get the entity that formed the block.

        Returns
        - Entity involved in event
        """
        ...
