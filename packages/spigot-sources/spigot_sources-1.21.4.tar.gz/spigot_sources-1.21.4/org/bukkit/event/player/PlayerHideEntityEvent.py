"""
Python module generated from Java source file org.bukkit.event.player.PlayerHideEntityEvent

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Entity
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from typing import Any, Callable, Iterable, Tuple


class PlayerHideEntityEvent(PlayerEvent):
    """
    Called when a visible entity is hidden from a player.
    
    This event is only called when the entity's visibility status is actually
    changed.
    
    This event is called regardless of if the entity was within tracking range.

    See
    - Player.hideEntity(org.bukkit.plugin.Plugin, org.bukkit.entity.Entity)
    """

    def __init__(self, who: "Player", entity: "Entity"):
        ...


    def getEntity(self) -> "Entity":
        """
        Gets the entity which has been hidden from the player.

        Returns
        - the hidden entity
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
