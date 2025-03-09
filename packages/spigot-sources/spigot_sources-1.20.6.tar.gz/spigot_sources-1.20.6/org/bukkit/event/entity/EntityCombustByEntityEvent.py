"""
Python module generated from Java source file org.bukkit.event.entity.EntityCombustByEntityEvent

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Entity
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class EntityCombustByEntityEvent(EntityCombustEvent):
    """
    Called when an entity causes another entity to combust.
    """

    def __init__(self, combuster: "Entity", combustee: "Entity", duration: int):
        ...


    def getCombuster(self) -> "Entity":
        """
        Get the entity that caused the combustion event.

        Returns
        - the Entity that set the combustee alight.
        """
        ...
