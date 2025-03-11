"""
Python module generated from Java source file org.bukkit.event.entity.EntityRemoveEvent

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.entity import Entity
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class EntityRemoveEvent(EntityEvent):
    """
    Called when an Entity is removed.
    
    This event should only be used for monitoring. The result
    of modifying the entity during or after this event is unspecified.
    This event is not called for a org.bukkit.entity.Player.
    """

    def __init__(self, what: "Entity", cause: "Cause"):
        ...


    def getCause(self) -> "Cause":
        """
        Gets the cause why the entity got removed.

        Returns
        - the cause why the entity got removed
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...


    class Cause(Enum):
        """
        Represents various ways an entity gets removed.
        """

        DEATH = 0
        """
        When an entity dies.
        """
        DESPAWN = 1
        """
        When an entity does despawn. This includes mobs which are too far away,
        items or arrows which lay to long on the ground or area effect cloud.
        """
        DROP = 2
        """
        When an entity gets removed because it drops as an item.
        For example, trident or falling sand.
        
        **Note:** Depending on other factors, such as gamerules, no item will actually drop,
        the cause, however, will still be drop.
        """
        ENTER_BLOCK = 3
        """
        When an entity gets removed because it enters a block.
        For example, bees or silverfish.
        """
        EXPLODE = 4
        """
        When an entity gets removed because it exploded.
        For example, creepers, tnt or firework.
        """
        HIT = 5
        """
        When an entity gets removed because it hit something. This mainly applies to projectiles.
        """
        MERGE = 6
        """
        When an entity gets removed because it merges with another one.
        For example, items or xp.
        """
        OUT_OF_WORLD = 7
        """
        When an entity gets removed because it is too far below the world.
        This only applies to entities which get removed immediately,
        some entities get damage instead.
        """
        PICKUP = 8
        """
        When an entity gets removed because it got pickup.
        For example, items, arrows, xp or parrots which get on a player shoulder.
        """
        PLAYER_QUIT = 9
        """
        When an entity gets removed with a player because the player quits the game.
        For example, a boat which gets removed with the player when he quits.
        """
        PLUGIN = 10
        """
        When a plugin manually removes an entity.
        """
        TRANSFORMATION = 11
        """
        When an entity gets removed because it transforms into another one.
        """
        UNLOAD = 12
        """
        When the chunk an entity is in gets unloaded.
        """
