"""
Python module generated from Java source file org.bukkit.entity.Mob

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Sound
from org.bukkit.entity import *
from org.bukkit.loot import Lootable
from typing import Any, Callable, Iterable, Tuple


class Mob(LivingEntity, Lootable):
    """
    Represents a Mob. Mobs are living entities with simple AI.
    """

    def setTarget(self, target: "LivingEntity") -> None:
        """
        Instructs this Mob to set the specified LivingEntity as its target.
        
        Hostile creatures may attack their target, and friendly creatures may
        follow their target.

        Arguments
        - target: New LivingEntity to target, or null to clear the target
        """
        ...


    def getTarget(self) -> "LivingEntity":
        """
        Gets the current target of this Mob

        Returns
        - Current target of this creature, or null if none exists
        """
        ...


    def setAware(self, aware: bool) -> None:
        """
        Sets whether this mob is aware of its surroundings.
        
        Unaware mobs will still move if pushed, attacked, etc. but will not move
        or perform any actions on their own. Unaware mobs may also have other
        unspecified behaviours disabled, such as drowning.

        Arguments
        - aware: whether the mob is aware
        """
        ...


    def isAware(self) -> bool:
        """
        Gets whether this mob is aware of its surroundings.
        
        Unaware mobs will still move if pushed, attacked, etc. but will not move
        or perform any actions on their own. Unaware mobs may also have other
        unspecified behaviours disabled, such as drowning.

        Returns
        - whether the mob is aware
        """
        ...


    def getAmbientSound(self) -> "Sound":
        """
        Get the Sound this mob makes while ambiently existing. This sound
        may change depending on the current state of the entity, and may also
        return null under specific conditions. This sound is not constant.
        For instance, villagers will make different passive noises depending
        on whether or not they are actively trading with a player, or make no
        ambient noise while sleeping.

        Returns
        - the ambient sound, or null if this entity is ambiently quiet
        """
        ...
