"""
Python module generated from Java source file org.bukkit.entity.Firework

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from org.bukkit.inventory.meta import FireworkMeta
from typing import Any, Callable, Iterable, Tuple


class Firework(Projectile):

    def getFireworkMeta(self) -> "FireworkMeta":
        """
        Get a copy of the fireworks meta

        Returns
        - A copy of the current Firework meta
        """
        ...


    def setFireworkMeta(self, meta: "FireworkMeta") -> None:
        """
        Apply the provided meta to the fireworks

        Arguments
        - meta: The FireworkMeta to apply
        """
        ...


    def setAttachedTo(self, entity: "LivingEntity") -> bool:
        """
        Set the LivingEntity to which this firework is attached.
        
        When attached to an entity, the firework effect will act as normal but
        remain positioned on the entity. If the entity `LivingEntity.isGliding()
        is gliding`, then the entity will receive a boost in the direction that
        they are looking.

        Arguments
        - entity: the entity to which the firework should be attached, or
        null to remove the attached entity

        Returns
        - True if the entity could be attached, False if the firework was
        already detonated
        """
        ...


    def getAttachedTo(self) -> "LivingEntity":
        """
        Get the LivingEntity to which this firework is attached.
        
        When attached to an entity, the firework effect will act as normal but
        remain positioned on the entity. If the entity `LivingEntity.isGliding()
        is gliding`, then the entity will receive a boost in the direction that
        they are looking.

        Returns
        - the attached entity, or null if none
        """
        ...


    def setLife(self, ticks: int) -> bool:
        """
        Set the ticks that this firework has been alive. If this value exceeds
        .getMaxLife(), the firework will detonate.

        Arguments
        - ticks: the ticks to set. Must be greater than or equal to 0

        Returns
        - True if the life was set, False if this firework has already detonated
        """
        ...


    def getLife(self) -> int:
        """
        Get the ticks that this firework has been alive. When this value reaches
        .getMaxLife(), the firework will detonate.

        Returns
        - the life ticks
        """
        ...


    def setMaxLife(self, ticks: int) -> bool:
        """
        Set the time in ticks this firework will exist until it is detonated.

        Arguments
        - ticks: the ticks to set. Must be greater than 0

        Returns
        - True if the time was set, False if this firework has already detonated
        """
        ...


    def getMaxLife(self) -> int:
        """
        Get the time in ticks this firework will exist until it is detonated.

        Returns
        - the maximum life in ticks
        """
        ...


    def detonate(self) -> None:
        """
        Cause this firework to explode at earliest opportunity, as if it has no
        remaining fuse.
        """
        ...


    def isDetonated(self) -> bool:
        """
        Check whether or not this firework has detonated.

        Returns
        - True if detonated, False if still in the world
        """
        ...


    def isShotAtAngle(self) -> bool:
        """
        Gets if the firework was shot at an angle (i.e. from a crossbow).
        
        A firework which was not shot at an angle will fly straight upwards.

        Returns
        - shot at angle status
        """
        ...


    def setShotAtAngle(self, shotAtAngle: bool) -> None:
        """
        Sets if the firework was shot at an angle (i.e. from a crossbow).
        
        A firework which was not shot at an angle will fly straight upwards.

        Arguments
        - shotAtAngle: the new shotAtAngle
        """
        ...
