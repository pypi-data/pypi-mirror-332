"""
Python module generated from Java source file org.bukkit.event.entity.EntityTargetEvent

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.entity import Entity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class EntityTargetEvent(EntityEvent, Cancellable):
    """
    Called when a creature targets or untargets another entity
    """

    def __init__(self, entity: "Entity", target: "Entity", reason: "TargetReason"):
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getReason(self) -> "TargetReason":
        """
        Returns the reason for the targeting

        Returns
        - The reason
        """
        ...


    def getTarget(self) -> "Entity":
        """
        Get the entity that this is targeting.
        
        This will be null in the case that the event is called when the mob
        forgets its target.

        Returns
        - The entity
        """
        ...


    def setTarget(self, target: "Entity") -> None:
        """
        Set the entity that you want the mob to target instead.
        
        It is possible to be null, null will cause the entity to be
        target-less.
        
        This is different from cancelling the event. Cancelling the event will
        cause the entity to keep an original target, while setting to be null
        will cause the entity to be reset.

        Arguments
        - target: The entity to target
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...


    class TargetReason(Enum):
        """
        An enum to specify the reason for the targeting
        """

        TARGET_DIED = 0
        """
        When the entity's target has died, and so it no longer targets it
        """
        CLOSEST_PLAYER = 1
        """
        When the entity doesn't have a target, so it attacks the nearest
        player
        """
        TARGET_ATTACKED_ENTITY = 2
        """
        When the target attacks the entity, so entity targets it
        """
        PIG_ZOMBIE_TARGET = 3
        """
        When the target attacks a fellow pig zombie, so the whole group
        will target him with this reason.

        Deprecated
        - obsoleted by .TARGET_ATTACKED_NEARBY_ENTITY
        """
        FORGOT_TARGET = 4
        """
        When the target is forgotten for whatever reason.
        """
        TARGET_ATTACKED_OWNER = 5
        """
        When the target attacks the owner of the entity, so the entity
        targets it.
        """
        OWNER_ATTACKED_TARGET = 6
        """
        When the owner of the entity attacks the target attacks, so the
        entity targets it.
        """
        RANDOM_TARGET = 7
        """
        When the entity has no target, so the entity randomly chooses one.
        """
        DEFEND_VILLAGE = 8
        """
        When an entity selects a target while defending a village.
        """
        TARGET_ATTACKED_NEARBY_ENTITY = 9
        """
        When the target attacks a nearby entity of the same type, so the entity targets it
        """
        REINFORCEMENT_TARGET = 10
        """
        When a zombie targeting an entity summons reinforcements, so the reinforcements target the same entity
        """
        COLLISION = 11
        """
        When an entity targets another entity after colliding with it.
        """
        CUSTOM = 12
        """
        For custom calls to the event.
        """
        CLOSEST_ENTITY = 13
        """
        When the entity doesn't have a target, so it attacks the nearest
        entity
        """
        FOLLOW_LEADER = 14
        """
        When a raiding entity selects the same target as one of its compatriots.
        """
        TEMPT = 15
        """
        When another entity tempts this entity by having a desired item such
        as wheat in it's hand.
        """
        UNKNOWN = 16
        """
        A currently unknown reason for the entity changing target.
        """
