"""
Python module generated from Java source file org.bukkit.event.player.PlayerShowEntityEvent

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Entity
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from typing import Any, Callable, Iterable, Tuple


class PlayerShowEntityEvent(PlayerEvent):
    """
    Called when a hidden entity is shown to a player.
    
    This event is only called when the entity's visibility status is actually
    changed.
    
    This event is called regardless of whether the entity was within tracking
    range.

    See
    - Player.showEntity(org.bukkit.plugin.Plugin, org.bukkit.entity.Entity)

    Unknown Tags
    - draft API
    """

    def __init__(self, who: "Player", entity: "Entity"):
        ...


    def getEntity(self) -> "Entity":
        """
        Gets the entity which has been shown to the player.

        Returns
        - the shown entity
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
