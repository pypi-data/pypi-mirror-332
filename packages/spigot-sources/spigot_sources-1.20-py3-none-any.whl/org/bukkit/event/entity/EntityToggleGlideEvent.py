"""
Python module generated from Java source file org.bukkit.event.entity.EntityToggleGlideEvent

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import LivingEntity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class EntityToggleGlideEvent(EntityEvent, Cancellable):
    """
    Sent when an entity's gliding status is toggled with an Elytra.
    Examples of when this event would be called:
    
        - Player presses the jump key while in midair and using an Elytra
        - Player lands on ground while they are gliding (with an Elytra)
    
    This can be visually estimated by the animation in which a player turns horizontal.
    """

    def __init__(self, who: "LivingEntity", isGliding: bool):
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def isGliding(self) -> bool:
        """
        Returns True if the entity is now gliding or
        False if the entity stops gliding.

        Returns
        - new gliding state
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
