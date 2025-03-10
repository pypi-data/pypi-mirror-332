"""
Python module generated from Java source file org.bukkit.entity.Mob

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
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
