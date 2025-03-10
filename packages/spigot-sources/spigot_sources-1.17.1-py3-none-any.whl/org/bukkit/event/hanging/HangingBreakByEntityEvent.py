"""
Python module generated from Java source file org.bukkit.event.hanging.HangingBreakByEntityEvent

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Entity
from org.bukkit.entity import Hanging
from org.bukkit.event.hanging import *
from typing import Any, Callable, Iterable, Tuple


class HangingBreakByEntityEvent(HangingBreakEvent):
    """
    Triggered when a hanging entity is removed by an entity
    """

    def __init__(self, hanging: "Hanging", remover: "Entity"):
        ...


    def __init__(self, hanging: "Hanging", remover: "Entity", cause: "HangingBreakEvent.RemoveCause"):
        ...


    def getRemover(self) -> "Entity":
        """
        Gets the entity that removed the hanging entity.
        May be null, for example when broken by an explosion.

        Returns
        - the entity that removed the hanging entity
        """
        ...
