"""
Python module generated from Java source file org.bukkit.event.entity.EntityKnockbackEvent

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from enum import Enum
from org.bukkit.attribute import Attribute
from org.bukkit.enchantments import Enchantment
from org.bukkit.entity import LivingEntity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from org.bukkit.util import Vector
from typing import Any, Callable, Iterable, Tuple


class EntityKnockbackEvent(EntityEvent, Cancellable):
    """
    Called when a living entity receives knockback.
    """

    def __init__(self, entity: "LivingEntity", cause: "KnockbackCause", force: float, rawKnockback: "Vector", knockback: "Vector"):
        ...


    def getEntity(self) -> "LivingEntity":
        ...


    def getCause(self) -> "KnockbackCause":
        """
        Gets the cause of the knockback.

        Returns
        - the cause of the knockback
        """
        ...


    def getForce(self) -> float:
        """
        Gets the raw force of the knockback. 
        This value is based on factors such as the Enchantment.KNOCKBACK
        level of an attacker and the
        Attribute.GENERIC_KNOCKBACK_RESISTANCE of the entity.

        Returns
        - the knockback force
        """
        ...


    def getKnockback(self) -> "Vector":
        """
        Gets the raw knockback force that will be applied to the entity. 
        This value is read-only, changes made to it **will not** have any
        effect on the final knockback received.

        Returns
        - the raw knockback

        See
        - .getFinalKnockback()
        """
        ...


    def getFinalKnockback(self) -> "Vector":
        """
        Gets the force that will be applied to the entity. 
        In contrast to EntityKnockbackEvent.getKnockback() this value is
        affected by the entities current velocity and whether they are touching
        the ground.
        
        **Note:** this method returns a copy, changes must be applied with
        .setFinalKnockback(Vector).

        Returns
        - the final knockback
        """
        ...


    def setFinalKnockback(self, knockback: "Vector") -> None:
        """
        Sets the force that will be applied to the entity.

        Arguments
        - knockback: the force to apply
        """
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...


    class KnockbackCause(Enum):
        """
        An enum to specify the cause of the knockback.
        """

        DAMAGE = 0
        """
        Knockback caused by non-entity damage.
        """
        ENTITY_ATTACK = 1
        """
        Knockback caused by an attacking entity.
        """
        EXPLOSION = 2
        """
        Knockback caused by an explosion.
        """
        SHIELD_BLOCK = 3
        """
        Knockback caused by the target blocking with a shield.
        """
        SWEEP_ATTACK = 4
        """
        Knockback caused by a sweeping attack.
        """
        UNKNOWN = 5
        """
        Knockback with an unknown cause.
        """
