"""
Python module generated from Java source file org.bukkit.damage.DamageSource

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Bukkit
from org.bukkit import Location
from org.bukkit.damage import *
from org.bukkit.entity import Entity
from typing import Any, Callable, Iterable, Tuple


class DamageSource:
    """
    Represents a source of damage.
    """

    def getDamageType(self) -> "DamageType":
        """
        Get the DamageType.

        Returns
        - the damage type
        """
        ...


    def getCausingEntity(self) -> "Entity":
        """
        Get the Entity that caused the damage to occur.
        
        Not to be confused with .getDirectEntity(), the causing entity is
        the entity to which the damage is ultimately attributed if the receiver
        is killed. If, for example, the receiver was damaged by a projectile, the
        shooter/thrower would be returned.

        Returns
        - an Entity or null
        """
        ...


    def getDirectEntity(self) -> "Entity":
        """
        Get the Entity that directly caused the damage.
        
        Not to be confused with .getCausingEntity(), the direct entity is
        the entity that actually inflicted the damage. If, for example, the
        receiver was damaged by a projectile, the projectile would be returned.

        Returns
        - an Entity or null
        """
        ...


    def getDamageLocation(self) -> "Location":
        """
        Get the Location from where the damage originated. This will only
        be present if an entity did not cause the damage.

        Returns
        - the location, or null if none
        """
        ...


    def getSourceLocation(self) -> "Location":
        """
        Get the Location from where the damage originated.
        
        This is a convenience method to get the final location of the damage.
        This method will attempt to return
        .getDamageLocation() the damage location. If this is null, the
        .getCausingEntity() causing entity location will be returned.
        Finally if there is no damage location nor a causing entity, null will be
        returned.

        Returns
        - the source of the location or null.
        """
        ...


    def isIndirect(self) -> bool:
        """
        Get if this damage is indirect.
        
        Damage is considered indirect if .getCausingEntity() is not equal
        to .getDirectEntity(). This will be the case, for example, if a
        skeleton shot an arrow or a player threw a potion.

        Returns
        - `True` if is indirect, `False` otherwise.
        """
        ...


    def getFoodExhaustion(self) -> float:
        """
        Get the amount of hunger exhaustion caused by this damage.

        Returns
        - the amount of hunger exhaustion caused.
        """
        ...


    def scalesWithDifficulty(self) -> bool:
        """
        Gets if this source of damage scales with difficulty.

        Returns
        - `True` if scales.
        """
        ...


    @staticmethod
    def builder(damageType: "DamageType") -> "Builder":
        """
        Create a new DamageSource.Builder.

        Arguments
        - damageType: the DamageType to use

        Returns
        - a DamageSource.Builder
        """
        ...


    class Builder:
        """
        Utility class to make building a DamageSource easier. Only a
        DamageType is required.
        """

        def withCausingEntity(self, entity: "Entity") -> "Builder":
            """
            Set the Entity that caused the damage.

            Arguments
            - entity: the entity

            Returns
            - this instance. Allows for chained method calls

            See
            - DamageSource.getCausingEntity()
            """
            ...


        def withDirectEntity(self, entity: "Entity") -> "Builder":
            """
            Set the Entity that directly inflicted the damage.

            Arguments
            - entity: the entity

            Returns
            - this instance. Allows for chained method calls

            See
            - DamageSource.getDirectEntity()
            """
            ...


        def withDamageLocation(self, location: "Location") -> "Builder":
            """
            Set the Location of the source of damage.

            Arguments
            - location: the location where the damage occurred

            Returns
            - this instance. Allows for chained method calls

            See
            - DamageSource.getSourceLocation()
            """
            ...


        def build(self) -> "DamageSource":
            """
            Create a new DamageSource instance using the supplied
            parameters.

            Returns
            - the damage source instance
            """
            ...
