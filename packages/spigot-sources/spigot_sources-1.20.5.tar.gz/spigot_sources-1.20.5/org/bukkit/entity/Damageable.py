"""
Python module generated from Java source file org.bukkit.entity.Damageable

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.attribute import Attribute
from org.bukkit.damage import DamageSource
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Damageable(Entity):
    """
    Represents an Entity that has health and can take damage.
    """

    def damage(self, amount: float) -> None:
        """
        Deals the given amount of damage to this entity.

        Arguments
        - amount: Amount of damage to deal
        """
        ...


    def damage(self, amount: float, source: "Entity") -> None:
        """
        Deals the given amount of damage to this entity from a specified
        Entity.

        Arguments
        - amount: amount of damage to deal
        - source: entity to which the damage should be attributed
        """
        ...


    def damage(self, amount: float, damageSource: "DamageSource") -> None:
        """
        Deals the given amount of damage to this entity from a specified
        DamageSource.

        Arguments
        - amount: amount of damage to deal
        - damageSource: source to which the damage should be attributed
        """
        ...


    def getHealth(self) -> float:
        """
        Gets the entity's health from 0 to .getMaxHealth(), where 0 is dead.

        Returns
        - Health represented from 0 to max
        """
        ...


    def setHealth(self, health: float) -> None:
        """
        Sets the entity's health from 0 to .getMaxHealth(), where 0 is
        dead.

        Arguments
        - health: New health represented from 0 to max

        Raises
        - IllegalArgumentException: Thrown if the health is < 0 or >
            .getMaxHealth()
        """
        ...


    def getAbsorptionAmount(self) -> float:
        """
        Gets the entity's absorption amount.

        Returns
        - absorption amount from 0
        """
        ...


    def setAbsorptionAmount(self, amount: float) -> None:
        """
        Sets the entity's absorption amount.
        
        Note: The amount is capped to the value of
        Attribute.GENERIC_MAX_ABSORPTION. The effect of this method on
        that attribute is currently unspecified and subject to change.

        Arguments
        - amount: new absorption amount from 0

        Raises
        - IllegalArgumentException: thrown if health is < 0 or
        non-finite.
        """
        ...


    def getMaxHealth(self) -> float:
        """
        Gets the maximum health this entity has.

        Returns
        - Maximum health

        Deprecated
        - use Attribute.GENERIC_MAX_HEALTH.
        """
        ...


    def setMaxHealth(self, health: float) -> None:
        """
        Sets the maximum health this entity can have.
        
        If the health of the entity is above the value provided it will be set
        to that value.
        
        Note: An entity with a health bar (Player, EnderDragon,
        Wither, etc...} will have their bar scaled accordingly.

        Arguments
        - health: amount of health to set the maximum to

        Deprecated
        - use Attribute.GENERIC_MAX_HEALTH.
        """
        ...


    def resetMaxHealth(self) -> None:
        """
        Resets the max health to the original amount.

        Deprecated
        - use Attribute.GENERIC_MAX_HEALTH.
        """
        ...
