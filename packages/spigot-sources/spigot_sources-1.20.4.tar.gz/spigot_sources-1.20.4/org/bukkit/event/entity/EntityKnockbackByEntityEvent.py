"""
Python module generated from Java source file org.bukkit.event.entity.EntityKnockbackByEntityEvent

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Entity
from org.bukkit.entity import LivingEntity
from org.bukkit.event.entity import *
from org.bukkit.util import Vector
from typing import Any, Callable, Iterable, Tuple


class EntityKnockbackByEntityEvent(EntityKnockbackEvent):
    """
    Called when an entity receives knockback from another entity.
    """

    def __init__(self, entity: "LivingEntity", source: "Entity", cause: "KnockbackCause", force: float, rawKnockback: "Vector", knockback: "Vector"):
        ...


    def getSourceEntity(self) -> "Entity":
        """
        Get the entity that has caused knockback to the defender.

        Returns
        - entity that caused knockback
        """
        ...
