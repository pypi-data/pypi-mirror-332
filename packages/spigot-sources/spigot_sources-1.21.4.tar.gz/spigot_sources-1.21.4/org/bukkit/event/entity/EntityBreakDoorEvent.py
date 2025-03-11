"""
Python module generated from Java source file org.bukkit.event.entity.EntityBreakDoorEvent

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.block import Block
from org.bukkit.entity import Entity
from org.bukkit.entity import LivingEntity
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class EntityBreakDoorEvent(EntityChangeBlockEvent):
    """
    Called when an Entity breaks a door
    
    Cancelling the event will cause the event to be delayed
    """

    def __init__(self, entity: "LivingEntity", targetBlock: "Block"):
        ...


    def getEntity(self) -> "LivingEntity":
        ...
