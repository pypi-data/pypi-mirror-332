"""
Python module generated from Java source file org.bukkit.event.entity.EntityTargetLivingEntityEvent

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Entity
from org.bukkit.entity import LivingEntity
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class EntityTargetLivingEntityEvent(EntityTargetEvent):
    """
    Called when an Entity targets a LivingEntity and can only target
    LivingEntity's.
    """

    def __init__(self, entity: "Entity", target: "LivingEntity", reason: "TargetReason"):
        ...


    def getTarget(self) -> "LivingEntity":
        ...


    def setTarget(self, target: "Entity") -> None:
        """
        Set the Entity that you want the mob to target.
        
        It is possible to be null, null will cause the entity to be
        target-less.
        
        Must be a LivingEntity, or null.

        Arguments
        - target: The entity to target
        """
        ...
