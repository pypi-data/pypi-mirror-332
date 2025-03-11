"""
Python module generated from Java source file org.bukkit.entity.minecart.ExplosiveMinecart

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Minecart
from org.bukkit.entity.minecart import *
from typing import Any, Callable, Iterable, Tuple


class ExplosiveMinecart(Minecart):
    """
    Represents a Minecart with TNT inside it that can explode when triggered.
    """

    def setFuseTicks(self, ticks: int) -> None:
        """
        Set the fuse ticks of this minecart.
        
        If the fuse ticks are set to a non-zero value, this will ignite the
        explosive.

        Arguments
        - ticks: the ticks
        """
        ...


    def getFuseTicks(self) -> int:
        """
        Get the fuse ticks of this minecart.
        
        If the fuse ticks reach 0, the minecart will explode.

        Returns
        - the fuse ticks, or -1 if this minecart's fuse has not yet been
        ignited
        """
        ...


    def ignite(self) -> None:
        """
        Ignite this minecart's fuse naturally.
        """
        ...


    def isIgnited(self) -> bool:
        """
        Check whether or not this minecart's fuse has been ignited.

        Returns
        - True if ignited, False otherwise
        """
        ...


    def explode(self) -> None:
        """
        Immediately explode this minecart with the power assumed by its current
        movement.
        """
        ...


    def explode(self, power: float) -> None:
        """
        Immediately explode this minecart with the given power.

        Arguments
        - power: the power to use. Must be positive and cannot exceed 5.0
        """
        ...
