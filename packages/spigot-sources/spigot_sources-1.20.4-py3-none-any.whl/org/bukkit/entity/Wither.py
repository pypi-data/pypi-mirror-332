"""
Python module generated from Java source file org.bukkit.entity.Wither

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Wither(Monster, Boss):
    """
    Represents a Wither boss
    """

    def setTarget(self, target: "LivingEntity") -> None:
        """
        
        
        This method will set the target of the Head.CENTER center head of
        the wither.

        See
        - .setTarget(org.bukkit.entity.Wither.Head, org.bukkit.entity.LivingEntity)
        """
        ...


    def setTarget(self, head: "Head", target: "LivingEntity") -> None:
        """
        This method will set the target of individual heads Head of the
        wither.

        Arguments
        - head: the individual head
        - target: the entity that should be targeted
        """
        ...


    def getTarget(self, head: "Head") -> "LivingEntity":
        """
        This method will get the target of individual heads Head of the
        wither.

        Arguments
        - head: the individual head

        Returns
        - the entity targeted by the given head, or null if none is
        targeted
        """
        ...


    def getInvulnerabilityTicks(self) -> int:
        """
        Returns the wither's current invulnerability ticks.

        Returns
        - amount of invulnerability ticks
        """
        ...


    def setInvulnerabilityTicks(self, ticks: int) -> None:
        """
        Sets the wither's current invulnerability ticks.
        
        When invulnerability ticks reach 0, the wither will trigger an explosion.

        Arguments
        - ticks: amount of invulnerability ticks
        """
        ...
