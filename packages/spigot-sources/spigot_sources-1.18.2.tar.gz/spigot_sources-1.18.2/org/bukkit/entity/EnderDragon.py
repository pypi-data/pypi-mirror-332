"""
Python module generated from Java source file org.bukkit.entity.EnderDragon

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import World
from org.bukkit.boss import DragonBattle
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class EnderDragon(ComplexLivingEntity, Boss, Mob):
    """
    Represents an Ender Dragon
    """

    def getPhase(self) -> "Phase":
        """
        Gets the current phase that the dragon is performing.

        Returns
        - the current phase
        """
        ...


    def setPhase(self, phase: "Phase") -> None:
        """
        Sets the next phase for the dragon to perform.

        Arguments
        - phase: the next phase
        """
        ...


    def getDragonBattle(self) -> "DragonBattle":
        """
        Get the DragonBattle associated with this EnderDragon.
        
        This will return null if the EnderDragon is not in the End dimension.

        Returns
        - the dragon battle

        See
        - World.getEnderDragonBattle()
        """
        ...


    def getDeathAnimationTicks(self) -> int:
        """
        Get the current time in ticks relative to the start of this dragon's
        death animation.
        
        If this dragon is alive, 0 will be returned. This value will never exceed
        200 (the length of the animation).

        Returns
        - this dragon's death animation ticks
        """
        ...
