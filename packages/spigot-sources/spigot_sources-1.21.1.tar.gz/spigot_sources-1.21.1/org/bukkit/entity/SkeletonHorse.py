"""
Python module generated from Java source file org.bukkit.entity.SkeletonHorse

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class SkeletonHorse(AbstractHorse):
    """
    Represents a SkeletonHorse - variant of AbstractHorse.
    """

    def isTrapped(self) -> bool:
        """
        Returns whether this skeleton horse is trapped.
        
        When a horse is trapped and a player comes within 10 blocks of a trapped
        horse, lightning will strike the horse. When struck, the skeleton trap
        will activate, turning the horse into a skeleton horseman as well as
        spawning three additional horsemen nearby.

        Returns
        - True if trapped
        """
        ...


    def setTrapped(self, trapped: bool) -> None:
        """
        Sets if this skeleton horse is trapped.

        Arguments
        - trapped: new trapped state
        """
        ...


    def getTrapTime(self) -> int:
        """
        Returns the horse's current trap time in ticks.
        
        Trap time is incremented every tick when .isTrapped() is True.
        The horse automatically despawns when it reaches 18000 ticks.

        Returns
        - current trap time
        """
        ...


    def setTrapTime(self, trapTime: int) -> None:
        """
        Sets the trap time for the horse.
        
        Values greater than 18000 will cause the horse to despawn on the next
        tick.

        Arguments
        - trapTime: new trap time
        """
        ...
